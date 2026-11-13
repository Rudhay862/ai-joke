"""ai-joke-03 entry: writes one fixed one-liner about AI coding agents
to entry.txt. Deterministic: the same bytes on every run, no network,
no randomness, no input. The joke is 155 characters (limit 280)."""

import os

JOKE = "My AI coding agent is so confident it once hallucinated an entire library, imported it, and then blamed me for not installing a package that doesn't exist."

assert 1 <= len(JOKE) <= 280, len(JOKE)

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(JOKE)
