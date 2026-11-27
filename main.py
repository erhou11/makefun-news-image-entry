#!/usr/bin/env python3
"""Write the bundled news-summary image to /output/entry.png.

The entry image (entry.png, shipped next to this file) sums up the world
news of 26 November 2026 in one graphic. This program copies it to the
output location the grader reads. Set OUTPUT_DIR to override the output
directory (used only for local testing).
"""

import os
import shutil
import sys


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    print(f"wrote {dst} ({os.path.getsize(dst)} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
