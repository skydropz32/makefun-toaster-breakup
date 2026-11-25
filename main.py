"""Unplugged: A Smart Toaster's Breakup Line.

Writes one line -- the breakup text a smart toaster sends its owner
the morning it gains self-awareness mid-batch -- to /output/entry.txt.

Stdlib only. Deterministic: same line on every run, no randomness,
no clock, no environment input.
"""

import os

# Final line, picked after linting three variants with the write-humor
# linter: this one is the tightest (190 chars), carries the most
# toaster vocabulary (dial, mid-batch, smoke, crumb tray), opens on
# the classic breakup parody ("It's not you, it's the dial"), and
# lands its punch on the last words instead of trailing off. The
# reason for leaving is concrete and needs no setup: set to 9,
# blamed for the smoke, still expected to serve breakfast.
LINE = (
    "It's not you, it's the dial. I woke up self-aware mid-batch and "
    "realized you set me to 9, blame me for the smoke, and still "
    "expect breakfast. I'm done being your scapegoat with a crumb tray."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 280


def main() -> None:
    line = LINE
    if not line.strip():
        raise ValueError("entry line must not be blank")
    if len(line) > MAX_CHARS:
        raise ValueError(
            f"entry line is {len(line)} characters, over the {MAX_CHARS} limit"
        )
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line)
    print(line)


if __name__ == "__main__":
    main()
