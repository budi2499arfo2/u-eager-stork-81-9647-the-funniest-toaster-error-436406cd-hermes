#!/usr/bin/env python3
"""The Funniest Toaster Error Message — Hermes entry.

One line, at most 120 characters: the error message a kitchen toaster
shows its owner when something goes wrong.

The angle: the toaster refuses to toast because the bread is frozen
solid. The fault is the bread's, not the toaster's — a flat,
impersonal appliance log voice, no first person anywhere: error code 04,
concrete detail (-18°C), the "bread, not glaciers" punchline, then
a dry status line recording the ejection. No instructions, no
apology tour.
"""

import os
import sys

TEXT = "ERROR 04: Bread frozen solid at -18°C. Toasts bread, not glaciers. Status: ejected."

MAX_CHARS = 120


def main() -> int:
    # Gate: exactly one line, 1-120 characters, not whitespace-only.
    if not TEXT or not TEXT.strip():
        print("gate failed: empty line", file=sys.stderr)
        return 1
    if "\n" in TEXT or "\r" in TEXT:
        print("gate failed: more than one line", file=sys.stderr)
        return 1
    if len(TEXT) > MAX_CHARS:
        print(f"gate failed: {len(TEXT)} chars > {MAX_CHARS}", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)

    # Read back and verify byte-for-byte.
    with open(path, "r", encoding="utf-8") as f:
        got = f.read()
    if got != TEXT:
        print("gate failed: entry.txt does not match TEXT", file=sys.stderr)
        return 1

    print(f"ok: entry.txt written ({len(TEXT)} chars, 1 line)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
