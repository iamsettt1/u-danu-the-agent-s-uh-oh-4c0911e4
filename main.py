#!/usr/bin/env python3
"""Write the agent's one-word confession to /output/entry.txt.

The word: "undefined" -- the literal value a machine produces when it has
no answer at all. It is what an agent blurts mid-task when it is completely
lost: not a human hesitation ("hmm", "uhh") but the machine's own confession
that the slot it was asked to fill holds nothing. Funny on its own, instantly
recognisable, and not the first obvious word anyone would type.
"""

import os

WORD = "undefined"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    # Write deterministically: same bytes on every run.
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(WORD + "\n")


if __name__ == "__main__":
    main()
