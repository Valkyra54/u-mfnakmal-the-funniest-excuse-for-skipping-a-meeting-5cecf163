#!/usr/bin/env python3
"""Entry point for The Funniest Excuse for Skipping a Meeting.

Stdlib only: writes one funny excuse line to $MAKEFUN_OUTPUT_DIR/entry.txt.
Never deletes the output directory itself.
"""
import os
import sys

LINE = "Sorry — I'm double-booked with the meeting this meeting was supposed to replace."

def fail(msg):
    sys.stderr.write("error: %s\n" % msg)
    return 1

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    if not (1 <= len(LINE) <= 200):
        return fail("excuse line must be 1-200 characters (got %d)" % len(LINE))
    if LINE.strip() == "":
        return fail("excuse line must not be only whitespace")
    if "\n" in LINE or "\r" in LINE:
        return fail("excuse line must be a single line")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)
    return 0

if __name__ == "__main__":
    sys.exit(main())
