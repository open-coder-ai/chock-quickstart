<div align="center">

<img src=".github/logo.svg" alt="chock-quickstart: exactly what one chock init command leaves behind in an empty repository — the wiring, with no policies installed. The mark is chock's: a wheel held by a chock wedge." width="90">

# chock-quickstart

[![Demo repository](https://img.shields.io/badge/demo-repository-lightgrey)](https://github.com/open-coder-ai/chock)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)
[![Issues and PRs](https://img.shields.io/badge/issues%20%26%20PRs-chock-8957e5)](https://github.com/open-coder-ai/chock/issues)

**Exactly what one [Chock](https://github.com/open-coder-ai/chock) command leaves behind in an empty repository.**

[the framework →](https://github.com/open-coder-ai/chock) ·
[the full catalog →](https://github.com/open-coder-ai/chock-catalog) ·
[with policies installed →](https://github.com/open-coder-ai/chock-example)

</div>

> **Demo repository.** A frozen exhibit of `chock init`, nothing more. Questions and issues
> belong on the [framework repo](https://github.com/open-coder-ai/chock/issues).
> Click **Use this template** to start your own.

This whole file tree is the output of:

```bash
pip install chock
chock init .
```

**No policies are installed.** `init` is deliberately wiring-only — the framework ships
mechanism; policies are content you choose. What you're looking at:

| What you see | What it is |
| :--- | :--- |
| `AGENTS.md` | The one rules file every agent reads (directly, or via its wrapper) |
| `chock.lock` | Hash-pinned record of installed content — empty until you install some |
| `.gitattributes` | LF pinning for generated and hash-attested files, so packs check out byte-identical on every platform |
| `.agents/policies/` | Where policies will live — just the generated `INDEX.md` plus a guardrail `AGENTS.md`/`CLAUDE.md` pair stating the provenance-and-editing contract |
| `.agents/skills/` | The bundled authoring skills (`eval`, `optimize`, `policy-init`, `validate`) an agent uses to write and test policies, plus the same guardrail pair |
| `.chock/` | Engine state: `config.yaml` (yours to edit), `registry.json`, `coverage.json`, `dependency-allowlist.txt`, and `bin/sessionstart.py` — the vendored arm-on-clone adapter (git never clones hooks; this re-installs them when a Claude Code session opens). The gate runtime and compiled output appear once a policy is installed |
| `.claude/`, `.gemini/`, `.github/` | Thin per-agent wrappers delegating to `AGENTS.md` — plus `.claude/skills/`, a generated bridge of `.agents/skills/` for Claude Code's native discovery (each copy carries a `.chock-bridge` ownership marker), and `.claude/settings.json` wiring the SessionStart arm hook |
| `docs/` | A short adopter-facing guide to the layout |
| `.git/hooks/` (not visible here) | Pre-commit, pre-merge-commit and pre-push dispatchers, installed by `init` |

Next steps from here:

```bash
chock add protect-main-branch   # install a guardrail from the catalog
chock status                    # see what's installed and what it enforces
chock check                     # is this repo sound?
```

For the version of this repo *with* policies installed — one per artifact layer — see
[chock-example](https://github.com/open-coder-ai/chock-example).

## Where to go from here

- **Adopt it in your own repository.** `pip install chock && chock init .`, then `chock add`
  the policies that match how your team gets hurt; the
  [catalog](https://github.com/open-coder-ai/chock-catalog) labels each one with what it actually enforces.
- **Contribute a policy.** The [catalog's contributing guide](https://github.com/open-coder-ai/chock-catalog/blob/main/CONTRIBUTING.md) is short
  and its rules are mechanical: a policy claims only what it can do, and evals are the
  argument. The `policy wanted` entries in the [threat ledger](https://github.com/open-coder-ai/chock-threat-intel/blob/main/reference/agentic-threat-ledger.md) are the
  open work list.
- **Found something wrong in this exhibit?** This tree is a frozen exhibit of `chock init`, so the fix belongs in the framework. Issues go to the
  [framework repo](https://github.com/open-coder-ai/chock/issues/new/choose).

## Part of the open-coder-ai family

Everything under [open-coder-ai](https://github.com/open-coder-ai) is built on one rule: a claim must match a
mechanism. Where this repository sits among the others:

| Repository | What it is |
| :--- | :--- |
| [chock](https://github.com/open-coder-ai/chock) | The framework: write a policy once, enforce it on git hooks, CI, and every agent |
| [chock-catalog](https://github.com/open-coder-ai/chock-catalog) | The policies, each graded by what it actually enforces |
| [agentseam](https://github.com/open-coder-ai/agentseam) | The primitives layer under chock: one handler API over every agent's hooks, with a capability matrix that carries its provenance |
| [context-report](https://github.com/open-coder-ai/context-report) | A signed report format for whether a plugin, hook, skill or `AGENTS.md` actually works |
| [chock-threat-intel](https://github.com/open-coder-ai/chock-threat-intel) | A weekly, human-reviewed threat digest scored against the catalog |
| [chock-claude-plugins](https://github.com/open-coder-ai/chock-claude-plugins) · [copilot](https://github.com/open-coder-ai/chock-copilot-plugins) · [cursor](https://github.com/open-coder-ai/chock-cursor-plugins) · [codex](https://github.com/open-coder-ai/chock-codex-plugins) | The catalog compiled into each client's native plugin format; generated only, rebuilt and diffed in CI |
| [chock-example](https://github.com/open-coder-ai/chock-example) | The same scaffold with policies installed, one per artifact layer |
