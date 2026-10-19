---
max_turns: 6
allowed_tools: [Skill]
tags: [should-fire, prior-art]
---

Get an outside view before I build this.

I'm about to write a small background job runner for our web service: a Postgres table of pending jobs, a worker loop that polls it every few seconds, and my own retry logic with exponential backoff and a dead-letter table for jobs that fail five times. Expected load is a few thousand jobs a day, and the service is already written in Python with Postgres as its only datastore.
