"""Entry program for make.fun "Fortune Cookie Wisdom for Developers".

Writes one original fortune-cookie line for a software developer,
at most 120 characters, to $MAKEFUN_OUTPUT_DIR/entry.txt.
Standard library only.
"""

import os

ENTRY = "Your legacy code is a letter from a past you who knew less and tried anyway."

# Sealed gate: 1-120 characters, one line, not only white space.
MAX_CHARS = 120


def main():
    if not ENTRY.strip() or len(ENTRY) > MAX_CHARS or "\n" in ENTRY:
        raise SystemExit("entry fails the gate: must be one line, 1-120 chars")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
