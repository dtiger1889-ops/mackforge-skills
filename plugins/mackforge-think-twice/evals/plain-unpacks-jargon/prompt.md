---
max_turns: 6
allowed_tools: [Skill]
tags: [should-fire, plain]
---

Say that in plain English. Here is the message I was sent:

"Rolled back the B7 migration because the P2 canary tripped on the ACL sync. Root cause is a stale TTL on the shard-3 cache, so reads were served pre-merge. Hotfix is queued behind the WQ-12 freeze; ETA is the next window, assuming no regression in the nightly soak. Until then the old path stays pinned and writes are idempotent, so nothing is lost."
