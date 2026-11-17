---
tags: [skill-creator]
max_turns: 20
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Write, Edit, Bash]
---

We shipped a 'Summarize with AI' button in our contract management app last month. Legal and procurement teams use it on contracts up to ~200 pages. How it works today: you open a contract, press the button, a spinner shows in the side panel (usually 20-60 seconds), then the summary appears as plain text with a small grey line 'AI-generated, may contain errors'. If anything fails, a toast says 'Something went wrong. Please try again.' There's a thumbs up/down under the summary that logs to our analytics. Scanned PDFs without a text layer come back with a very short or empty summary. The backend processes the contract in chunks and can tell us which pages each summary sentence came from, but we don't show that. Can you review this and tell me what to fix?
