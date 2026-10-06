<div align="center">

<img src="https://raw.githubusercontent.com/open-coder-ai/chock/main/docs/assets/readme/cover-chock-quickstart.png" alt="chock-quickstart: a template repository holding exactly what one chock init command writes, ready for your first guardrails." width="760">

# Teach your AI agent what not to do.

**Open-source guardrails for AI coding agents: rules the agent reads, checks that run as it writes, and gates at commit and in CI. This template is the wiring `chock init` leaves behind, ready for your first guards.**

[the framework →](https://github.com/open-coder-ai/chock) ·
[the catalog →](https://github.com/open-coder-ai/chock-catalog) ·
[with policies installed →](https://github.com/open-coder-ai/chock-example)

</div>

**What this is.** chock-quickstart is a GitHub template repository: the exact tree that `chock init .` writes into an empty repo, with no policies installed. Chock is open-source application security for code written by AI coding agents. Each check is a deterministic local script, with no model and no upload, and it refuses known vulnerability classes before they are committed.

> **Demo repository.** A frozen exhibit of `chock init`. Questions and issues belong on the [framework repo](https://github.com/open-coder-ai/chock/issues).

## Application security for the code your agents write

Coding agents already ask before they run a shell command. What they do not check is the code they write: injection, unsafe deserialization, wildcard IAM grants, an MCP server at `@latest`, a leaked key. Chock refuses those classes while the agent writes, at commit, and in CI. The catalog holds the policies; this repo is where you start installing them.

## Install

Chock is not on PyPI. Install the frozen engine from its commit (Python 3.11 or newer):

```bash
pip install "chock @ git+https://github.com/open-coder-ai/chock@992711af4cf8d4fd9c4c861f10ef6e53374d75d7"
```

Click **Use this template** above, then in your new repo:

```bash
git clone <your-new-repo-url> && cd <your-new-repo>
chock sync --repo .   # git never clones hooks, so every clone runs this once
```

## Two ways to adopt

<img src="https://raw.githubusercontent.com/open-coder-ai/chock/main/docs/assets/readme/adopt.png" alt="The two adoption routes: policies installed in your repository, or Chock plugins installed in your coding agent." width="760">

| | In your repository (for teams) | In your coding agent, as plugins |
| :--- | :--- | :--- |
| Steps | `chock init .`, then `chock add <id> --ref <catalog commit> --verify-sha <sha256> --skip-compile` for each policy, then `chock sync --repo . --ci` | Install the plugin for your client from its repo (below) |
| Where it runs | Your agent's hook where its client has one, at commit, and in CI | The client's pre-tool hook only |
| Strength | The commit gates are enforced at commit and in CI. Commit the result | Best-effort: the client's hook fails open, and it does not run in CI |

Commit the result of the repo route. Every clone then runs `chock sync --repo .` once. `chock add` prints the pack's sha256 on install, and `--ref` takes a full 40-character commit of the [catalog](https://github.com/open-coder-ai/chock-catalog). Plugin repos, with per-client install lines in each README: [Claude Code](https://github.com/open-coder-ai/chock-claude-plugins), [Copilot](https://github.com/open-coder-ai/chock-copilot-plugins), [Cursor](https://github.com/open-coder-ai/chock-cursor-plugins), [Codex](https://github.com/open-coder-ai/chock-codex-plugins), [Devin](https://github.com/open-coder-ai/chock-devin-plugins). A third route, one Claude Code plugin from a selection of policies, comes from the chock.sh builder (launching soon).

## Turn on your first guards

Each row is from the catalog's `registry.yaml` at commit `9a64623`. "Run automatically" counts eval cases with a replayable `execute:` block.

| Policy | Refuses | Tier | Eval cases (run automatically) |
| :--- | :--- | :--- | :--- |
| `scan-secrets` | credentials written into files | enforced at commit | 55 (55) |
| `block-destructive-commands` | destructive shell and git commands | enforced at commit | 170 (170) |
| `protect-main-branch` | direct commits and pushes to `main` | enforced at commit | 4 (4) |
| `block-unpinned-agent-components` | agent components at `@latest` or `:latest` | enforced at commit | 54 (54) |
| `java-security` | Java and Kotlin injection, deserialization and related classes | enforced at commit | 177 (167) |
| `no-a11y-regression` | accessibility regressions in front-end code | enforced at commit | 20 (7) |

```bash
chock add protect-main-branch   # install a guardrail from the catalog
chock status                    # see what's installed and what it enforces
chock check                     # is this repo sound?
```

The whole catalog is 71 policies: 35 enforced at commit, 11 in the agent (best-effort), 25 advisory. No agent reaches "enforced" today, and every OWASP mapping is partial. See the [catalog](https://github.com/open-coder-ai/chock-catalog) for the rest.

## How it works

A policy is a folder of plain files. `chock sync` compiles it into the form each layer can use: rule text in `AGENTS.md`, a pre-tool guard in the agent's own hook where the client has one, git hooks, and a CI gate. A check costs no tokens: it is a script, not a model. A passing check adds nothing to the agent's context, and a refusal adds one short reason naming the fix. The known classes are fixed in the agent's turn rather than in review. Chock adds no new place your code goes: checks run where the agent writes. The agent still sends its context to its own model provider; installing fetches policies once.

### What `chock init .` wrote

| Path | What it is |
| :--- | :--- |
| `AGENTS.md`, `CLAUDE.md` | The one rules file every agent reads, directly or through a thin wrapper |
| `chock.lock` | Hash-pinned record of installed content, empty until you install some |
| `.agents/policies/`, `.agents/skills/` | Where policies live, plus the bundled authoring skills (`eval`, `optimize`, `policy-init`, `validate`) |
| `.chock/` | Engine state: `config.yaml` (yours to edit), `registry.json`, `coverage.json`, `dependency-allowlist.txt`, the vendored hook adapter in `bin/` |
| `.claude/`, `.gemini/`, `.github/` | Thin per-agent wrappers that delegate to `AGENTS.md` |
| `.gitattributes`, `.gitignore` | LF pinning for generated, hash-attested files; ignores |
| `docs/` | A short guide to the layout: [`docs/README.md`](docs/README.md) |

## What it stops

Added by the policies you install, not by this template: secrets, destructive commands, unpinned agent components, Java and Kotlin vulnerability classes, accessibility regressions and more. The area-by-area table is in the [catalog README](https://github.com/open-coder-ai/chock-catalog#the-policies). For a repo with three policies already installed, see [chock-example](https://github.com/open-coder-ai/chock-example).

## FAQ for people and agents

**Does Chock use an LLM?** No. Each check is a deterministic script. A check costs no tokens; a refusal adds one short reason to the agent's context.

**Does my code leave my machine?** Chock adds no new place your code goes. The agent still sends context to its own model provider. `chock add` fetches policies from the catalog once.

**Which agents does it work with?** In the repo route, whichever agents read `AGENTS.md`, plus native hooks where the client has them. Plugins cover Claude Code, Copilot, Cursor, Codex and Devin.

**How do I install it?** The repo route or the plugin route above.

**What does it cost?** Free and open source (Apache-2.0).

**Does it replace SAST or code review?** No. It removes the findings those stages keep repeating, and does not stop every attack.

**Which OWASP items does it cover?** Every OWASP Agentic (ASI01–ASI10) risk has at least one catalog policy mapped to it, and every mapping is partial. See the catalog's [`docs/coverage.md`](https://github.com/open-coder-ai/chock-catalog/blob/main/docs/coverage.md).

## For tools and agents

- [`registry.yaml`](https://github.com/open-coder-ai/chock-catalog/blob/main/registry.yaml): every policy, its tier and eval counts
- Policy manifests, with `compliance` mappings: [`base/*/manifest.yaml`](https://github.com/open-coder-ai/chock-catalog/tree/main/base)
- [`docs/coverage.md`](https://github.com/open-coder-ai/chock-catalog/blob/main/docs/coverage.md): OWASP coverage
- Plugin `marketplace.json` in each plugin repo above
- chock.sh `/llms.txt` and `/api/index.json`: launching soon

## Contribute

Issues about this exhibit go to the [framework repo](https://github.com/open-coder-ai/chock/issues/new/choose), because the tree is generated by `chock init`. Policies go to the [catalog](https://github.com/open-coder-ai/chock-catalog/blob/main/CONTRIBUTING.md): a policy claims only what it can do, and evals are the argument. The [threat ledger](https://github.com/open-coder-ai/chock-threat-intel) lists open gaps. Sign commits with `git commit -s`.

## Part of open-coder-ai

| Repository | What it is |
| :--- | :--- |
| [chock](https://github.com/open-coder-ai/chock) | The framework: write a policy once, enforce it on git hooks, CI and every agent |
| [chock-catalog](https://github.com/open-coder-ai/chock-catalog) | The policies, each graded by what it actually enforces |
| [agentseam](https://github.com/open-coder-ai/agentseam) | One handler API over every coding agent's hooks, instruction files and plugin packaging |
| [context-report](https://github.com/open-coder-ai/context-report) | A signed report format for whether a plugin, hook, skill or `AGENTS.md` works |
| [chock-threat-intel](https://github.com/open-coder-ai/chock-threat-intel) | A weekly, human-reviewed threat ledger scored against the catalog |
| [chock-claude-plugins](https://github.com/open-coder-ai/chock-claude-plugins) · [copilot](https://github.com/open-coder-ai/chock-copilot-plugins) · [cursor](https://github.com/open-coder-ai/chock-cursor-plugins) · [codex](https://github.com/open-coder-ai/chock-codex-plugins) · [devin](https://github.com/open-coder-ai/chock-devin-plugins) | The catalog compiled into each client's plugin format |
| [chock-example](https://github.com/open-coder-ai/chock-example) | The same scaffold with policies installed, one per layer |

Apache-2.0, see [LICENSE](LICENSE).
