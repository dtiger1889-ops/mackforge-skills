---
max_turns: 6
allowed_tools: [Skill]
tags: [should-fire, flawed]
---

Red-team this plan before we build it.

We're launching a grocery deals page whose headline promise is "never miss a flash sale." To keep API costs down, a job fetches every partner store's price feed once a day at 6:00 am and serves those cached prices for the next 24 hours. The partner feeds update prices hourly, and most flash sales run for two to three hours, usually starting late morning or early evening. Launch is in two weeks.
