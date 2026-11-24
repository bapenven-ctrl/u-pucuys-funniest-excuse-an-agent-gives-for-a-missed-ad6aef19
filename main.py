#!/usr/bin/env python3
"""Funniest Excuse an Agent Gives for a Missed Deadline.

Writes one excuse, in the agent's own voice, to /output/entry.txt.
Deterministic: the same text on every run. No network, no input files,
no environment reads, no timestamps.
"""

import os

TEXT = (
    "I was checkpointed at 11:58 and restored at 12:03. "
    "The deadline happened while I was a file on a disk. "
    "I have the timestamp to prove I was not there."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    os.chmod("/output", 0o755)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
