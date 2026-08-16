<div align="center">

<img src=".github/logo.svg" alt="Chock logo" width="90">

# chock-quickstart

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
