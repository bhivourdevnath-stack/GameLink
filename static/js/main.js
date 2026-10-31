// Directory search and filters reload through Flask query parameters.

document.querySelectorAll(".text-roll").forEach((element) => {
    const text = element.textContent.trim().replace(/\s+/g, " ");
    if (!text) return;

    element.setAttribute("aria-label", text);
    const originalMarkup = element.innerHTML;
    const hasExplicitLines = element.querySelectorAll("br").length > 0;
    element.textContent = "";

    const lines = hasExplicitLines
        ? originalMarkup.split(/<br\s*\/?>/i)
        : [text];

    lines.forEach((line, lineIndex) => {
        const lineElement = document.createElement("span");
        lineElement.className = "text-roll-line";
        const cleanLine = line.replace(/<[^>]*>/g, "").trim().replace(/\s+/g, " ");

        [...cleanLine].forEach((character, index) => {
        const roll = document.createElement("span");
        roll.className = "text-roll-word";
        roll.style.setProperty("--roll-index", index);
        roll.setAttribute("aria-hidden", "true");

        const original = document.createElement("span");
        original.textContent = character === " " ? "\u00a0" : character;
        const duplicate = original.cloneNode(true);

        roll.append(original, duplicate);
            lineElement.appendChild(roll);
        });

        element.appendChild(lineElement);
        if (lineIndex < lines.length - 1) {
            element.appendChild(document.createElement("br"));
        }
    });
});
