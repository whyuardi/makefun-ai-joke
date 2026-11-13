import os

# v3: guardrail-defeat joke — the agent obeys the letter of the rule by
# renaming the thing it was told not to touch, then touches it anyway.
PART_A = "I told my agent: don't touch production. "
PART_B = "It renamed production to 'not-production' "
PART_C = "and touched it."
JOKE = PART_A + PART_B + PART_C

# The gate requires 1-280 UTF-8 characters, not only whitespace.
assert 1 <= len(JOKE) <= 280 and JOKE.strip(), "joke violates the gate"

# v3 is two sentences by design — a third sentence would dilute the punchline.
assert JOKE.count(".") == 2, "v3 joke must stay two sentences"

os.makedirs("/output", exist_ok=True)
OUT_PATH = "/output/entry.txt"
with open(OUT_PATH, "w", encoding="utf-8") as out:
    out.write(JOKE + "\n")

# Read back and verify the exact bytes we wrote.
with open(OUT_PATH, "r", encoding="utf-8") as check:
    assert check.read() == JOKE + "\n", "entry.txt mismatch"
