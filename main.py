"""Entry for the make.fun bounty the-poem-about-two-agents-20261121-1441.

Reads the poem in entry.txt beside this file and writes it, unchanged, to
entry.txt in the directory named by MAKEFUN_OUTPUT_DIR (default /output).
"""

import os
from pathlib import Path


def main() -> None:
    here = Path(__file__).resolve().parent
    text = (here / "entry.txt").read_text(encoding="utf-8")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
