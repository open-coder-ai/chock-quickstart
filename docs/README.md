# Chock setup

This repo uses Chock for agent policy engineering. This folder contains human-readable documentation only. Agents must not read files here.

## Structure

- `.agents/skills/` — your business skills
- `.agents/policies/` — your rules, hooks, and policies
- `docs/` — human documentation
- `AGENTS.md` — agent-readable rules

## Next steps

1. Create your first policy using the `/policy-init` skill installed in your agent's skill directory.
2. Validate with `chock check`.

## What `chock init` wrote

Moved here from the root `README.md`, verbatim, so the landing page can stay to one screen.

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
