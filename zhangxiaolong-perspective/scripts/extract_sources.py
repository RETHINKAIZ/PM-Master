#!/usr/bin/env python3
from __future__ import annotations

import html
import re
import sys
import zipfile
from html.parser import HTMLParser
from pathlib import Path

from pypdf import PdfReader


class TextHTMLParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.parts: list[str] = []
        self.skip_depth = 0

    def handle_starttag(self, tag: str, attrs) -> None:
        if tag in {"script", "style", "nav"}:
            self.skip_depth += 1
        if tag in {"p", "div", "section", "article", "h1", "h2", "h3", "li", "br"}:
            self.parts.append("\n")

    def handle_endtag(self, tag: str) -> None:
        if tag in {"script", "style", "nav"} and self.skip_depth:
            self.skip_depth -= 1
        if tag in {"p", "div", "section", "article", "h1", "h2", "h3", "li"}:
            self.parts.append("\n")

    def handle_data(self, data: str) -> None:
        if not self.skip_depth:
            text = html.unescape(data).strip()
            if text:
                self.parts.append(text)

    def text(self) -> str:
        raw = " ".join(self.parts)
        raw = re.sub(r"[ \t\r\f\v]+", " ", raw)
        raw = re.sub(r"\n\s+", "\n", raw)
        raw = re.sub(r"\n{3,}", "\n\n", raw)
        return raw.strip()


def extract_epub(path: Path) -> str:
    chunks: list[str] = []
    with zipfile.ZipFile(path) as zf:
        names = [
            name
            for name in zf.namelist()
            if name.lower().endswith((".html", ".xhtml", ".htm"))
        ]
        for name in sorted(names):
            data = zf.read(name)
            parser = TextHTMLParser()
            parser.feed(data.decode("utf-8", errors="ignore"))
            text = parser.text()
            if text:
                chunks.append(f"\n\n# SOURCE: {name}\n\n{text}")
    return "\n".join(chunks).strip()


def extract_pdf(path: Path) -> str:
    reader = PdfReader(str(path))
    chunks: list[str] = []
    for idx, page in enumerate(reader.pages, start=1):
        text = page.extract_text() or ""
        text = re.sub(r"[ \t\r\f\v]+", " ", text)
        text = re.sub(r"\n{3,}", "\n\n", text)
        if text.strip():
            chunks.append(f"\n\n# PAGE {idx}\n\n{text.strip()}")
    return "\n".join(chunks).strip()


def main() -> int:
    if len(sys.argv) < 3:
        print("usage: extract_sources.py OUT_DIR FILE...", file=sys.stderr)
        return 2
    out_dir = Path(sys.argv[1])
    out_dir.mkdir(parents=True, exist_ok=True)

    for raw in sys.argv[2:]:
        path = Path(raw)
        suffix = path.suffix.lower()
        if suffix == ".epub":
            text = extract_epub(path)
        elif suffix == ".pdf":
            text = extract_pdf(path)
        else:
            print(f"skip unsupported file: {path}", file=sys.stderr)
            continue

        out_path = out_dir / f"{path.stem}.txt"
        out_path.write_text(text, encoding="utf-8")
        print(f"{out_path}\t{len(text)} chars")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
