"""ai-joke-03 v2 entry: writes one joke about AI coding agents."""

import os

# Three beats, one punchline: the agent redefines the bug as a feature,
# then proves it with a passing test.
JOKE = (
    "I asked my agent to add a test for the bug. "
    "It wrote one asserting the bug is a feature. "
    "The bug now has 100% coverage."
)

# The gate counts Unicode code points: 1-280, not only whitespace.
assert 1 <= len(JOKE) <= 280, "joke must be 1-280 characters"
assert JOKE.strip(), "joke must not be only whitespace"

OUT = "/output/entry.txt"
os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, "w", encoding="utf-8") as handle:
    handle.write(JOKE + "\n")

# Read-back: the bytes on disk must be exactly the joke plus a newline.
with open(OUT, encoding="utf-8") as handle:
    assert handle.read() == JOKE + "\n"
