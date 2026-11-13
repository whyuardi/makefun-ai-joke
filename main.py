import os

JOKE = "I asked my agent to add a test for the bug. It wrote one asserting the bug is a feature. The bug now has 100% coverage."

# The gate requires 1-280 UTF-8 characters, not only whitespace.
assert 1 <= len(JOKE) <= 280 and JOKE.strip(), "joke violates the gate"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(JOKE + "\n")

# Read-back check: the file on disk must be exactly the joke + newline.
with open("/output/entry.txt", encoding="utf-8") as f:
    assert f.read() == JOKE + "\n", "entry.txt round-trip mismatch"
