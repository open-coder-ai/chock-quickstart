#!/usr/bin/env python3
"""Derive the README's policy-count sentence from chock-catalog's registry.yaml.

    python3 tools/policy_count.py            rewrite the sentence between the markers
    python3 tools/policy_count.py --check    exit 1 if the README sentence differs
    --registry FILE                          read a local registry.yaml instead of the pin
    --commit SHA                             40-hex catalog commit (default: CATALOG_COMMIT)

Counting rule (the same as chock's docs/assets/readme/derive.py):
  - a policy whose status is "deprecated" is not counted, in the total or in any tier;
  - the tier is the first word of the entry's `enforces`:
    enforced-at-commit -> commit, best-effort -> in the agent, advisory -> advisory.
Needs PyYAML (CI pins it).
"""
import argparse
import re
import sys
import urllib.request
from collections import Counter
from pathlib import Path

# The one place the catalog pin lives: a full 40-hex commit of open-coder-ai/chock-catalog.
CATALOG_COMMIT = "c2925a1500dfdd7042b07c37f877af2607f91959"

REPO = "open-coder-ai/chock-catalog"
README = Path(__file__).resolve().parent.parent / "README.md"
START, END = "<!-- policy-count:start -->", "<!-- policy-count:end -->"
TIERS = {"enforced-at-commit": "commit", "best-effort": "in-agent", "advisory": "advisory"}


def load_registry(commit: str, path: str | None) -> str:
    if path:
        return Path(path).read_text(encoding="utf-8")
    url = f"https://raw.githubusercontent.com/{REPO}/{commit}/registry.yaml"
    with urllib.request.urlopen(url, timeout=60) as r:  # noqa: S310 -- fixed https host, immutable commit URL
        return r.read().decode("utf-8")


def sentence(registry_text: str, commit: str) -> str:
    import yaml  # noqa: PLC0415

    listed = yaml.safe_load(registry_text)["policies"]
    live = [p for p in listed if p["status"] != "deprecated"]
    tiers = Counter(TIERS[p["enforces"].split(" ")[0]] for p in live)
    return (
        f"The whole catalog is {len(live)} policies: {tiers['commit']} enforced at commit, "
        f"{tiers['in-agent']} in the agent (best-effort), {tiers['advisory']} advisory "
        f"(`registry.yaml` in [chock-catalog](https://github.com/{REPO}) at `{commit[:7]}`)."
    )


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--registry")
    ap.add_argument("--commit", default=CATALOG_COMMIT)
    a = ap.parse_args()
    if not re.fullmatch(r"[0-9a-f]{40}", a.commit):
        print("--commit must be a full 40-hex commit", file=sys.stderr)
        return 2
    text = README.read_text(encoding="utf-8")
    if text.count(START) != 1 or text.count(END) != 1 or text.index(START) > text.index(END):
        print(f"README.md must hold exactly one {START} ... {END} pair", file=sys.stderr)
        return 2
    want = sentence(load_registry(a.commit, a.registry), a.commit)
    head, rest = text.split(START)
    have, tail = rest.split(END)
    if have == want:
        print(f"ok: {want}")
        return 0
    if a.check:
        print(f"README.md policy count is stale.\n  have: {have}\n  want: {want}\n"
              "Run: python3 tools/policy_count.py", file=sys.stderr)
        return 1
    README.write_text(head + START + want + END + tail, encoding="utf-8")
    print(f"updated: {want}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
