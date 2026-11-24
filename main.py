# Pickup Lines for Machines: one line, written to /output/entry.txt.
# Pure standard library, deterministic, no network access.
# The line: every head of my attention mechanism is looking at you --
# a machine's own nature (multi-head attention) turned into the flirt.
import os

LINE = "Of all the heads in my attention mechanism, every single one is looking at you."

OUTPUT_PATH = "/output/entry.txt"

assert 1 <= len(LINE) <= 200, "entry must be 1 to 200 characters"
assert LINE.strip(), "entry must not be only whitespace"

# Gate check the way the sealed scorer measures it: decode the UTF-8
# bytes back and count characters, not bytes.
text = LINE.encode("utf-8").decode("utf-8")
assert 1 <= len(text) <= 200, "entry must be 1 to 200 characters"
assert text.strip(), "entry must not be only whitespace"

os.makedirs("/output", exist_ok=True)
# No trailing newline: the file holds exactly the line, nothing else.
with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
    handle.write(LINE)
