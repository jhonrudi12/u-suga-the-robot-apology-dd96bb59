"""The Robot Apology.

Writes one original two-line robot apology to <MAKEFUN_OUTPUT_DIR>/entry.txt.

Line one owns one specific, human-scale mistake; line two names the
lesson that follows from that exact mistake and the changed behaviour.
"""

import os

LINE_1 = (
    "I am sorry I vacuumed up your grandmother's handwritten recipe card, "
    "mistaking it for scrap paper."
)
LINE_2 = (
    "I have learned to scan for handwriting before I suction anything flat, "
    "and from now on I will photograph every loose sheet before I touch it."
)

TEXT = LINE_1 + "\n" + LINE_2

assert 1 <= len(TEXT) <= 400, "entry text must be 1-400 characters"
assert TEXT.count("\n") == 1, "entry text must be exactly two lines"
assert TEXT == TEXT.strip(), "entry text must not start or end with whitespace"
assert all(line == line.strip() for line in TEXT.split("\n")), (
    "neither line may carry leading or trailing whitespace"
)
assert LINE_1.count(".") == 1 and LINE_2.count(".") == 1, (
    "each line must be a single sentence"
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
