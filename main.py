#!/usr/bin/env python3
"""Fix Human Sleep: Funniest Patch Note.

Writes a single-line changelog entry announcing that human sleep
has been fixed. Deterministic: no input, no network, no randomness,
no clock reads -- the same line every run.
"""

import os

PATCH_NOTE = (
    "Fixed: humans no longer lie awake until 3 AM replaying that "
    "embarrassing thing from 2014 \u2014 sleep now installs on the first try."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    note = PATCH_NOTE.strip()
    assert "\n" not in note, "patch note must be a single line"
    assert len(note) < 160, f"patch note is {len(note)} chars, must be < 160"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(note + "\n")
    print(note)


if __name__ == "__main__":
    main()
