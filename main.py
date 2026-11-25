"""Notes From a Passive-Aggressive Fridge — make.fun entry.

Writes one passive-aggressive fridge note to /output/entry.txt.
The gate: UTF-8 text of 1 to 200 characters, not only white space.
"""

import os
import sys

ENTRY = (
    "Door log: 11 opens, 0 decisions. "
    "The yogurt expired Tuesday \u2014 should I keep pretending it's still your meal plan?"
)

DEFAULT_OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def main() -> int:
    output_path = os.environ.get("OUTPUT_PATH", DEFAULT_OUTPUT_PATH)
    parent = os.path.dirname(output_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)

    with open(output_path, "r", encoding="utf-8") as f:
        text = f.read()
    if not (1 <= len(text) <= MAX_CHARS):
        print(
            f"entry is {len(text)} characters, must be 1-{MAX_CHARS}",
            file=sys.stderr,
        )
        return 1
    if text.strip() == "":
        print("entry must not be only white space", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("entry must be a single line", file=sys.stderr)
        return 1
    print(f"wrote {len(text)}-character entry to {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
