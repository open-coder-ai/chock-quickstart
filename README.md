<div align="center">

<img src=".github/logo.svg" alt="chock-quickstart: exactly what one chock init command leaves behind in an empty repository — the wiring, with no policies installed. The mark is chock's: a wheel held by a chock wedge." width="110">

# chock-quickstart

**What `chock init` leaves behind: the wiring exhibit.**

[the framework →](https://github.com/open-coder-ai/chock) ·
[the full catalog →](https://github.com/open-coder-ai/chock-catalog) ·
[with policies installed →](https://github.com/open-coder-ai/chock-example)

</div>

> **Demo repository.** A frozen exhibit of `chock init`, nothing more. Questions and issues
> belong on the [framework repo](https://github.com/open-coder-ai/chock/issues).

## Use this template

Click **Use this template** above, then sync it into your new repo:

```bash
git clone <your-new-repo-url> && cd <your-new-repo>
chock sync --repo .   # git never clones hooks — this wires them in
```

## What `chock init .` wrote

```
.
├── AGENTS.md
├── chock.lock
├── .gitattributes
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

The wiring behind that tree: `.agents/policies/` and `.agents/skills/` are what an agent
reads to work here — policies once you `chock add` some, plus the bundled authoring skills
(`eval`, `optimize`, `policy-init`, `validate`) it uses to write and test them. `.chock/` is
the engine's own state: `config.yaml` you're free to edit, plus `registry.json`,
`coverage.json`, `dependency-allowlist.txt`, and the vendored hook adapter in
`bin/claude_code.py` that re-installs hooks on a fresh Claude Code session, since git never
clones them. `.claude/`, `.gemini/` and `.github/` are thin per-agent wrappers — nothing
agent-facing lives twice, everything delegates back to the single `AGENTS.md`.
`.gitattributes` pins generated and hash-attested files to LF, so a pack checks out
byte-identical whether the clone happens on Linux or Windows.

What each of these is, file by file: [`docs/README.md`](docs/README.md).

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
| [agentseam](https://github.com/open-coder-ai/agentseam) | The primitives layer for every coding agent: one handler API over their hooks, instruction files, plugin packaging and config, with a capability matrix that carries its provenance. chock is one thing built on it |
| [context-report](https://github.com/open-coder-ai/context-report) | A signed report format for whether a plugin, hook, skill or `AGENTS.md` actually works |
| [chock-threat-intel](https://github.com/open-coder-ai/chock-threat-intel) | A weekly, human-reviewed threat digest scored against the catalog |
| [chock-claude-plugins](https://github.com/open-coder-ai/chock-claude-plugins) · [copilot](https://github.com/open-coder-ai/chock-copilot-plugins) · [cursor](https://github.com/open-coder-ai/chock-cursor-plugins) · [codex](https://github.com/open-coder-ai/chock-codex-plugins) | The catalog compiled into each client's native plugin format; generated only, rebuilt and diffed in CI |
| [chock-example](https://github.com/open-coder-ai/chock-example) | The same scaffold with policies installed, one per artifact layer |
