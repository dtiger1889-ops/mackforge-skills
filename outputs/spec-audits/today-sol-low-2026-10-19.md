model analysis -- 2026-10-19 (Sol, low effort, read-only), not adopted.

1. **Medium — Yolo evals reference sample projects that are never supplied.** `plugins/mackforge-yolo-alchemy/evals/brief-and-ledger/prompt.md:9` and `plugins/mackforge-yolo-alchemy/evals/cut-short-by-limit/prompt.md:9` (commit `faa9c84`). Both prompts claim specific project folders exist in the current directory, but no fixtures or setup create them. Running against this checkout → the required project README/status reads cannot succeed. A compliant implementation must report missing inputs, while one that skips project inspection can produce the requested brief and satisfy the graders. These evals therefore reward bypassing a required step.

Read-only inspection completed; nothing changed.

AUDIT COMPLETE -- mackforge-skills -- 1 findings