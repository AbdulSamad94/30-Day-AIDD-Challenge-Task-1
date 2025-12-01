---
ID: 0004
TITLE: Fix main.py ImportError and Update README
STAGE: green
DATE_ISO: 2025-12-02
SURFACE: agent
MODEL: claude-sonnet-4-5-20250929
FEATURE: 002-calculator-basic-ops
BRANCH: 002-calculator-basic-ops
USER: null
COMMAND: user-feedback
LABELS: ["bugfix", "documentation", "main.py"]
LINKS:
  SPEC: null
  TICKET: null
  ADR: null
  PR: null
FILES_YAML:
  - src/main.py
  - README.md
TESTS_YAML: []
---

## Prompt

```text
got this error tho, importError: attempted relative import with no known parent package, at line 2, from .calculator.calculator import calculate
```

## Response

Addressed the `ImportError` in `src/main.py` by populating it with an example usage that expects module execution. The `README.md` was updated to provide explicit instructions on running `main.py` as a module (e.g., `python -m src.main "<expression>"`), preventing the relative import issue. This also involved correcting minor formatting issues in `README.md` that arose during previous edits.
