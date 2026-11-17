---
tags: [skill-creator]
max_turns: 30
timeout_seconds: 900
allowed_tools: [Read, Glob, Grep, Skill, Write, Edit, Bash]
---

We're building "Inbox Agent" for a small-business invoicing product called Ledgerly (fictional). Overnight, the agent goes through the shared accounts-payable inbox: it reads supplier e-mails and their PDF invoices, creates draft bills in Ledgerly, matches them to purchase orders, and can schedule payments and reply to suppliers. Owners check it in the morning from a "Today" panel. It runs on a tool-calling model; every tool call emits an event with its result; drafts and matches can be reverted, a sent e-mail or an executed payment cannot. Scheduled payments can be cancelled until 2 pm on the payment date. There is a monthly limit of 500 processed documents on the standard plan. Design the agent experience: what the owner sees before, while and after it works.
