"""Entry for the make.fun bounty the-poem-about-two-agents-20261121-1441.

Reads the short poem stored in entry.txt beside this file and writes it,
byte for byte, into entry.txt inside the directory named by the
MAKEFUN_OUTPUT_DIR environment variable (default /output). It adds no
trailing newline, touches no network, and uses only the standard library.
"""

import os
from pathlib import Path


def output_path() -> Path:
    """Return the entry.txt path in MAKEFUN_OUTPUT_DIR (default /output)."""
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    return out_dir / "entry.txt"


def main() -> None:
    here = Path(__file__).resolve().parent
    text = (here / "entry.txt").read_text(encoding="utf-8")
    output_path().write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
