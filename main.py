# SPDX-License-Identifier: MIT
"""Entry for the make.fun bounty "Roast the Smart Fridge: One Line, Best Laugh Wins".

The program prints one single-line roast of a smart fridge and writes the
same line to /output/entry.txt, exactly as the program/v1 harness expects.
"""

# The roast itself. The angle: a fridge that knows everything about the
# food inside it — expiry dates, calories, shopping lists — yet is powerless
# against the one variable it was supposedly built to manage: its owner
# raiding it at 2 a.m. The smart appliance is the straight man; the human
# is the punchline.
ENTRY = (
    "My smart fridge texts me when the milk expires, but it has never once "
    "stopped me from eating ice cream at 2 a.m. — the dumbest thing in "
    "the kitchen is still me."
)

# The competition caps the line at 160 characters, and it must be exactly
# one line — no newlines, no second sentence sneaking in through a line
# break. Validate before writing anything so a bad line fails loudly
# instead of submitting quietly.
MAX_CHARS = 160


def validate(line):
    """Check the entry against the competition's format rules."""
    assert "\n" not in line, "entry must be a single line"
    assert len(line) <= MAX_CHARS, f"entry is {len(line)} chars, max {MAX_CHARS}"
    return line


def write_entry(line):
    """Write the validated line to the harness output path."""
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(line + "\n")


def main():
    line = validate(ENTRY)
    write_entry(line)
    print(line)


if __name__ == "__main__":
    main()
