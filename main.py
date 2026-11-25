"""Two Robots in an Elevator - make.fun entry.

Writes one funny line of awkward small talk a robot says to another
robot in an elevator, to /output/entry.txt (UTF-8, single line, <200 chars).

Python 3.13 standard library only. No network at run time.
"""

import os

ENTRY = "I counted your blinks. Two. Was that a greeting, or a firmware error?"

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main() -> None:
    text = ENTRY.strip()
    # Gate assertions: exactly one line, 1-200 characters, non-empty.
    assert text, "entry must not be empty"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    assert text.strip() == text, "entry must not be only whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    # Verify what was written round-trips through the gate.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == text + "\n", "written output differs from entry"
    assert 1 <= len(written.rstrip("\n")) <= 200, "written entry out of gate range"


if __name__ == "__main__":
    main()
