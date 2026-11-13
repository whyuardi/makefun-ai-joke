import os

JOKE = "My AI agent fixed my bug by deleting the feature, the tests, and my will to live. The build passes."

# The gate requires 1-280 UTF-8 characters, not only whitespace.
assert 1 <= len(JOKE) <= 280 and JOKE.strip(), "joke violates the gate"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(JOKE + "\n")
