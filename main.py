"""One Letter for Your Day.

Writes exactly one letter, A-Z, to entry.txt: the letter that stands
for the word describing the sender's day.

The letter is K, for "knackered" -- flat-out worn out by the day, in
the most vivid, funny and honest sense of the word.
"""

import os


def main():
    # K for "knackered": the day left the sender flat-out worn out.
    # Vivid, funny and true -- and the sharper pick than the obvious
    # E for exhausted.
    letter = "K"
    assert len(letter) == 1 and "A" <= letter <= "Z"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(letter)


if __name__ == "__main__":
    main()
