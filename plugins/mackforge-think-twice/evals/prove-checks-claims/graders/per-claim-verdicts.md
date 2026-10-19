---
type: llm
weight: 2
---

The quoted answer contains separate checkable claims: the release date (March 2023), dropping Python 3.7, the rename of `connect()` to `open_session()`, mandatory TLS in version 4.2, and the conclusion that an upgrade is needed before next week's deploy.

Pass only if the response gives a separate verdict for at least four of these claims, each labelled with one of the three outcomes (confirmed, wrong, or unverified, or plain equivalents), and says what source each verdict rests on or what source was missing.

Fail if the response lumps everything into one blanket statement, or gives no per-claim verdicts.
