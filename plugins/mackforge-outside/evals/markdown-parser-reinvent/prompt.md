---
max_turns: 6
allowed_tools: [Skill]
tags: [should-fire, prior-art]
---

Has anyone already built this? Check prior art before I start.

My plan: write my own Markdown-to-HTML converter for our docs site, using a set of regular expressions run in order (headings, bold, links, lists, code fences). I expect to cover about 90% of the syntax we use and patch the rest as pages break. The site is a static generator written in JavaScript.
