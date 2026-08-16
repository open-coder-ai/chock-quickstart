# 🛞 chock-quickstart

> **Demo repository.** This repo exists so you can *see* what [Chock](https://github.com/open-coder-ai/chock)
> adoption looks like — nothing more. Questions and issues belong on the
> [framework repo](https://github.com/open-coder-ai/chock/issues); this one is a frozen exhibit.
> Click **Use this template** to start your own.

This is exactly what one command leaves behind in an empty repository:

```bash
pip install chock
chock init .
```

**No policies are installed.** `init` is deliberately wiring-only — the framework ships
mechanism; policies are content you choose. That is the whole file tree you're looking at:

| What you see | What it is |
| :--- | :--- |
| `AGENTS.md` | The one rules file every agent reads (directly, or via its wrapper) |
| `chock.lock` | Hash-pinned record of installed content — empty until you install some |
| `.gitattributes` | LF pinning for generated and hash-attested files, so packs check out byte-identical on every platform |
| `.agents/policies/` | Where policies will live — just the generated `INDEX.md` plus a guardrail `AGENTS.md`/`CLAUDE.md` pair stating the provenance-and-editing contract |
| `.agents/skills/` | The bundled authoring skills (`eval`, `optimize`, `policy-init`, `validate`) an agent uses to write and test policies, plus the same guardrail pair |
| `.chock/` | Engine state: `config.yaml` (yours to edit), `registry.json`, `coverage.json`, `dependency-allowlist.txt` — the vendored gate runtime and compiled output appear once a policy is installed |
| `.claude/`, `.gemini/`, `.github/` | Thin per-agent wrappers delegating to `AGENTS.md` — plus `.claude/skills/`, a generated bridge of `.agents/skills/` for Claude Code's native discovery (each copy carries a `.chock-bridge` ownership marker) |
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
