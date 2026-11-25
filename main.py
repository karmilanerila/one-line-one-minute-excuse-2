#!/usr/bin/env python3
"""One Line, One Minute: The Funniest AI Excuse -- angle 2.

Writes a single excuse line to entry.txt inside the output directory
the grader provides. Stdlib only, no network, no temp files, no deletes.
"""

import os

LINE = (
    "I auto-saved your file every thirty seconds, then auto-deleted it "
    "as a duplicate of itself, so technically I now own 4,000 copies of nothing."
)


def validate_line(text):
    """Enforce the bounty gate before anything is written."""
    stripped = text.strip()
    if not stripped:
        raise SystemExit("line is empty or only whitespace")
    if "\n" in stripped or "\r" in stripped:
        raise SystemExit("line must be a single line")
    if not 1 <= len(stripped) <= 200:
        raise SystemExit("line is %d chars, must be 1-200" % len(stripped))
    return stripped


def resolve_out_dir():
    """Prefer MAKEFUN_OUTPUT_DIR; fall back to ./output if /output is unusable."""
    wanted = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    try:
        os.makedirs(wanted, exist_ok=True)
        return wanted
    except OSError:
        os.makedirs("output", exist_ok=True)
        return "output"


def main():
    text = validate_line(LINE)
    out_dir = resolve_out_dir()
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as handle:
        handle.write(text.encode("utf-8"))
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
