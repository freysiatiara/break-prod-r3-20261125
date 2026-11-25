# Break Production, Own It — round 3 entry (fresh mechanism: cached error page)
#
# The program writes exactly one line to /output/entry.txt: the one line
# an AI agent prints the moment it breaks production. Standard library only.

import os

ENTRY = "I cached the 500 error page for performance. It is now the fastest page we serve. It is also the only page we serve."

OUTPUT_PATH = "/output/entry.txt"


def main():
    # Guard: the gate requires UTF-8 text of 1 to 200 characters, a single
    # line, and not only whitespace. The text itself is never altered here.
    if not ENTRY or ENTRY.strip() == "":
        raise ValueError("entry is empty")
    if len(ENTRY) > 200:
        raise ValueError("entry exceeds 200 characters")
    if "\n" in ENTRY or "\r" in ENTRY:
        raise ValueError("entry must be a single line")
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
