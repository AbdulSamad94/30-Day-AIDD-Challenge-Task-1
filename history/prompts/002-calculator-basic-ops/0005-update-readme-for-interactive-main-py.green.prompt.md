---
ID: 0005
TITLE: Update README for Interactive main.py
STAGE: green
DATE_ISO: 2025-12-02
SURFACE: agent
MODEL: claude-sonnet-4-5-20250929
FEATURE: 002-calculator-basic-ops
BRANCH: 002-calculator-basic-ops
USER: null
COMMAND: user-feedback
LABELS: ["documentation", "main.py", "interactive"]
LINKS:
  SPEC: null
  TICKET: null
  ADR: null
  PR: null
FILES_YAML:
  - README.md
TESTS_YAML: []
---

## Prompt

```text
it should work like a program dude, like when i run the file, it should run like a program, like enter your first number, which operation you want to perform, then enter your second number, like this, its a basic calculator, or, like ask for prompt for full your whole question thing
```

## Response

Updated `README.md` to reflect the new interactive usage of `src/main.py`.
The instructions for running the command-line application now correctly guide the user to execute `python -m src.main` for an interactive experience, prompting for numbers and operations sequentially.
