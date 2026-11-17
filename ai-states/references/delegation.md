# Delegation states

The examples below speak in first person, as an agent the user talks to would. A background job with no conversation says the same things in the product's impersonal voice ("3 invoices set aside", not "I set aside 3 invoices").

Use this map, in addition to the fourteen answer states, whenever the AI does work on the user's behalf: it takes actions, runs several steps, uses tools, or keeps working after the user looks away. That is most AI features now. An agent is not a chat with extra buttons: the user is not asking a question, they are handing over a job, and the design problem becomes the one managers have always had - how to delegate without either hovering or being surprised.

**The user's question changes** from "is this answer right?" to "can I leave it alone, and will I be able to tell what it did?"

**Contents:** D1 Brief · D2 Plan · D3 Permission · D4 Working unattended · D5 Needs you · D6 Steered · D7 Handback · D8 Review at scale · D9 Undo and repair · D10 Went wrong while away · D11 Learns · D12 Acts toward others · Autonomy levels · The permission table

---

## D1. Brief

**The user is asking:** Did it understand the job, and its limits?

**Trigger:** the user starts a task that will take several steps or run unattended.

**Pattern**
- The agent restates the job in one or two lines: the goal, what "done" looks like, and the limits it understood (what not to touch, budget, deadline).
- Limits are fields the user can set, not something to remember to type: scope ("only this folder"), spend, time, who may be contacted.
- Missing essentials are asked now, in one round - not at minute twelve.

**Avoid**
- Starting a long task from an ambiguous one-line request and discovering the misunderstanding at the end.

| Español | English |
|---|---|
| Voy a conciliar las facturas de octubre con los pagos del banco. No modifico ningún registro: te dejo las diferencias en una lista. | I'll reconcile October's invoices against the bank payments. I won't change any record: I'll leave the differences in a list. |

## D2. Plan

**The user is asking:** How is it going to do it, and can I change that?

**Trigger:** the task has more than a few steps, or any step has an effect outside the product.

**Pattern**
- The steps in plain words, in order, with the ones that have outside effects marked.
- Editable before starting: remove a step, reorder, add a constraint.
- The plan is the contract for D4: anything outside it is a reason to stop and ask.
- Skip the plan for short, reversible tasks. A plan for a two-step job is a confirmation with extra reading.

## D3. Permission

**The user is asking:** What exactly am I letting it touch, and for how long?

**Trigger:** the agent needs access or an action type it has not been granted.

**Pattern**
- Ask at the moment of need, for the narrowest thing that works: this folder, this action, this run.
- Name what the permission allows in the user's terms ("leer tu calendario y crear eventos"), never the technical scope.
- Three durations, clearly different: **this once**, **for this task**, **always** - and "always" is never the default for anything with outside effects.
- A place where every standing permission is listed and can be revoked (links to D11).

**Avoid**
- A wall of permissions up front, before the user has seen it do anything useful.
- "Always allow" offered on an action that sends money or messages.

## D4. Working unattended

**The user is asking:** Is it still on track? Do I need to watch?

**Trigger:** the task is running and the user may not be looking.

**Pattern**
- A live activity log of real actions: what it did, on what, with what result. Past tense for done, present for now.
- Progress against the plan from D2, not a percentage invented for the bar.
- Controls that stay reachable: **Pausar**, **Detener**, and a way to say something to it (D6).
- What it has spent so far against the budget, if there is one.
- The user can leave. When they do, say how they will be told: notification, e-mail, the task list.
- Several agents or tasks at once: one place listing each, its state in a word, and whether it needs the user.

**Avoid**
- A log of the model's inner monologue. Users need actions and results, not reasoning transcripts; keep reasoning behind a detail.
- An agent that looks identical whether it is working, waiting or stuck.

## D5. Needs you

**The user is asking:** What is it waiting for, and what happens if I don't answer?

**Trigger:** a question only the user can answer, an approval the permission table requires, or something outside the plan.

**Pattern**
- A request that stands on its own: what it was doing, what it found, the decision needed, the options, and its recommendation. The user may be reading it hours later on a phone.
- Say what happens while it waits (the rest continues, or everything is paused) and whether there is a deadline.
- Batch related questions; do not interrupt five times for five rows of the same kind. Offer "apply to all like this".
- With many agents or tasks, requests collect in one queue, ordered by what is blocking the most.

**Avoid**
- A notification that says "Your agent needs attention" and nothing else.
- Approval prompts so frequent that the user approves without reading. If an approval is always granted, it should be a standing permission (D11) or not be asked.

| Español | English |
|---|---|
| Encontré 3 facturas sin pago asociado por un total de $ 184.000. ¿Las marco como pendientes o las dejo fuera del informe? Sigo con el resto mientras tanto. | I found 3 invoices with no matching payment, $184,000 in total. Mark them as pending or leave them out of the report? I'll carry on with the rest meanwhile. |

## D6. Steered

**The user is asking:** Did it take the new instruction, and what happens to the work so far?

**Trigger:** the user sends a message, edits the plan, pauses or stops while it works.

**Pattern**
- Acknowledge at once, even if the current step has to finish first, and say when the change takes effect.
- Say what happens to work already done: kept, redone, or undone.
- **Detener** is immediate for anything not yet executed and honest about anything in flight ("El correo ya salió; los otros dos no").

## D7. Handback

**The user is asking:** What did it do, what did it not do, and where do I look first?

**Trigger:** the task ends - complete, partial or abandoned.

**Pattern**
- Lead with the outcome in one line, then: what was done, what was not and why, what needs the user's eyes, with the riskiest first.
- Evidence the user can open: the files changed, the messages sent, the records touched - each a link, not a claim.
- Say what it verified and what it did not ("Corrí las pruebas; no revisé el formato del PDF").
- Assumptions it made along the way, listed.
- Outside effects called out separately from internal ones.

**Avoid**
- "Done! ✅" and a paragraph of self-congratulation.
- A report indistinguishable between "everything worked" and "I gave up on step 4".

## D8. Review at scale

**The user is asking:** There are 140 changes. Which ones do I actually have to look at?

**Trigger:** the result is too large to check item by item.

**Pattern**
- Group by kind of change, and let the user approve a kind after inspecting examples.
- Rank by risk: put first what is unusual, low-certainty, high-value or irreversible. The agent knows which items it was least sure of; say so.
- Show what did *not* change that the user might expect to.
- Accept, reject and edit per item and per group; nothing is applied to the real system until reviewed, when the stakes call for it.
- Make it cheap to verify: the before and the after side by side, the source one click away.

**Avoid**
- A single **Accept all** over an unsorted list. It is how unchecked work gets shipped.

## D9. Undo and repair

**The user is asking:** Can I take it back - all of it, or just this?

**Trigger:** the user wants to reverse something the agent did.

**Pattern**
- Undo per action and per task, from the activity log.
- Be exact about what undo cannot reach: the e-mail that was read, the payment that settled. For those, offer the repair instead (send a correction, request a refund) and say it is a repair.
- Before any irreversible action the agent says so (answer state 5). After it, the log marks it as irreversible.

## D10. Went wrong while away

**The user is asking:** How bad is it, and where did it stop?

**Trigger:** the run failed, exceeded its budget or time, looped, or went outside the plan while the user was not watching.

**Pattern**
- A stopped agent stops safely: it finishes or rolls back the step in flight and does not start new ones.
- The report says which steps completed, which did not, and the state things were left in - especially half-applied changes.
- Guardrails are part of the design, not only of the code: a spend limit, a step limit, a time limit, each with a message of its own.
- Resuming starts from where it stopped, not from the beginning.

| Español | English |
|---|---|
| Me detuve en el paso 4 de 7: el banco rechazó la conexión tres veces. Los pasos 1 a 3 quedaron aplicados; no toqué nada más. | I stopped at step 4 of 7: the bank refused the connection three times. Steps 1 to 3 were applied; I touched nothing else. |

## D11. Learns

**The user is asking:** What does it now assume about me, and can I change that?

**Trigger:** the agent stores a preference, a standing permission or a fact for future tasks.

**Pattern**
- Say when something is saved, in the moment, with one press to undo it.
- One place listing what it remembers and what it is allowed to do without asking, each item editable and removable, with when and why it was added.
- When a remembered thing shapes a result, show it ("Usé tu formato habitual"), so a wrong memory can be found.
- Autonomy is earned and adjustable: offer to stop asking after the same approval is granted several times; let the user tighten it again at any time.
- Standing permissions for risky actions expire or get re-confirmed.

**Avoid**
- Silent personalization. The user cannot correct what they cannot see.
- "I'll remember that" when nothing is stored.

## D12. Acts toward others

**The user is asking:** What do other people see - and do they know it was the AI?

**Trigger:** the agent contacts or affects someone other than the user: sends a message, books with a business, comments on shared work, talks to another agent.

**Pattern**
- The user sees exactly what the other person will see before it goes, at the stakes that call for it.
- Decide and state how it is attributed: sent as the user, sent as the user's assistant, labelled as AI-written. Disclosure rules for AI-generated communication are tightening; check what applies in the product's markets and build the label in rather than bolting it on.
- Replies from the other side come back to the user, with the thread.
- What the agent may commit to on the user's behalf (dates, money, promises) is in the permission table.

---

## Several agents at once

When the user has more than one agent or task running, or agents hand work to each other, three things change.

- **The surface is a list.** One row per task: what it is, its state in a word (running, waiting for you, stopped, done), since when, and what it has used. Sorted with "waiting for you" on top. A chat cannot show this.
- **One queue for requests.** Everything any agent needs from the user arrives in one place, each request naming the task it belongs to, so nothing waits unseen in a thread nobody opened.
- **Responsibility stays visible.** When one agent's output feeds another, the handback says which agent did what, and a failure names where it started. "The pipeline failed" is the multi-agent version of "Something went wrong".

Also decide and state:
- what happens when two agents want to change the same thing (the second one stops and asks; it never overwrites silently);
- whether a permission given to one agent extends to an agent it calls (default: no - it asks);
- the limit that applies to the whole group (spend, documents, messages sent), not only to each one.

## Autonomy levels

Pick a level per kind of action, not per product. The same agent can file a draft on its own and still need approval to send it.

| Level | The agent | The user | Fits |
|---|---|---|---|
| 1. Suggests | proposes | does it | High stakes, low trust, or learning the domain |
| 2. Drafts | prepares the action | reviews and executes | Outside effects that matter |
| 3. Acts with approval | executes after a yes | approves each one | Irreversible or costly actions |
| 4. Acts and reports | executes, then tells | reviews after, can undo | Reversible, frequent actions |
| 5. Acts silently | executes | sees it in the log | Trivial, reversible, expected |

Choose with two questions: **can it be undone?** and **how bad is a mistake?**

| | Mistake is minor | Mistake is serious |
|---|---|---|
| **Reversible** | Level 4-5 | Level 3-4, undo prominent |
| **Irreversible** | Level 3 | Level 1-3, never above 3 |

## Reversible for a while

Many actions can be undone only until a moment: a scheduled payment until the cut-off, a sent e-mail during a short undo window, an order until it ships. Treat them as reversible until that moment and irreversible after it.

- The approval (state 5) says the deadline in the same sentence as the action: "Schedule 12 payments · each can be cancelled until 2 pm on its date".
- The handback and the activity log show the deadline next to each item while it is still open, and the undo control disappears - with a line saying why - once it has passed.
- Plan the timing so the user has a real chance to use the window: an agent that schedules a payment at 1:55 pm for the same day has turned a reversible action into an irreversible one.
- In the permission table, put these in "asks first" unless the window is long enough for the user to see them during an ordinary day.

## The permission table

Part of the spec for any agent. One row per kind of action.

| Action | Without asking | Asks first | Never |
|---|---|---|---|
| Read the user's calendar | Yes | | |
| Create a draft e-mail | Yes | | |
| Send an e-mail to someone inside the company | | First time per recipient | |
| Send an e-mail outside the company | | Always | |
| Delete files | | | Yes |
| Spend money | | Above the limit the user set | Above the account limit |

Fill it with the team: every blank cell is a decision nobody has made yet, and the agent will make it for them.
