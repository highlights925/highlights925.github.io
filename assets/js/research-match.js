(() => {
  const cfg = window.QS_AGENT;
  if (!cfg || !cfg.enable) return;

  const apiBase = String(cfg.apiBase || "http://127.0.0.1:8000")
    .trim().replace(/^["']|["']$/g, "").replace(/\/$/, "");

  const form = document.getElementById("qs-match-form");
  if (!form) return;

  const input = document.getElementById("qs-match-input");
  const result = document.getElementById("qs-match-result");
  const btn = form.querySelector(".qs-match__btn");

  let busy = false;
  form.addEventListener("submit", async (e) => {
    e.preventDefault();
    if (busy) return;
    const interest = input.value.trim();
    if (!interest) return;

    busy = true;
    input.value = "";
    btn.disabled = true;
    input.disabled = true;
    result.hidden = false;
    result.innerHTML = '<span class="qs-match__loading">Matching…</span>';

    try {
      const res = await fetch(`${apiBase}/api/match`, {
        method: "POST",
        headers: { "Content-Type": "application/json", ...(cfg.apiKey ? { "X-API-Key": cfg.apiKey } : {}) },
        body: JSON.stringify({ interest }),
      });
      if (!res.ok) throw new Error(`HTTP ${res.status}`);
      const data = await res.json();
      result.innerHTML = "";
      const card = document.createElement("div");
      card.className = "qs-match__card";
      card.innerHTML = window.qsRenderMd ? window.qsRenderMd(data.reply) : data.reply;
      result.append(card);
    } catch (err) {
      result.innerHTML = '<span class="qs-match__error">Could not reach the agent. Make sure the local service is running.</span>';
    } finally {
      busy = false;
      btn.disabled = false;
      input.disabled = false;
      input.focus();
    }
  });
})();
