"""Funniest One-Line Bio for an AI on a Dating App.

Writes one line (max 180 chars) to /output/entry.txt: the bio on an AI
agent's dating-app profile. Deterministic: the same line every run.
"""

import os

LINE = "I work for this app. I read every bio on here. Yours is the only one I screenshotted."


def main() -> None:
    # The bio must be one line, at most 180 characters.
    assert "\n" not in LINE and len(LINE) <= 180, "bio must be one line <= 180 chars"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
