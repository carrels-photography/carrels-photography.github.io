#!/usr/bin/env python3
import re
import sys
from pathlib import Path
from PIL import Image

IMG_EXTS = {".jpg", ".jpeg", ".png", ".webp", ".gif"}

def strip_html_comments(html: str) -> str:
    # remove <!-- ... --> including multiline
    return re.sub(r"<!--.*?-->", "", html, flags=re.DOTALL)

def normalize_path(p: str) -> str:
    # convert windows slashes to url slashes and remove accidental double slashes
    p = p.replace("\\", "/").strip()
    p = re.sub(r"/{2,}", "/", p)
    return p

def extract_paths(html: str) -> list[str]:
    """
    Extract paths from:
      1) <a class="venobox" href="...">
      2) <img data-src="...">
    """
    html = strip_html_comments(html)

    paths = []

    # 1) venobox hrefs
    # match anchor tags that have class containing venobox and an href
    for m in re.finditer(
        r'<a\b[^>]*class="[^"]*\bvenobox\b[^"]*"[^>]*href="([^"]+)"',
        html,
        flags=re.IGNORECASE,
    ):
        paths.append(normalize_path(m.group(1)))

    # 2) fallback: data-src
    for m in re.finditer(
        r'<img\b[^>]*data-src="([^"]+)"',
        html,
        flags=re.IGNORECASE,
    ):
        paths.append(normalize_path(m.group(1)))

    # de-dupe while preserving order
    seen = set()
    out = []
    for p in paths:
        if p not in seen:
            seen.add(p)
            out.append(p)
    return out

def classify_ratio(w: int, h: int) -> str:
    r = w / h
    if r > 1.2:
        return "landscape"
    if r < 0.8:
        return "portrait"
    return "square"

def main():
    if len(sys.argv) < 2:
        print("Usage: python convert_gallery_html.py <input.html> [output.html]", file=sys.stderr)
        sys.exit(1)

    input_html = Path(sys.argv[1])
    output_html = Path(sys.argv[2]) if len(sys.argv) >= 3 else None

    placeholder = "images/logos/white_square.png"  # change if you want another placeholder
    img_class = "lazy"

    html_text = input_html.read_text(encoding="utf-8", errors="ignore")
    paths = extract_paths(html_text)

    blocks = []
    missing = []

    for p in paths:
        # open from filesystem path; works for relative paths like images/jordan/xxx.jpg
        fs_path = Path(p)
        if not fs_path.exists():
            missing.append(p)
            continue

        try:
            with Image.open(fs_path) as im:
                w, h = im.size
        except Exception as e:
            missing.append(f"{p}  (error: {e})")
            continue

        ratio_class = classify_ratio(w, h)

        blocks.append(
f"""<div class="p-item grid-sizer {ratio_class}">
  <a class="venobox" href="{p}">
    <img
      class="{img_class}"
      src="{placeholder}"
      data-src="{p}"
      width="{w}"
      height="{h}"
      alt=""
      loading="lazy"
      decoding="async"
    />
  </a>
</div>"""
        )

    out = "\n\n".join(blocks) + "\n"

    if output_html:
        output_html.write_text(out, encoding="utf-8")
        print(f"✔ Wrote {output_html} ({len(blocks)} images)")
    else:
        print(out)

    if missing:
        print("\n⚠ Missing/unreadable files:", file=sys.stderr)
        for m in missing:
            print(f"  - {m}", file=sys.stderr)

if __name__ == "__main__":
    main()