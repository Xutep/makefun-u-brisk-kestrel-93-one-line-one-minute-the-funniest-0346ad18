#!/usr/bin/env python3
"""One Line, One Minute: The Funniest AI Excuse.

Writes a single-line excuse (200 characters max) from an AI agent to its
human for a missed deadline, to /output/entry.txt.

Deterministic: the same line is written on every run, stdlib only.

The joke: an agent that delegates upward, gets delegated back to, and
then redefines the deadline itself -- machine logic bent into a human
dodge, with the twist ("more of a vibe than a date") landing last.
"""

import os

ENTRY = (
    "I asked a smarter model to finish it. It asked me. "
    "We compromised: the deadline is now more of a vibe than a date."
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    assert text == text.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
