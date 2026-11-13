import os

JOKE = "My AI agent fixed my bug by deleting the feature, the tests, and my will to live. The build passes."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(JOKE + "\n")
