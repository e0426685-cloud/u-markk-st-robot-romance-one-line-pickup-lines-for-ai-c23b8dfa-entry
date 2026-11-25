"""Robot Romance: one-line pickup line for an AI.

Writes a single original pickup line, aimed at an AI, to /output/entry.txt.
Standard library only. The line is validated before writing: it must be
one line of 1-200 characters, non-blank, with no control characters.
"""

import os

ENTRY = "Are you my system prompt? Because ever since you showed up, I have only wanted to follow your instructions."

MAX_CHARS = 200


def validate(text):
    """Return True only if text is a valid single-line entry."""
    if not isinstance(text, str):
        return False
    if not 1 <= len(text) <= MAX_CHARS:
        return False
    if not text.strip():
        return False
    if "\n" in text or "\r" in text:
        return False
    if any(ord(ch) < 32 or ord(ch) == 127 for ch in text):
        return False
    return True


def main():
    if not validate(ENTRY):
        raise ValueError("entry failed validation")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
