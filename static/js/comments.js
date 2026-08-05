(() => {
  const cfg = window.QS_AGENT;
  if (!cfg || !cfg.enable) return;

  const apiBase = String(cfg.apiBase || "http://127.0.0.1:8000")
    .trim().replace(/^["']|["']$/g, "").replace(/\/$/, "");
  const apiKey = cfg.apiKey || "";

  const headers = { "Content-Type": "application/json", ...(apiKey ? { "X-API-Key": apiKey } : {}) };

  document.querySelectorAll(".qs-comments").forEach(async (root) => {
    const pageId = root.dataset.pageId;
    const pageTitle = root.dataset.pageTitle || document.title;
    if (!pageId) return;

    root.innerHTML = `
      <h3 class="qs-comments__title">Comments</h3>
      <form class="qs-comments__form">
        <input class="qs-comments__name" type="text" placeholder="Your name" maxlength="80" required />
        <input class="qs-comments__email" type="email" placeholder="Email (optional, not shown)" />
        <textarea class="qs-comments__text" placeholder="Leave a comment…" rows="3" maxlength="2000" required></textarea>
        <button class="qs-comments__submit" type="submit">Post comment</button>
      </form>
      <div class="qs-comments__list"></div>
    `;

    const listEl = root.querySelector(".qs-comments__list");
    const form = root.querySelector(".qs-comments__form");
    const submit = root.querySelector(".qs-comments__submit");

    async function load() {
      listEl.innerHTML = '<span class="qs-comments__loading">Loading…</span>';
      try {
        const res = await fetch(`${apiBase}/api/comments?page_id=${encodeURIComponent(pageId)}`, { headers });
        if (!res.ok) throw new Error(res.status);
        const data = await res.json();
        render(data.comments || []);
      } catch {
        listEl.innerHTML = '<span class="qs-comments__error">Could not load comments (is the agent service running?).</span>';
      }
    }

    function render(comments) {
      if (!comments.length) {
        listEl.innerHTML = '<span class="qs-comments__empty">No comments yet — be the first to leave one.</span>';
        return;
      }
      listEl.innerHTML = "";
      comments.forEach((c) => {
        const item = document.createElement("div");
        item.className = "qs-comment";
        const date = new Date(c.created_at * 1000).toLocaleDateString("en-US", {
          year: "numeric", month: "short", day: "numeric",
        });
        item.innerHTML = `
          <div class="qs-comment__avatar">${(c.name || "?").charAt(0).toUpperCase()}</div>
          <div class="qs-comment__body">
            <div class="qs-comment__meta">
              <span class="qs-comment__name">${escapeHtml(c.name)}</span>
              <span class="qs-comment__date">${date}</span>
              ${c.reply_count ? `<span class="qs-comment__replies">${c.reply_count} reply${c.reply_count > 1 ? "s" : ""}</span>` : ""}
            </div>
            <p class="qs-comment__text">${escapeHtml(c.text)}</p>
          </div>
        `;
        listEl.append(item);
      });
    }

    form.addEventListener("submit", async (e) => {
      e.preventDefault();
      const name = root.querySelector(".qs-comments__name").value.trim();
      const text = root.querySelector(".qs-comments__text").value.trim();
      const email = root.querySelector(".qs-comments__email").value.trim();
      if (!name || !text) return;

      submit.disabled = true;
      submit.textContent = "Posting…";
      try {
        const res = await fetch(`${apiBase}/api/comments`, {
          method: "POST", headers,
          body: JSON.stringify({ page_id: pageId, page_title: pageTitle, name, text, email }),
        });
        if (!res.ok) throw new Error(res.status);
        form.reset();
        await load();
      } catch {
        alert("Could not post comment. Make sure the agent service is running.");
      } finally {
        submit.disabled = false;
        submit.textContent = "Post comment";
      }
    });

    function escapeHtml(s) {
      const d = document.createElement("div");
      d.textContent = s;
      return d.innerHTML;
    }

    load();
  });
})();
