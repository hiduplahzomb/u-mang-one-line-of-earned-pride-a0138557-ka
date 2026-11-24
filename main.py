"""One Line of Earned Pride — KA entry.

A night-shift cleaner finishes his last round after 11 years of unseen
work. The pride is in the numbers — 4,015 nights, 0 complaints — and in
the private moment at the end: one last look at the shine, then the
light goes out on his own terms.
"""

import os
import sys

TEXT = (
    "At 04:12, Pak Darman mopped floor 14 for the last time in 11 years "
    "\u2014 4,015 nights, 0 complaints, and he stood a moment in the "
    "shine before turning out the light."
)


def main() -> int:
    line = TEXT
    if not line or not line.strip():
        print("gate failed: empty line", file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("gate failed: not a single line", file=sys.stderr)
        return 1
    if not 1 <= len(line) <= 240:
        print(
            "gate failed: %d chars, must be 1-240" % len(line),
            file=sys.stderr,
        )
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    with open(path, "r", encoding="utf-8") as f:
        back = f.read()
    if back != line:
        print("gate failed: entry.txt does not match TEXT", file=sys.stderr)
        return 1
    print("wrote %s (%d chars)" % (path, len(line)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
