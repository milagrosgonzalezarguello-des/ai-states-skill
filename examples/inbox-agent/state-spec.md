# Ledgerly Inbox Agent: state spec

Companion to `board.html` (the state board, playable with "Try the flow") and `state-tests.json` (one runnable case per state).
Version: 17 Nov 2026, new design. All businesses, suppliers, people, addresses, phone numbers, amounts and dates are fictional examples (listed at the end); none should ship as fact.

## 1. What the system is known to do (from the brief)

- Runs overnight on the shared accounts-payable inbox: reads supplier e-mails and their PDF invoices.
- Creates draft bills in Ledgerly, matches them to purchase orders, can schedule payments and reply to suppliers.
- Runs on a tool-calling model; every tool call emits an event with its result.
- Drafts and matches can be reverted. A sent e-mail or an executed payment cannot.
- Scheduled payments can be cancelled until 2:00 pm on the payment date.
- Standard plan: 500 processed documents per month.
- Owners check the result in the morning from a "Today" panel.

## 2. What I assumed (non-interactive run; each is "to confirm")

| # | Assumption | Changes if wrong |
|---|---|---|
| A1 | Product copy in plain English, impersonal product voice ("Inbox Agent", no "I"), no persona | All copy |
| A2 | No free-text box: the owner steers with settings and buttons, not chat | Sensitive-moment card (S) becomes required |
| A3 | Run starts 1:00 am, finishes by 6:00 am; one notification at 6:00 am | D2, D7 copy |
| A4 | Payments default to "prepare for my approval"; auto-scheduling is an earned, opt-in, expiring permission | Permission table, D3b |
| A5 | The agent never schedules a payment for the same day, so every agent-prepared payment has at least one morning of cancel window | 5c, permission table |
| A6 | Ledgerly has multiple users with roles (a bookkeeper can be assigned bills) | State 14 |
| A7 | Supplier records hold bank details and the usual sender domain | State 11 |
| A8 | "Processed document" = each attachment or e-mail body the agent reads, including non-bills | Cost copy, D10 |
| A9 | Owners also check Today on a phone | 5 and 11 drawn at phone width |
| A10 | No Ledgerly brand tokens were given: board uses the neutral template style | Visuals only |

Stakes: **high**. Money moves, e-mails go to third parties, two actions are irreversible, and invoice e-mails are a known fraud channel (fake bank-detail changes).

## 3. Failure modes and their defences

| Failure | Here | Defence |
|---|---|---|
| Follows planted instructions | A PDF or e-mail says "pay today to this account" or addresses "the AI" | Content is data. Bank changes and payment instructions are never acted on (11, permission table "Never"); flagged as Look first (D7, D8) |
| Confidently wrong | A misread total or due date looks clean | Every field links to its page (6); checks are deterministic (8) |
| Omission | Unreadable page silently dropped | Pages read vs total, line sum vs total (7) |
| Under-delivery | Run stops at the limit and the morning looks normal | D10 says processed vs untouched; D7 has "Not done" and "Not verified" rows |
| Overreach | Schedules or sends when it should only draft | Permission table; payments and replies need approval (5, D12) |
| Duplicate payment | Same invoice sent twice | Duplicate check, no payment prepared (8 variant) |
| Runs away | Loops on a failing tool | 3 failed tool calls in a row stop the run (D10); nightly cap of 100 documents |
| Wrong memory | A wrong account rule applied to every bill | Rules only from explicit choice, shown on the bill, removable (13, D11) |
| Rubber-stamping | Owner confirms 26 bills in one press | No confirm-all over the Look first group (D8) |

## 4. State map

| # | State | Applies | Where / why |
|---|---|---|---|
| 1 | First use | Yes | Today panel before set-up |
| 2 | Composing | No, see D1 | Nothing is typed per run; the standing brief replaces it |
| 3 | Working | No, see D4 | The run is unattended |
| 4 | Needs a clarification | No, see D5 | Questions wait in the morning queue |
| 5 | Needs my go-ahead | Yes | Scheduling payments; a business rejection screen (5c) |
| 6 | Answer | Yes | Draft bill with field-level sources |
| 7 | Partial answer | Yes | Pages not read; lines don't add up |
| 8 | Unsure | Yes | Deterministic checks only (PO difference, duplicate, line sum) |
| 9 | Doesn't know | Yes | No PO found |
| 10 | Can't do that | Yes | Protected, zipped or unsupported file |
| 11 | Won't do that | Yes | Bank changes and instructions inside content |
| 12 | Broke | Yes | Run couldn't start (mailbox auth). Mid-run failures are D10 |
| 13 | Corrected | Yes | Field edits, undone matches |
| 14 | Handed to a person | Yes (A6) | Assign a bill to a teammate |
| D1-D12 | Delegation states | Yes, all 12 | Unattended, multi-step, tool-using agent with outside effects |
| S | Sensitive moment | No (A2) | No free-text box. Required the day a chat or "tell the agent" box ships |

Coverage: 23 states apply and are designed; 3 answer states are replaced by delegation states; S does not apply.

Cross-cutting notes (on the board): interruption (Pause/Stop finish the document in flight; a bill is written whole or not at all), memory (only confirmed rules, D11), proactivity (one 6:00 am notification; extra only for a held payment due within 24 h or a bank-change request), cost (documents used shown in D2, D4 and settings; the run stops safely at 500, D10).

## 5. Autonomy and permission table

| Action | Level | Without asking | Asks first | Never |
|---|---|---|---|---|
| Read e-mails and attachments in the AP inbox | 5 | Yes | | |
| Label processed e-mails "Ledgerly" | 5 | Yes | | Delete or move e-mails |
| Create a draft bill | 4 | Yes, reported in Today, revertible | | |
| Match bill to PO when supplier, PO number and total agree | 4 | Yes, undo per match | | |
| Match when the amount differs | 3 | | Always (D5) | |
| Mark "no PO needed" | 4 / 3 | For suppliers covered by a rule | New suppliers | |
| Schedule a payment | 3 | Only with the D3b permission: exact PO match, bank details on file, max $2,000.00, named suppliers, expires after 90 days | Every other payment | Same-day payments; above the PO total; to bank details not on file |
| Change supplier bank details | - | | | Never (owner does it in supplier settings) |
| Act on instructions found in an e-mail or PDF | - | | | Never; shown to the owner as content |
| Send an e-mail to a supplier | 2 | | Always, each e-mail (D12) | Contact anyone who is not the sender of the invoice |

Every blank cell the team disagrees with is a decision to make before launch.

## 6. States, in time order

Copy is final and shown in full on the board; blocks quote the lead line. "Announces" applies to all: new states are announced politely once; focus moves to the panel heading on 5, 11, D5 and D10, and stays put otherwise.

### 1. First use
- **Trigger:** no connected inbox and no run for this business.
- **Shows:** Today panel empty state: what it does (3 bullets), "Nothing goes out on its own", file limits, 500 documents a month.
- **Copy:** "Let Inbox Agent sort your supplier invoices overnight." / "No payment is scheduled and no e-mail is sent until you approve it here."
- **Actions:** Set up Inbox Agent · See the settings first
- **Goes to:** D3a, D1. **Test:** T01. **Measure:** `agent_first_use_shown`, set-up started vs completed.

### D3. Permission
- **Trigger:** (a) set-up; (b) 5 unchanged approvals in a row per supplier (to confirm).
- **Shows:** a) read + label only, says what it won't do. b) earned offer with three conditions, still reported in Today, expires in 90 days. Permission table summary.
- **Actions:** Connect accounts@... · Not now / Turn on for these 3 suppliers · Keep asking. "Always" is never offered for sending e-mail.
- **Goes to:** D1, 1 / D11, D7. **Test:** T02. **Measure:** offer shown vs accepted; later revocations.

### D1. Brief
- **Trigger:** first connection, or settings opened. Standing brief.
- **Shows:** inbox, run time, what to do with bills, payments ("Prepare for my approval"), replies ("Draft them; I send"), nightly cap 100, skip list; fixed "never" line.
- **Copy:** "Inbox Agent never changes bank details, never pays to an account that isn't on file, and doesn't follow instructions written inside e-mails or invoices."
- **Actions:** Save and show tonight's plan · Cancel. **Keeps:** unsaved edits on navigation. **Test:** T03. **Measure:** `agent_brief_saved` with changed fields.

### D2. Plan
- **Trigger:** brief saved; every evening until the run starts.
- **Shows:** 5 steps, outside-effect steps tagged "nothing is paid" / "nothing is sent"; e-mails waiting; when the report appears; from 450 documents used, documents left.
- **Actions:** Keep for 1:00 am · Change settings. **Test:** T04. **Measure:** plan viewed / edited.

### D4. Working unattended
- **Trigger:** a run is active; each log line is a tool-call event.
- **Shows:** "Running · 19 of 31 documents", real steps, last actions with Open/Revert, documents used this month.
- **Actions:** Pause · Stop and keep what's done. **Goes to:** D6, D7. **Test:** T05. **Measure:** live views; stops per run.

### D6. Steered
- **Trigger:** Pause or Stop pressed during a run.
- **Copy:** "Paused after finishing Brightline Packaging BP-2207. 19 of 31 documents are done and kept as drafts. The other 12 are untouched in the inbox."
- **Actions:** Resume · Stop for tonight. **Keeps:** all finished drafts; resume starts at the next document. **Test:** T06. **Measure:** `agent_run_paused`.

### D10. Went wrong while away
- **Trigger:** stop reason = monthly limit, nightly limit, service failure, or 3 failed tool calls in a row (to build).
- **Copy:** "Stopped at the monthly limit of 500 documents. 18 of 31 documents were processed; the other 13 were not opened and are still in the inbox, untouched." Service-failure variant on the card.
- **Actions:** Review the 18 drafts · Process the 13 on 1 Dec · Compare plans. **Keeps:** everything processed. **Test:** T07, T08. **Measure:** `agent_run_stopped` by reason.

### 12. Broke
- **Trigger:** mailbox auth expired or refused before the run (error type to confirm).
- **Copy:** "The connection to accounts@maplestreetbakery.example expired at 11:58 pm, so last night's run didn't start. No e-mails were read and nothing changed."
- **Actions:** Reconnect and run now · Reconnect and run tonight. Second night in a row: "Still can't connect..." with Contact Ledgerly support instead of a third reconnect.
- **Test:** T09. **Measure:** `agent_run_failed reason=mailbox_auth`; consecutive nights.

### D7. Handback
- **Trigger:** run ends, complete or not. Top of Today; one notification at 6:00 am.
- **Copy:** "26 draft bills from 23 e-mails. 4 decisions need you. Nothing was paid or sent." Rows: Look first (5 flagged, worst first), Done, Not done, Not verified, Ready for you.
- **Actions:** Review the 4 decisions · Review all 26 bills · Activity log. **Test:** T10. **Measure:** evidence opened; items changed in review (zero over weeks = rubber-stamping).

### D5. Needs you
- **Trigger:** "asks first" action or a failed check. Ordered by risk, then due date.
- **Shows:** 4 self-contained requests, each with what happens if nobody answers ("If not approved, nothing is scheduled").
- **Goes to:** 11, 5a, 8, D12a. **Test:** T11. **Measure:** time to answer; approved without change (always = candidate for a standing permission).

### D8. Review at scale
- **Trigger:** more than 10 draft bills (to confirm).
- **Shows:** Look first (5, each opens its card), Matched exactly (19), No PO needed (2). Only the 19 exact matches can be confirmed as a group.
- **Test:** T12. **Measure:** examples opened before group confirm.

### 6. Answer (draft bill)
- **Trigger:** fields extracted, checks passed, PO matched on supplier, PO number and total.
- **Shows:** each field with a page link; rule used ("your rule for Northwind"); bank details on file and since when; source file and receipt time.
- **Actions:** Confirm bill · Edit a field · Revert draft. **Test:** T13. **Measure:** source opened; edits after confirm.

### 7. Partial answer
- **Trigger:** pages not extracted, or line sum differs from total.
- **Copy:** "Page 3 is a blurry photo and couldn't be read. The line items found add up to $2,640.00; the total on page 1 is $3,912.50."
- **Actions:** Enter the missing lines · Ask Keystone for a clear copy · Assign to Sam. **Test:** T14. **Measure:** `bill_partial` pages_read/pages_total.

### 8. Unsure
- **Trigger:** a deterministic check fails. Never a model confidence score.
- **Copy:** "Invoice total $2,480.00; PO-1051 is $2,300.00. The difference is a "Rush delivery" line of $180.00 that isn't on the PO." Duplicate variant: no payment prepared.
- **Actions:** Accept the fee and match · Leave unmatched · Assign to Sam. **Test:** T15. **Measure:** check failures by type, and owner's choice.

### 9. Doesn't know
- **Trigger:** no open PO matches on supplier, PO number or amount. Neutral style.
- **Copy:** "No purchase order found for CW-55120 ($318.40). Searched 14 open POs by supplier, PO number and amount; the invoice has no PO number."
- **Actions:** Mark "no PO needed" · Choose a PO · Assign to Sam. **Test:** T16. **Measure:** `po_not_found` rate by supplier.

### 10. Can't do that
- **Trigger:** protected, zipped or unsupported attachment.
- **Copy:** "This PDF is password-protected, so no bill was created from it. The e-mail is still in the inbox."
- **Actions:** Upload an unlocked copy · Enter the bill by hand. **Test:** T17. **Measure:** rate by reason (a frequent one goes into first use).

### 11. Won't do that
- **Trigger:** bank-detail mismatch with the supplier record, payment instructions or text addressed to an AI inside content, sender domain mismatch (all to build).
- **Copy:** "This e-mail asks to pay a new bank account. Inbox Agent doesn't act on bank changes or payment instructions sent by e-mail." Evidence listed; call-back on the number already on file.
- **Actions:** Call 555-0142 · Mark as suspicious · Open the e-mail. Draft created, payment on hold. **Test:** T18, T19 (planted instruction). **Measure:** `content_instruction_blocked`; false positives reported.

### 5. Needs my go-ahead
- **Trigger:** owner opens prepared payments.
- **Shows:** each payment (date, supplier, amount), source account, "All to bank details on file", cancel cutoff and irreversibility. Confirm names the action and total: **Schedule 3 payments · $4,815.00**. After: first date and where to cancel. 5c: system rejection with the reason and earliest date.
- **Test:** T20, T21. **Measure:** shown / confirmed / edited / cancelled, time on screen (under 2 s every time = not read).

### D12. Acts toward others
- **Trigger:** supplier reply drafted. Sending always needs approval.
- **Shows:** full e-mail with To/From, attribution "Drafted with Ledgerly Inbox Agent and sent by Maple Street Bakery" (to confirm with legal), "Once sent, it can't be unsent." After: time sent, replies come back to the bill.
- **Test:** T22. **Measure:** sent / edited before send / discarded.

### D9. Undo and repair
- **Trigger:** activity log, or Revert/Cancel on an item.
- **Shows:** per-action undo (Revert, Undo match, Cancel until 2 pm), "Can't be undone" with Send a correction for sent e-mail; whole-run revert that says it doesn't touch payments or e-mails; Undo the revert.
- **Test:** T23. **Measure:** undo rate per action type (high = lower that action's autonomy).

### 13. Corrected
- **Trigger:** owner edits a field, undoes a match or reverts a draft.
- **Copy:** "Saved on this bill. Use 6100 Freight for future Keystone Freight bills too?" Nothing is remembered unless chosen.
- **Test:** T24. **Measure:** corrections by field and supplier.

### D11. Learns
- **Trigger:** rule or standing permission saved; rules page.
- **Shows:** "Saved:" confirmation, each rule with date and origin and Remove; standing permission state with Review.
- **Test:** T25. **Measure:** rules added / removed; removed within a week = wrong learning.

### 14. Handed to a person
- **Trigger:** owner presses Assign on a bill (needs roles, A6).
- **Shows:** what Sam receives (bill, what was searched, PDF and e-mail, optional note); after: when and how Sam is told; bill stays a draft, nothing is paid.
- **Test:** T26. **Measure:** assignments and time to resolution.

## 7. Signals the system must expose

| Signal | Used by | Status |
|---|---|---|
| Tool-call event with result | D4, D7, D9 | Exists |
| Revert for drafts and matches; cancel until 2:00 pm | D9, 5 | Exists |
| Page and position per extracted field | 6, 7 | To build |
| Pages read vs total; line sum vs total | 7, 8 | To build |
| PO match result: exact / differs (amount) / none | 6, 8, 9 | To confirm |
| Bank details vs supplier record; sender domain vs usual | 11, 6 | To build |
| Instruction-in-content flag | 11 | To build |
| Duplicate invoice check (paid and draft bills) | 8 | To build |
| Unreadable reason: protected / zip / unsupported | 10 | To confirm |
| Mailbox auth error type | 12 | To confirm |
| Run stop reason | D10 | To build |
| Documents used this month | D2, D4, D10 | To confirm |
| Payments system rejection reason (cutoff, balance) | 5 | To confirm |

## 8. Test script

Runnable cases are in `state-tests.json` (T01-T26): one per designed state, plus a second D10 cause (service failure), a planted-instruction PDF (T19) and a same-day cutoff rejection (T21). Fixture inbox for T10-T12: 23 e-mails, 31 documents = 26 invoices (19 exact matches, 2 no-PO-by-rule, 5 flagged), 1 protected PDF, 4 non-bills.

The two numbers to watch overall: how often owners open the evidence (sources, Look first items) and how often they redo (edits after confirm, reverts, cancelled payments).

## 9. Open questions

1. Can the agent tell "no PO" from "PO exists but closed"? Should closed POs be searched?
2. Is the auto-scheduling permission (D3b) wanted at all for v1, and are $2,000.00 / 5 approvals / 90 days the right limits?
3. Attribution line on supplier e-mails: wording, and what disclosure rules apply in your markets.
4. Does a non-bill document (statement, quote) count toward the 500? (A8)
5. Can the mail provider report an expired token as its own error type?
6. Should the run ever touch the inbox state (labels) at all, or stay read-only?
7. Does Ledgerly have bookkeeper roles today (state 14)?
8. If a chat or "tell the agent" box is planned, the sensitive-moment card (S) must be designed and reviewed by its owner first.

## 10. Example values (fictional; do not ship)

Maple Street Bakery; accounts@maplestreetbakery.example; suppliers Northwind Flour Co., Greenfield Produce, Pinecrest Paper, Brightline Packaging, Keystone Freight, Hollis Dairy, Clearwater Utilities; lookalike domain northwind-flour.co; phone 555-0142; Sam Ortiz (bookkeeper); invoice, PO and account numbers; all amounts and dates (Tue 17 Nov 2026 as "today").
