#!/usr/bin/env python3
"""One Line, One Laugh — entry program.

Writes a single funny line (<=200 chars) to /output/entry.txt.
"""
import os

LINE = "My sourdough starter survived the move, the breakup, and a three-day blackout. It is now my emergency contact, and frankly the most reliable relationship I have."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
