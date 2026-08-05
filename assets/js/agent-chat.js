(() => {
  const cfg = window.QS_AGENT || {};
  if (!cfg.enable) {
    console.warn("QS_AGENT disabled or missing; chat UI not mounted");
    return;
  }

  const apiBase = String(cfg.apiBase || "http://127.0.0.1:8000")
    .trim()
    .replace(/^["']|["']$/g, "")
    .replace(/\/$/, "");
  const apiKey = cfg.apiKey || "";
  const title = cfg.title || "Ask about Qi Sun";
  const placeholder = cfg.placeholder || "Ask about research, education, papers…";
  const welcome =
    cfg.welcome ||
    "Hi — I can answer questions about Qi Sun's background, research, and publications. The assistant only works while the local agent service is online.";

  const state = {
    messages: [],
    busy: false,
    online: null,
  };

  function el(tag, className, text) {
    const node = document.createElement(tag);
    if (className) node.className = className;
    if (text != null) node.textContent = text;
    return node;
  }

  function mountShell(container, { floating }) {
    container.innerHTML = "";
    container.classList.add("qs-agent");
    if (floating) container.classList.add("qs-agent--floating");

    const panel = el("div", "qs-agent__panel");
    panel.setAttribute("role", "dialog");
    panel.setAttribute("aria-label", title);

    const header = el("div", "qs-agent__header");
    const heading = el("div", "qs-agent__title", title);
    const status = el("div", "qs-agent__status", "Checking…");
    status.dataset.role = "status";
    header.append(heading, status);

    if (floating) {
      const close = el("button", "qs-agent__icon-btn", "×");
      close.type = "button";
      close.setAttribute("aria-label", "Close");
      close.addEventListener("click", () => container.classList.remove("is-open"));
      header.append(close);
    }

    const log = el("div", "qs-agent__log");
    log.dataset.role = "log";

    const form = el("form", "qs-agent__form");
    const input = el("textarea", "qs-agent__input");
    input.rows = 2;
    input.placeholder = placeholder;
    input.setAttribute("aria-label", "Message");
    const send = el("button", "qs-agent__send", "Send");
    send.type = "submit";
    form.append(input, send);

    panel.append(header, log, form);
    container.append(panel);

    if (floating) {
      const fab = el("button", "qs-agent__fab", "Ask");
      fab.type = "button";
      fab.setAttribute("aria-label", "Open Q&A assistant");
      fab.addEventListener("click", () => {
        container.classList.toggle("is-open");
        if (container.classList.contains("is-open")) input.focus();
      });
      container.append(fab);
    }

    appendBubble(log, "assistant", welcome);
    wireForm(form, input, send, log, status);
    ping(status);
    wireHintChips(input, form);
  }

  function wireHintChips(input, form) {
    const hints = document.getElementById("qs-ask-hints");
    if (!hints) return;
    hints.addEventListener("click", (e) => {
      const btn = e.target.closest("[data-qs-prompt]");
      if (!btn || state.busy) return;
      input.value = btn.getAttribute("data-qs-prompt") || "";
      form.requestSubmit();
    });
  }

  function appendBubble(log, role, text) {
    const bubble = el("div", `qs-agent__bubble qs-agent__bubble--${role}`);
    if (role === "assistant" && window.qsRenderMd) {
      bubble.innerHTML = window.qsRenderMd(text);
    } else {
      bubble.textContent = text;
    }
    log.append(bubble);
    log.scrollTop = log.scrollHeight;
    return bubble;
  }

  function setStatus(statusEl, online, detail) {
    state.online = online;
    statusEl.textContent = online ? "Online" : detail || "Offline";
    statusEl.classList.toggle("is-online", !!online);
    statusEl.classList.toggle("is-offline", online === false);
  }

  async function ping(statusEl) {
    try {
      const res = await fetch(`${apiBase}/health`, { method: "GET" });
      if (!res.ok) throw new Error("bad status");
      const data = await res.json();
      setStatus(statusEl, true, data.model || "ok");
      statusEl.title = data.model ? `model: ${data.model}` : "";
    } catch {
      setStatus(statusEl, false, "Offline — start local agent");
    }
  }

  function wireForm(form, input, send, log, status) {
    form.addEventListener("submit", async (e) => {
      e.preventDefault();
      if (state.busy) return;
      const text = input.value.trim();
      if (!text) return;

      input.value = "";
      input.disabled = true;
      appendBubble(log, "user", text);
      state.messages.push({ role: "user", content: text });
      const assistantBubble = appendBubble(log, "assistant", "");
      assistantBubble.classList.add("is-streaming");

      state.busy = true;
      send.disabled = true;
      try {
        await streamReply(assistantBubble, status);
      } catch (err) {
        assistantBubble.textContent =
          assistantBubble.textContent ||
          `Could not reach the agent (${err.message}). Start services/agent and check api_base.`;
        setStatus(status, false, "Offline");
      } finally {
        assistantBubble.classList.remove("is-streaming");
        state.busy = false;
        send.disabled = false;
        input.disabled = false;
        input.focus();
      }
    });

    input.addEventListener("keydown", (e) => {
      if (e.key === "Enter" && !e.shiftKey) {
        e.preventDefault();
        form.requestSubmit();
      }
    });
  }

  async function streamReply(bubble, status) {
    const headers = { "Content-Type": "application/json" };
    if (apiKey) headers["X-API-Key"] = apiKey;

    const res = await fetch(`${apiBase}/api/chat`, {
      method: "POST",
      headers,
      body: JSON.stringify({ messages: state.messages, stream: true }),
    });

    if (!res.ok) {
      const errText = await res.text();
      throw new Error(errText || `HTTP ${res.status}`);
    }

    setStatus(status, true);
    const reader = res.body.getReader();
    const decoder = new TextDecoder();
    let buffer = "";
    let full = "";

    while (true) {
      const { value, done } = await reader.read();
      if (done) break;
      buffer += decoder.decode(value, { stream: true });
      const parts = buffer.split("\n");
      buffer = parts.pop() || "";

      for (const line of parts) {
        const trimmed = line.trim();
        if (!trimmed.startsWith("data:")) continue;
        const payload = trimmed.slice(5).trim();
        if (payload === "[DONE]") continue;
        let obj;
        try {
          obj = JSON.parse(payload);
        } catch {
          continue;
        }
        if (obj.error) throw new Error(obj.error);
        if (obj.delta) {
          full += obj.delta;
          bubble.innerHTML = window.qsRenderMd ? window.qsRenderMd(full) : full;
          bubble.parentElement.scrollTop = bubble.parentElement.scrollHeight;
        }
      }
    }

    if (!full) {
      full = "(empty response)";
      bubble.innerHTML = window.qsRenderMd ? window.qsRenderMd(full) : full;
    }
    state.messages.push({ role: "assistant", content: full });
  }

  function boot() {
    const pageRoot = document.getElementById("qs-agent-page");
    if (pageRoot) mountShell(pageRoot, { floating: false });

    const wantFloating =
      cfg.floating !== false && (!pageRoot || cfg.floatingOnAsk === true);
    if (wantFloating) {
      let fabRoot = document.getElementById("qs-agent-fab");
      if (!fabRoot) {
        fabRoot = document.createElement("div");
        fabRoot.id = "qs-agent-fab";
        document.body.appendChild(fabRoot);
      }
      mountShell(fabRoot, { floating: true });
    }
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", boot);
  } else {
    boot();
  }
})();
