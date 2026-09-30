<div align="center">

<img src=".github/logo.svg" alt="chock-quickstart: exactly what one chock init command leaves behind in an empty repository — the wiring, with no policies installed. The mark is chock's: a wheel held by a chock wedge." width="110">

# chock-quickstart

**Start secure in 60 seconds: the wiring `chock init` leaves behind, ready for your first security guards.**

[![security policies](https://img.shields.io/badge/security_policies-48-D9B45C?labelColor=0D1626)](https://github.com/open-coder-ai/chock-catalog)
[![eval cases](https://img.shields.io/badge/eval_cases-1%2C179-D9B45C?labelColor=0D1626)](https://github.com/open-coder-ai/chock-catalog)
[![OWASP Agentic Top 10](https://img.shields.io/badge/OWASP_Agentic_Top_10-10%2F10-D9B45C?labelColor=0D1626)](https://github.com/open-coder-ai/chock-catalog)
[![template repo](https://img.shields.io/badge/repo-template-D9B45C?labelColor=0D1626)](https://github.com/open-coder-ai/chock-quickstart/generate)
[![license](https://img.shields.io/badge/license-Apache--2.0-D9B45C?labelColor=0D1626)](LICENSE)

[the framework →](https://github.com/open-coder-ai/chock) ·
[the full catalog →](https://github.com/open-coder-ai/chock-catalog) ·
[with policies installed →](https://github.com/open-coder-ai/chock-example)

</div>

> **Demo repository.** A frozen exhibit of `chock init`, nothing more. Questions and issues
> belong on the [framework repo](https://github.com/open-coder-ai/chock/issues).

<p align="center">
  <img src="https://raw.githubusercontent.com/open-coder-ai/chock/main/docs/assets/demo.gif" alt="Terminal: five security guards adopted from the catalog; a hard-coded AWS key, an MCP server at @latest, a wildcard IAM grant, model output piped into os.system and a Trojan Source bidi override are each refused at commit; the fixed file commits cleanly." width="760">
</p>

Your coding agent has a shell, your git history and your cloud credentials. It can hard-code
a key, run `git push --force`, or wire an MCP server at `@latest` — and a rule in a prompt is
forgotten when the context fills. Chock refuses the dangerous action before it lands: as a git
hook, a CI gate, or the agent's own pre-tool hook. *A rule an agent reads is advice. A hook
that exits non-zero is a control.*

## Start secure in 60 seconds

| Step | Do this | You get |
| :---: | :--- | :--- |
| 1 | Click **Use this template** above | Your own repo with the wiring below, no policies yet |
| 2 | `git clone <your-new-repo-url> && cd <your-new-repo>` | A local checkout |
| 3 | `pip install chock && chock sync --repo .` | Hooks installed — git never clones hooks, this wires them in |
| 4 | `chock add <policy>` ([next section](#turn-on-your-first-security-guards)) | Your first guard, compiled and live on the next commit |

```bash
git clone <your-new-repo-url> && cd <your-new-repo>
chock sync --repo .   # git never clones hooks — this wires them in
```

## Turn on your first security guards

Each guard is one command: it is copied from the
[catalog](https://github.com/open-coder-ai/chock-catalog), compiled, and wired into your git
hooks and every supported agent's config.

```bash
chock add scan-secrets                     # everyone
chock add block-destructive-commands       # everyone
chock add protect-main-branch              # everyone
chock add block-unpinned-agent-components  # anyone wiring MCP servers or agent tooling
chock add java-security                    # Java / Kotlin teams
chock add no-a11y-regression               # front-end teams
chock status                               # what's installed, and what each one enforces
```

| Guard | What it refuses | Tier | Eval cases |
| :--- | :--- | :--- | ---: |
| `scan-secrets` | Hard-coded credentials: vendor key prefixes, private-key blocks, key/token/password assignments — in staged changes, and in an agent's tool-call arguments where the write guard is wired. Pattern-matched; not a replacement for a dedicated secret scanner | enforced-at-commit | 32 |
| `block-destructive-commands` | `rm -rf` on absolute, home or root-adjacent paths, `git push --force`, `reset --hard`, `clean -f`, `kubectl delete`, `terraform destroy`, `aws s3 rm --recursive` and more; the pre-push hook refuses any non-fast-forward push. Friction, not a security boundary | enforced-at-commit | 80 |
| `protect-main-branch` | Direct commits and pushes to `main` / `master` (configurable) — work goes through a branch and a pull request | enforced-at-commit | 4 |
| `block-unpinned-agent-components` | Agent components at an unpinned version: `npx`/`uvx`/`bunx` launches at `@latest` (the standard MCP server idiom), `"@latest"` in agent config, `:latest` container images (OWASP ASI04) | enforced-at-commit | 12 |
| `java-security` | 129 rules in 16 packs: SQL / command / SpEL / LDAP / XPath / template injection, XXE, SSRF, unsafe deserialization, path traversal and zip slip, weak crypto and trust-all TLS, disabled Spring Security, exposed actuator, known-exploited dependency versions. Each rule or pack is allow · deny · ask in `.chock/security.json` | enforced-at-commit | 115 |
| `no-a11y-regression` | A change that retracts an accessible name an element already had — `alt` emptied, `aria-label` removed, `aria-hidden` / `role=presentation` added, `label` or `lang` removed, a flagged element deleted instead of fixed — so ADA / Section 508 / WCAG work can't silently regress | enforced-at-commit | 20 |

**Tiers, honestly.** `enforced-at-commit` means a git hook (and CI gate) exits non-zero before
the change lands. `best-effort` guards run in the agent's pre-tool hook and fail open if that
hook crashes. `advisory` is rule text the agent reads. The top tier, `enforced`, is reached by
no agent today. Guardrails, not guarantees.

<details>
<summary>Everything else in the catalog (48 policies, 1,179 eval cases)</summary>

| Area | Examples |
| :--- | :--- |
| Secrets & data leakage | `protect-commit-privacy`, `guard-memory-writes`, `block-unapproved-egress` |
| Hook bypass | `block-no-verify`, `block-curl-pipe-sh`, `rtk-dangerous-actions-blocker` |
| Agent self-protection | `protect-agent-config`, `protect-ci-workflows`, `block-wildcard-agent-permissions`, `block-unguarded-agent-spawn`, `verify-mcp-allowlist` |
| Supply chain | `verify-dependency-exists`, `pin-github-actions` |
| Prompt injection | `block-invisible-unicode` (Trojan Source, Unicode tag smuggling) |
| Secure agent code | `agentic-code-security`, `block-unsafe-code-execution`, `block-wildcard-iam` |
| Test integrity | `protect-test-integrity`, `block-test-skips` |
| OWASP Agentic Top 10 | `owasp-asi01` … `owasp-asi10` |

Full list, tiers and evals: [chock-catalog](https://github.com/open-coder-ai/chock-catalog).
</details>

## What `chock init .` wrote

```
.
├── AGENTS.md
├── CLAUDE.md
├── chock.lock
├── .gitattributes
├── .gitignore
├── LICENSE
├── README.md
├── docs/
│   └── README.md
├── .agents/
│   ├── policies/
│   └── skills/
├── .chock/
│   ├── bin/
│   ├── config.yaml
│   ├── coverage.json
│   ├── dependency-allowlist.txt
│   └── registry.json
├── .claude/
├── .gemini/
└── .github/
```

| Path | What it is |
| :--- | :--- |
| `AGENTS.md` | The single source of agent rules; everything else delegates here |
| `CLAUDE.md`, `.claude/`, `.gemini/`, `.github/` | Thin per-agent wrappers — nothing agent-facing lives twice |
| `.agents/policies/` | Policies once you `chock add` some, plus the generated `INDEX.md` an agent reads first |
| `.agents/skills/` | The bundled authoring skills (`eval`, `optimize`, `policy-init`, `validate`) an agent uses to write and test policies |
| `.chock/` | The engine's own state: `config.yaml` you're free to edit, plus `registry.json`, `coverage.json`, `dependency-allowlist.txt`, and the vendored hook adapter `bin/claude_code.py` that re-installs hooks on a fresh Claude Code session, since git never clones them |
| `chock.lock` | Installed packs, pinned by hash (none yet) |
| `.gitattributes` | Pins generated and hash-attested files to LF, so a pack checks out byte-identical on Linux or Windows |
| `.gitignore` | Keeps the per-machine gate outcome log (`.chock/log/`) out of commits |

What each of these is, file by file: [`docs/README.md`](docs/README.md).

Next steps from here:

```bash
chock add protect-main-branch   # install a guardrail from the catalog
chock status                    # see what's installed and what it enforces
chock check                     # is this repo sound?
```

For the version of this repo *with* policies installed — one per artifact layer — see
[chock-example](https://github.com/open-coder-ai/chock-example).

## How it works

<p align="center">
  <img src="https://raw.githubusercontent.com/open-coder-ai/chock/main/docs/assets/architecture.svg" alt="Author a policy once, compile it, and enforce it on every agent's native surface." width="820">
</p>

No LLM calls and no network access at enforcement time: guards are stdlib Python and shell,
deterministic and reviewable.

## Part of the open-coder-ai family

Everything under [open-coder-ai](https://github.com/open-coder-ai) is built on one rule: a claim must match a
mechanism. Where this repository sits among the others:

| Repository | What it is |
| :--- | :--- |
| [chock](https://github.com/open-coder-ai/chock) | The framework: write a policy once, enforce it on git hooks, CI, and every agent |
| [chock-catalog](https://github.com/open-coder-ai/chock-catalog) | The 48 security policies, each graded by what it actually enforces, with 1,179 eval cases |
| [agentseam](https://github.com/open-coder-ai/agentseam) | The primitives layer for every coding agent: one handler API over their hooks, instruction files, plugin packaging and config, with a capability matrix that carries its provenance. chock is one thing built on it |
| [context-report](https://github.com/open-coder-ai/context-report) | A signed report format for whether a plugin, hook, skill or `AGENTS.md` actually works |
| [chock-threat-intel](https://github.com/open-coder-ai/chock-threat-intel) | A weekly, human-reviewed threat digest mapping MITRE ATLAS and OWASP entries to a catalog answer |
| [chock-claude-plugins](https://github.com/open-coder-ai/chock-claude-plugins) · [copilot](https://github.com/open-coder-ai/chock-copilot-plugins) · [cursor](https://github.com/open-coder-ai/chock-cursor-plugins) · [codex](https://github.com/open-coder-ai/chock-codex-plugins) · [devin](https://github.com/open-coder-ai/chock-devin-plugins) | The catalog compiled into each client's native plugin format; generated only, rebuilt and diffed in CI |
| **chock-quickstart** | This repo: what `chock init` leaves behind |
| [chock-example](https://github.com/open-coder-ai/chock-example) | The same scaffold with policies installed, one per artifact layer |

## Contribute

This tree is a frozen exhibit of `chock init`, so fixes belong upstream. Issues go to the
[framework repo](https://github.com/open-coder-ai/chock/issues/new/choose).

| Good first contribution | Where |
| :--- | :--- |
| Found a bypass? Add an eval case that reproduces it | [chock-catalog](https://github.com/open-coder-ai/chock-catalog/blob/main/CONTRIBUTING.md) |
| Verify an agent row in the capability matrix with a live run | [agentseam](https://github.com/open-coder-ai/agentseam/blob/main/CONTRIBUTING.md) |
| Ship a new policy with `chock new policy <id>` — the `policy wanted` entries in the [threat ledger](https://github.com/open-coder-ai/chock-threat-intel/blob/main/reference/agentic-threat-ledger.md) are the open work list | [chock-catalog](https://github.com/open-coder-ai/chock-catalog/blob/main/CONTRIBUTING.md) |
| Add an agent adapter | [chock](https://github.com/open-coder-ai/chock/blob/main/CONTRIBUTING.md) |

Commits are signed off under the DCO (`git commit -s`). Read
[CONTRIBUTING](https://github.com/open-coder-ai/chock/blob/main/CONTRIBUTING.md) first;
report vulnerabilities privately per [SECURITY](https://github.com/open-coder-ai/chock/blob/main/SECURITY.md).

## License

Apache-2.0 — see [LICENSE](LICENSE).
