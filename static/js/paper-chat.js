(() => {
  const cfg = window.QS_AGENT;
  if (!cfg || !cfg.enable) return;

  const apiBase = String(cfg.apiBase || "http://127.0.0.1:8000")
    .trim().replace(/^["']|["']$/g, "").replace(/\/$/, "");

  document.addEventListener("click", (e) => {
    const toggle = e.target.closest(".qs-paper-chat__toggle");
    if (toggle) {
      const root = toggle.closest(".qs-paper-chat");
      const panel = root.querySelector(".qs-paper-chat__panel");
      panel.hidden = !panel.hidden;
      if (!panel.hidden) {
        const log = root.querySelector(".qs-paper-chat__log");
        if (!log.children.length) {
          appendBubble(log, "assistant", "Hi — ask me anything about this paper. I'll answer based on its abstract and context.");
        }
        root.querySelector(".qs-paper-chat__input").focus();
      }
      return;
    }
    const close = e.target.closest(".qs-paper-chat__close");
    if (close) {
      close.closest(".qs-paper-chat__panel").hidden = true;
    }
  });

  document.addEventListener("submit", async (e) => {
    const form = e.target.closest(".qs-paper-chat__form");
    if (!form) return;
    e.preventDefault();
    if (form.dataset.busy === "1") return;
    const root = form.closest(".qs-paper-chat");
    const input = form.querySelector(".qs-paper-chat__input");
    const log = root.querySelector(".qs-paper-chat__log");
    const send = form.querySelector(".qs-paper-chat__send");
    const text = input.value.trim();
    if (!text) return;

    input.value = "";
    appendBubble(log, "user", text);
    const bubble = appendBubble(log, "assistant", "");
    bubble.classList.add("is-streaming");

    const context = atob(root.dataset.qsContext || "");
    const messages = [{ role: "user", content: text }];
    form.dataset.busy = "1";
    send.disabled = true;
    input.disabled = true;

    try {
      const res = await fetch(`${apiBase}/api/chat`, {
        method: "POST",
        headers: { "Content-Type": "application/json", ...(cfg.apiKey ? { "X-API-Key": cfg.apiKey } : {}) },
        body: JSON.stringify({ messages, stream: true, context }),
      });
      if (!res.ok) throw new Error(`HTTP ${res.status}`);
      await readStream(res, bubble);
    } catch (err) {
      bubble.textContent = "Could not reach the agent. Make sure the local service is running.";
    } finally {
      bubble.classList.remove("is-streaming");
      delete form.dataset.busy;
      send.disabled = false;
      input.disabled = false;
      input.focus();
    }
  });

  function appendBubble(log, role, text) {
    const b = document.createElement("div");
    b.className = `qs-paper-chat__bubble qs-paper-chat__bubble--${role}`;
    if (role === "assistant" && window.qsRenderMd) {
      b.innerHTML = window.qsRenderMd(text);
    } else {
      b.textContent = text;
    }
    log.append(b);
    log.scrollTop = log.scrollHeight;
    return b;
  }

  async function readStream(res, bubble) {
    const reader = res.body.getReader();
    const decoder = new TextDecoder();
    let buf = "", full = "";
    while (true) {
      const { value, done } = await reader.read();
      if (done) break;
      buf += decoder.decode(value, { stream: true });
      const lines = buf.split("\n");
      buf = lines.pop() || "";
      for (const line of lines) {
        const t = line.trim();
        if (!t.startsWith("data:")) continue;
        const payload = t.slice(5).trim();
        if (payload === "[DONE]") continue;
        try {
          const obj = JSON.parse(payload);
          if (obj.delta) {
            full += obj.delta;
            bubble.innerHTML = window.qsRenderMd ? window.qsRenderMd(full) : full;
          }
        } catch {}
      }
    }
    if (!full) bubble.innerHTML = window.qsRenderMd ? window.qsRenderMd("(empty response)") : "(empty response)";
  }
})();
