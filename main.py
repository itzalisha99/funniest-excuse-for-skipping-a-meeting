#!/usr/bin/env python3
"""Funniest Excuse for Skipping a Meeting — make.fun entry.

Writes one razor-sharp line (<= 200 chars) that excuses the author from a
pointless work meeting, to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
Stdlib only — the grading sandbox is stock python:3.13-slim.
"""

import os

ENTRY = "I sent my calendar invite in my place. It's more qualified for this meeting than I am."


def output_path():
    """Resolve the output directory, honouring MAKEFUN_OUTPUT_DIR."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(out_dir, "entry.txt")


def validate(text):
    """Mirror the bounty gate: UTF-8, 1-200 chars, not whitespace-only, one line."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not (1 <= len(text) <= 200):
        raise ValueError(f"entry must be 1-200 chars, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be whitespace-only")
    if "\n" in text.strip():
        raise ValueError("entry must be a single line")
    text.encode("utf-8")  # raises if not valid UTF-8
    return True


def main():
    validate(ENTRY)
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    # Read back and verify the bytes are exactly what we intended.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != ENTRY + "\n":
        raise RuntimeError("output does not match the entry byte-for-byte")
    print(f"wrote {path} ({len(ENTRY)} chars, verified)")


if __name__ == "__main__":
    main()
