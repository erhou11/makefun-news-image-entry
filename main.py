#!/usr/bin/env python3
"""Write the bundled news-summary image to /output/entry.png.

The entry image (entry.png, shipped next to this file) sums up the world
news of Thursday, 26 November 2026 in one graphic: 36 numbered items with
a source and a CONFIRMED/CLAIM credibility tag each, a world map whose
pins match the item numbers, a markets strip, and a timeline of the day.
Only items published on 26 November 2026 are counted. This program copies
the image to the output location the grader reads. Set OUTPUT_DIR to
override the output directory (used only for local testing).
"""

import os
import shutil
import sys

PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def is_png(path: str) -> bool:
    """Return True when the file starts with the PNG signature."""
    with open(path, "rb") as fh:
        return fh.read(len(PNG_MAGIC)) == PNG_MAGIC


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    if not is_png(src):
        print(f"error: {src} is not a valid PNG file", file=sys.stderr)
        return 1
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    print(f"wrote {dst} ({os.path.getsize(dst)} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
