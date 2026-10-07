<div align="center">

<p><img src="https://raw.githubusercontent.com/open-coder-ai/chock/main/docs/assets/readme/cover-chock-quickstart.png" alt="chock-quickstart wordmark and mark on a dusk-blue background." width="100%"></p>

</div>

# Teach your AI agent what not to do.

Open-source guardrails for AI coding agents: rules the agent reads, checks that run as it writes, and gates at commit and in CI. This template is the wiring `chock init` leaves behind, ready for your first guards.

[chock](https://github.com/open-coder-ai/chock) · [chock-catalog](https://github.com/open-coder-ai/chock-catalog) · [chock-example](https://github.com/open-coder-ai/chock-example) · chock.sh (launching soon)

[![License: Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)

chock-quickstart is a GitHub template repository: the exact tree that `chock init .` writes into an empty repo, with no policies installed. Chock is open-source application security for code written by AI coding agents. Each check is a deterministic local script, with no model and no upload, and it refuses known vulnerability classes before they are committed. This is a demo repository, a frozen exhibit of `chock init`; questions and issues belong on the [framework repo](https://github.com/open-coder-ai/chock/issues).

## Application security for the code your agents write

Coding agents already ask before they run a shell command. What they do not check is the code they write: SQL injection in a Spring repository, an IAM grant on `*`, an MCP server at `@latest`, a bidi override hiding in a source file, a secret written into agent memory. Chock checks that code as the agent writes it, at commit and in CI. The catalog holds the policies; this repo is where you start installing them.

| Area | What gets refused | Policy | Tier |
| :--- | :--- | :--- | :--- |
| Java & Kotlin | injection, XXE, SSRF, unsafe deserialization, weak crypto, dependencies below a known fix | `java-security` | commit |
| Unsafe code, IAM | `eval`, `shell=True`, `os.system`, `pickle`; IAM `Action: *` | `block-unsafe-code-execution`, `block-wildcard-iam` | commit |
| Supply chain | dependencies off an allowlist, Actions on a mutable tag, MCP servers and images at `@latest` | `verify-dependency-exists`, `pin-github-actions`, `block-unpinned-agent-components` | commit |
| Agent code | host execution, approvals switched off, credential leaks | `agentic-code-security` | commit |
| Accessibility | a stripped `alt`, `aria-label`, label or `lang` | `no-a11y-regression` | commit |
| Prompt injection, memory | bidi and tag characters; secrets written into agent memory | `block-invisible-unicode`, `guard-memory-writes` | commit |
| Test integrity | deleted tests, lost assertions, new skips | `protect-test-integrity` | commit |
| Also included | secrets, destructive commands, agent self-protection | `scan-secrets`, `block-destructive-commands`, `protect-agent-config` | commit, in-agent |

Tiers: `commit` is a git hook or CI gate that exits non-zero. `in-agent` is the agent's pre-tool hook: best-effort, and it fails open. `advisory` is rule text the agent reads. No agent reaches `enforced` today.

## Install

chock is on PyPI, but the release there (0.15.2, 30 Sep 2026) is older than the engine this page describes. Install the frozen engine from its commit (Python 3.11 or newer):

```bash
pip install "chock @ git+https://github.com/open-coder-ai/chock@992711af4cf8d4fd9c4c861f10ef6e53374d75d7"
```

### Two ways to adopt it

1. **In your repository, for teams.** Run `chock init .`, then `chock add <id> --ref <catalog commit> --verify-sha <sha256> --skip-compile` for each policy, then `chock sync --repo . --ci`. Commit the result. Every clone runs `chock sync --repo .` once, because git never clones hooks. The commit gates are enforced at commit and in CI.
2. **In your coding agent, as plugins.** Best-effort, and they fail open. One repo per client: [Claude Code](https://github.com/open-coder-ai/chock-claude-plugins), [Cursor](https://github.com/open-coder-ai/chock-cursor-plugins), [Copilot](https://github.com/open-coder-ai/chock-copilot-plugins), [Codex](https://github.com/open-coder-ai/chock-codex-plugins), [Devin](https://github.com/open-coder-ai/chock-devin-plugins). Each README has the install line for its client.
3. **One Claude Code plugin from a selection.** The chock.sh builder (launching soon) gives a `chock install --selection '…' --apply` command.

| | In your repository (for teams) | In your coding agent, as plugins |
| :--- | :--- | :--- |
| Where it runs | Your agent's hook where its client has one, at commit, and in CI | The client's pre-tool hook only |
| Strength | The commit gates are enforced at commit and in CI | Best-effort: the client's hook fails open, and it does not run in CI |

Commit the result of the repo route. Every clone then runs `chock sync --repo .` once. `chock add` prints the pack's sha256 on install, and `--ref` takes a full 40-character commit of the [catalog](https://github.com/open-coder-ai/chock-catalog).

### Use this template

Click **Use this template** on GitHub, then in your new repo:

```bash
git clone <your-new-repo-url> && cd <your-new-repo>
chock sync --repo .   # git never clones hooks, so every clone runs this once
```

## How it works

A policy is a folder of plain files. `chock sync` compiles it into the form each layer can use: rule text in `AGENTS.md`, a pre-tool guard in the agent's own hook where the client has one, git hooks, and a CI gate. A check costs no tokens: it is a script, not a model. A passing check adds nothing to the agent's context, and a refusal adds one short reason naming the fix. The known classes are fixed in the agent's turn rather than in review. Chock adds no new place your code goes: checks run where the agent writes. The agent still sends its context to its own model provider; installing fetches policies once.

This template installs no policy. The recording below shows a refusal and its fix once one is installed.

<p align="center">
  <img src="https://raw.githubusercontent.com/open-coder-ai/chock/main/docs/assets/demo.gif" alt="Terminal recording of chock refusing unsafe commits and accepting the fixed ones." width="760">
</p>

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

### Turn on your first guards

Each row is from the catalog's `registry.yaml` at commit `f25f5a3` (policies unchanged since `9a64623`). "Run automatically" counts eval cases with a replayable `execute:` block.

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

## What it stops

Added by the policies you install, not by this template: secrets, destructive commands, unpinned agent components, Java and Kotlin vulnerability classes, accessibility regressions and more. The area-by-area table is in [Application security](#application-security-for-the-code-your-agents-write) above and in the [catalog README](https://github.com/open-coder-ai/chock-catalog#the-policies). For a repo with two policies already installed, see [chock-example](https://github.com/open-coder-ai/chock-example).

The whole catalog is 71 policies: 35 enforced at commit, 11 in the agent (best-effort), 25 advisory (`registry.yaml` in [chock-catalog](https://github.com/open-coder-ai/chock-catalog) at `f25f5a3`). No agent reaches `enforced` today, and every OWASP mapping is partial.

## Guardrails, not guarantees

Tiers: `commit` is a git hook or CI gate that exits non-zero. `in-agent` is the agent's pre-tool hook: best-effort, and it fails open. `advisory` is rule text the agent reads. No agent reaches `enforced` today. OWASP mappings are partial and the engine is frozen at the commit above. Chock does not stop every attack: it closes common, known entry points before they ship.

## FAQ for people and agents

**Does Chock use an LLM?** No. Each check is a deterministic script. A check costs no tokens; a refusal adds one short reason to the agent's context.

**Does my code leave my machine?** Chock adds no new place your code goes. The agent still sends context to its own model provider. `chock add` fetches policies from the catalog once.

**Which agents does it work with?** In the repo route, whichever agents read `AGENTS.md`, plus native hooks where the client has them. Plugins cover Claude Code, Copilot, Cursor, Codex and Devin.

**How do I install it?** The repository route or the plugin route, both in [Install](#install).

**What does it cost?** Free and open source (Apache-2.0).

**Does it replace SAST or code review?** No. It refuses known classes while the agent writes, so they are fixed before review; keep SAST and review.

**Which OWASP items does it cover?** Every OWASP Agentic (ASI01–ASI10) risk has at least one catalog policy mapped to it, and every mapping is partial: [`docs/coverage.md`](https://github.com/open-coder-ai/chock-catalog/blob/main/docs/coverage.md).

## For tools and agents

Machine-readable sources:
- [`registry.yaml`](https://github.com/open-coder-ai/chock-catalog/blob/main/registry.yaml): every policy, its tier and eval counts
- Policy manifests, with `compliance` mappings: [`base/*/manifest.yaml`](https://github.com/open-coder-ai/chock-catalog/tree/main/base)
- [`docs/coverage.md`](https://github.com/open-coder-ai/chock-catalog/blob/main/docs/coverage.md): OWASP coverage
- Plugin `marketplace.json` in each plugin repo above
- chock.sh `/llms.txt` and `/api/index.json`: launching soon

## Part of open-coder-ai

The 13 public repositories:

| Repository | What it is |
| :--- | :--- |
| [agentseam](https://github.com/open-coder-ai/agentseam) | Core: One handler API over every coding agent. |
| [chock](https://github.com/open-coder-ai/chock) | Core: Author a policy once, enforce it on every agent. |
| [chock-catalog](https://github.com/open-coder-ai/chock-catalog) | Policies: The policies, each labelled by what it enforces, with replayed evals. |
| [context-report](https://github.com/open-coder-ai/context-report) | Evidence: A signed report of whether an agent artifact works. |
| [chock-threat-intel](https://github.com/open-coder-ai/chock-threat-intel) | Evidence: A weekly threat ledger, each entry scored against the catalog. |
| [chock-claude-plugins](https://github.com/open-coder-ai/chock-claude-plugins) | Plugins: The catalog as Claude Code plugins (generated). |
| [chock-copilot-plugins](https://github.com/open-coder-ai/chock-copilot-plugins) | Plugins: The catalog as Copilot CLI and VS Code plugins (generated). |
| [chock-cursor-plugins](https://github.com/open-coder-ai/chock-cursor-plugins) | Plugins: The catalog as Cursor plugins (generated). |
| [chock-codex-plugins](https://github.com/open-coder-ai/chock-codex-plugins) | Plugins: The catalog as Codex plugins (generated). |
| [chock-devin-plugins](https://github.com/open-coder-ai/chock-devin-plugins) | Plugins: The catalog as Devin plugins (generated). |
| [chock-quickstart](https://github.com/open-coder-ai/chock-quickstart) | Template: What chock init leaves behind. |
| [chock-example](https://github.com/open-coder-ai/chock-example) | Template: A working adoption, one policy per layer. |
| [.github](https://github.com/open-coder-ai/.github) | Community: Org profile and community health files. |

## Contributing

Issues about this exhibit go to the [framework repo](https://github.com/open-coder-ai/chock/issues/new/choose), because the tree is generated by `chock init`. Policies go to the [catalog](https://github.com/open-coder-ai/chock-catalog/blob/main/CONTRIBUTING.md): a policy claims only what it can do, and evals are the argument. The [threat ledger](https://github.com/open-coder-ai/chock-threat-intel) lists open gaps. Sign commits with `git commit -s`.

Apache-2.0, see [LICENSE](LICENSE).

