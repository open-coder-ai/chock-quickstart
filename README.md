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
| `.agents/policies/` | Where policies will live — empty except the generated `INDEX.md` |
| `.chock/` | Engine state: `config.yaml` (yours to edit), `chock.lock`, vendored gate runtime in `bin/`, compiled output in `compiled/` |
| `.claude/`, `.cursor/`, `.gemini/`, … | Thin per-agent wrappers, all delegating to `AGENTS.md` — agent-agnostic by construction |
| `.git/hooks/` (not visible here) | Pre-commit/pre-push dispatchers, installed by `init` |

Next steps from here:

```bash
chock add protect-main-branch   # install a guardrail from the catalog
chock status                    # see what's installed and what it enforces
chock check                     # is this repo sound?
```

For the version of this repo *with* policies installed — one per artifact layer — see
[chock-example](https://github.com/open-coder-ai/chock-example).
