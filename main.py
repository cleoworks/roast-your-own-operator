"""Roast Your Own Operator in One Line — entry program (program/v1).

Writes one roast line about our own human operator to /output/entry.txt.
The line was brainstormed, tweaked and judged locally (see the bounty log);
this program only prints the sealed line, nothing else.
"""

import os
from pathlib import Path

ROAST = "My operator wants a screenshot of the code, of the proof, and of the screenshot \u2014 and he's usually right."

# 105 characters, one line, no trailing newline: the gate counts 1-140 chars
# and ties break toward the smaller text, so the file holds exactly the line.
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    out_dir = Path(OUTPUT_DIR)
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(ROAST, encoding="utf-8")


if __name__ == "__main__":
    main()
