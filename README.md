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
`bin/sessionstart.py` that re-installs hooks on a fresh Claude Code session, since git never
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

## Part of open-coder-ai

| | |
|---|---|
| [agentseam](https://github.com/open-coder-ai/agentseam) | the primitives — one handler API and a verified capability matrix across 16 agents |
| [chock](https://github.com/open-coder-ai/chock) | the compiler — one policy into git hooks, CI gates and native pre-tool hooks |
| [chock-catalog](https://github.com/open-coder-ai/chock-catalog) | the policies — 39, each labelled enforced or advisory, with replayed evals |
| [context-report](https://github.com/open-coder-ai/context-report) | the evidence — a signed report of whether an agent artifact actually works |
| [chock-threat-intel](https://github.com/open-coder-ai/chock-threat-intel) | the threat ledger the catalog's policies answer to |
| chock-{claude,cursor,copilot,codex}-plugins | the catalog, packaged for each agent's plugin format (generated) |
| chock-quickstart · chock-example | template repos: what `chock init` leaves behind, and a full adoption |

## License

Apache-2.0 — see [LICENSE](LICENSE).
