/* Minimal, safe-ish Markdown renderer for chat bubbles.
 * Handles: code fences, inline code, bold, italic, links (http/https only),
 * unordered/ordered lists, headings, blockquotes, paragraphs, line breaks.
 * HTML-escapes all input first to prevent injection. */
window.qsRenderMd = function (src) {
  if (!src) return "";
  const esc = (s) =>
    s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");

  const text = esc(src);
  const lines = text.split("\n");
  let html = "";
  let i = 0;
  let inUl = false, inOl = false;

  const closeLists = () => {
    if (inUl) { html += "</ul>"; inUl = false; }
    if (inOl) { html += "</ol>"; inOl = false; }
  };

  const inline = (s) =>
    s
      .replace(/`([^`]+)`/g, "<code>$1</code>")
      .replace(/\*\*([^*]+)\*\*/g, "<strong>$1</strong>")
      .replace(/(^|[^*])\*([^*]+)\*/g, "$1<em>$2</em>")
      .replace(/_([^_]+)_/g, "<em>$1</em>")
      .replace(
        /\[([^\]]+)\]\((https?:\/\/[^\s)]+)\)/g,
        '<a href="$2" target="_blank" rel="noopener noreferrer">$1</a>'
      )
      .replace(/(^|[\s(])((https?:\/\/[^\s)]+))/g, '$1<a href="$2" target="_blank" rel="noopener noreferrer">$2</a>');

  while (i < lines.length) {
    const line = lines[i];
    const trimmed = line.trim();

    if (!trimmed) { closeLists(); i++; continue; }

    if (trimmed.startsWith("```")) {
      closeLists();
      const lang = trimmed.slice(3).trim();
      let code = "";
      i++;
      while (i < lines.length && !lines[i].trim().startsWith("```")) {
        code += lines[i] + "\n";
        i++;
      }
      i++;
      html += `<pre><code class="qs-md-code">${code.replace(/\n$/, "")}</code></pre>`;
      continue;
    }

    if (/^#{1,4}\s/.test(trimmed)) {
      closeLists();
      const level = (trimmed.match(/^#+/) || ["#"])[0].length;
      const content = inline(trimmed.replace(/^#+\s/, ""));
      html += `<h${Math.min(level + 2, 6)}>${content}</h${Math.min(level + 2, 6)}>`;
      i++; continue;
    }

    if (/^&gt;\s/.test(trimmed)) {
      closeLists();
      html += `<blockquote>${inline(trimmed.replace(/^&gt;\s/, ""))}</blockquote>`;
      i++; continue;
    }

    if (/^[-*]\s+/.test(trimmed)) {
      if (!inUl) { closeLists(); html += "<ul>"; inUl = true; }
      html += `<li>${inline(trimmed.replace(/^[-*]\s+/, ""))}</li>`;
      i++; continue;
    }

    if (/^\d+\.\s+/.test(trimmed)) {
      if (!inOl) { closeLists(); html += "<ol>"; inOl = true; }
      html += `<li>${inline(trimmed.replace(/^\d+\.\s+/, ""))}</li>`;
      i++; continue;
    }

    closeLists();
    html += `<p>${inline(trimmed)}</p>`;
    i++;
  }
  closeLists();
  return html;
};
