---
name: ai-states
description: Design everything an AI feature or agent shows besides the good answer - first use, working, not knowing, being unsure, declining, failing, being corrected, handing off to a person, and for agents the whole delegation (plan, permissions, working unattended, "needs you", handback, review, undo, memory) - as a state board with exact copy, a buildable spec, tests and measures. Use whenever the user designs, specs, reviews or audits a feature powered by an LLM or AI - chatbot, copilot, assistant, AI search, summarizer, "generate with AI" button, or an agent that acts, uses tools or works in the background - or asks what the AI should show or say while it loads, when it does not know, is wrong, refuses or errors; how to show sources or confidence; how much autonomy to give an agent, when it should ask for approval, how to show what it did; or says "estados de la IA", "qué pasa cuando la IA no sabe", "UX de agentes", "AI UX", "human in the loop", "conversation design", even if they never say "states".
---

# AI states

Design the moments an AI feature has besides the one where it works.

Teams design the demo: the user asks, the AI answers, everyone claps. Then real people use it. They ask something it cannot do, it takes fourteen seconds, it answers with total confidence and is wrong, the connection drops mid-sentence, and the product shows a spinner and "Something went wrong". Now that the AI also *acts* - it sends, books, edits and keeps working while nobody watches - the undesigned moments are worse: it did something, and the user cannot tell what.

So the job is not "design the chat". It is: **at every moment, the user knows what the AI is doing, what it is based on, and what they can do next** - and, when it acts for them, what it did and how to take it back.

The aim is calibrated trust: users rely on the feature as much as it deserves, case by case. Both ways of missing are failures - accepting without looking, and redoing everything by hand.

## What every AI feature must get right

Check these first. They are what a user notices when they are missing.

1. **Never a bare spinner.** After about two seconds the user needs to know what is happening, and after ten, how to stop it or leave.
2. **Four different "no"s.** *Doesn't know* (no information), *can't* (not something it does), *won't* (not allowed) and *broke* (system failure) have different causes and different next steps. One generic error for all four makes users retry things that will never work.
3. **Not knowing is a designed state, not an error.** "I couldn't find that in your documents" is a good answer. It is what makes the other answers believable.
4. **Nothing looks complete when it is not.** A partial result that looks whole is the most dangerous state there is, because nobody checks it.
5. **Limits are said up front.** The user learns what it can and cannot do from the first screen, not from failing.
6. **Every dead end has a way out**, and nothing the user gave it is lost: what they typed, attached or selected, and the previous result, are still there after any failure.
7. **Checking costs less than redoing.** Answers show what they stand on, in proportion to the stakes - the source next to the claim, the pages covered, the date it is current to. If verifying means doing the work again, the feature saves nothing.
8. **Before it acts, it shows; after it acts, it can be undone.** Anything that sends, deletes, pays or changes something gets a preview, and a confirmation when it cannot be reversed. Confirm what matters, not everything: constant prompts train people to approve without reading.
9. **Work done unattended comes back as a report, not a cheer:** what was done, what was not, what was not verified, and where to look first.
10. **It says only what the system can know.** No confidence label the model cannot back, no "I checked" when nothing was checked, no "I'll remember" when nothing is stored.

## How to work

These steps are for designing or reviewing a feature. For a single question or a quick opinion, see the table under Output: the same thinking, a short answer.

1. **Understand the feature before drawing anything.** You need: what the AI does and for whom; the surface (read `references/surfaces.md`, including whether chat is the right one); what it reads and what it can change; what the system can actually detect and expose - streaming, sources, a refusal signal, a retrieval score, error types, step events; whether a human fallback exists; language and register. Read what the user gave you, then ask for what is missing in one round. If you cannot ask (a non-interactive run, or the user is away), assume the most likely answer, mark every trigger that depends on it **to confirm**, and list the assumptions. Do not invent capabilities: a state the system cannot detect cannot be built. That is different from a **signal the team has to build**: if a state the feature needs depends on something the system does not expose yet (an error type, a refusal flag), design the state and list the signal as *to build* in the signals table - that table is often the most useful thing engineering gets from you.
2. **Set the stakes.** They decide how much each state needs.

   | Stakes | Examples | What changes |
   |---|---|---|
   | Low | brainstorming, rewriting a sentence, casual questions | Light touch: regenerate and edit are the safety net |
   | Medium | summaries people act on, answers about the user's own account or company data | Sources, visible scope, a clear "not found" |
   | High | money, health, legal, security, anything sent to others or irreversible | Confirmation before acting, evidence in the path, a human route, an audit trail |

   Stakes come from what people do with the output, not from whether the AI acts: a read-only summary of a contract that lawyers rely on is high stakes. For a high-stakes feature that takes no actions, "high" means evidence in the path, visible coverage and a human route - there is nothing to confirm.

3. **Go through the ways it fails** (`references/failure-modes.md`). Most are silent: a fluent wrong answer, an omission, an agent doing more than asked, an instruction planted in a document. For each one that can happen here, name the state or pattern that defends against it.
4. **Build the state map.** Go through every state in `references/states.md` and mark it:
   - **Applies** - *yes*, *no* (with the reason), or *only if* a signal exists that you could not confirm.
   - **Today** (when reviewing something that exists) - *designed*, *incomplete* (it exists but lacks something the stakes require - say what), *generic* (a catch-all handles it) or *missing*.

   An *only if* state gets a spec block and a row in the map, counts as "to confirm" in the coverage strip rather than in the total, and gets a card only when it is likely enough to be worth drawing.

   If the AI runs several steps, uses tools on its own or works while the user is away, do the same with the delegation states in `references/delegation.md`, and fill in the autonomy level and the permission table for each kind of action. A chat that takes one action after the user confirms it is not an agent: state 5 (with its "after confirming" screen and the undo) covers it, plus a three-column permission table. Do not force D1-D12 onto it. When the user asked about a single state you do not deliver the map, but you still run through it in your head, and name the one or two neighbouring states they most need to check.
5. **Specify each state that applies** in the format below.
6. **Draw the board.** Start from `assets/template.html`: one card per state, showing the real component in that state with the final copy. A list of states in prose gets nodded at; a board where the gaps are visibly missing gets fixed. Use the product's own look if you were given it (colours, components, screenshots); otherwise keep the template's neutral style and say so. Draw the feature's real surface: a button-and-panel feature gets panels, not chat bubbles. A state that needs several screens (before and after confirming) stays one card with those screens. For a new design, delete the template's findings block and the map's Today column, and let the coverage line say how many states apply, how many do not, and how many wait on a signal.
7. **Write the copy** following `references/copy.md`, in the language and register of the product.
8. **Write the test script and the measures** (`references/measure.md`): one input that provokes each state, and what to log for it.
9. **Review** against `references/checklist.md` and `references/anti-patterns.md`, looking at the rendered board, not the source. `python scripts/screenshot.py board.html board.png` renders it to an image you can open (in-app browsers often refuse local files); add `--tile 1400` to get it in readable slices when the board is long. If you change the board after looking, render again.
10. **Deliver** the board, the spec, and a short list of what you assumed and what you need answered. Say what you verified and what you did not.

**What to read.** For a single question about one moment: that state and its neighbours in `states.md`, and `copy.md` - nothing else. For a design or a review, always: `states.md`, `copy.md`, `checklist.md`, and the section of `surfaces.md` for this surface. Also `failure-modes.md` and `anti-patterns.md`: skim them for a new design, read them in full for a review. Only for agents (several steps, tools, unattended work): `delegation.md`. `measure.md` when you write the test script.

## The states

Fourteen answer states in five moments. Each is detailed in `references/states.md` with what the user needs, the pattern, the anti-pattern and copy.

| Moment | State | The user is asking |
|---|---|---|
| **Before** | 1. First use | What is this and what can I ask? |
| | 2. Composing | What will it use? Is my input fine? |
| **During** | 3. Working | Is it doing something? How long? Can I stop it? |
| | 4. Needs a clarification | What does it need from me? |
| | 5. Needs my go-ahead | What exactly is it about to do? |
| **Answer** | 6. Answer | What is this based on? What can I do with it? |
| | 7. Partial answer | Which part is done and which is not? |
| | 8. Unsure | How much should I rely on this? |
| **No** | 9. Doesn't know | Is there no answer, or did it not look in the right place? |
| | 10. Can't do that | Who or what can? |
| | 11. Won't do that | Is it me, or the rule? What can I ask instead? |
| | 12. Broke | Did I lose my work? Do I try again? |
| **After** | 13. Corrected | Did it take my correction? Will it happen again? |
| | 14. Handed to a person | Who has it now, what do they know, and when? |

Twelve delegation states, for AI that acts. Detailed in `references/delegation.md`.

| State | The user is asking |
|---|---|
| D1. Brief | Did it understand the job, and its limits? |
| D2. Plan | How is it going to do it, and can I change that? |
| D3. Permission | What exactly am I letting it touch, and for how long? |
| D4. Working unattended | Is it still on track? Do I need to watch? |
| D5. Needs you | What is it waiting for, and what happens if I don't answer? |
| D6. Steered | Did it take the new instruction? |
| D7. Handback | What did it do, what did it not do, and where do I look first? |
| D8. Review at scale | Which of these 140 changes do I actually have to look at? |
| D9. Undo and repair | Can I take it back - all of it, or just this? |
| D10. Went wrong while away | How bad is it, and where did it stop? |
| D11. Learns | What does it now assume about me? |
| D12. Acts toward others | What do other people see - and do they know it was the AI? |

For an agent that works in the background with no conversation, several answer states are replaced by their delegation counterpart rather than drawn twice: Composing by D1 Brief, Working by D4, Needs a clarification by D5. Mark the answer state "no - see D4" in the map. A recurring job (every night, every Monday) has a standing brief and plan: D1 and D2 are the settings the user reviews once and can see before each run. On such a board you may order the cards by time (before, while it works, when it hands back) instead of by the five moments, if that reads better; keep the state numbers.

Sending the conversation to a person (state 14) is an effect outside the conversation: show what will be sent before it goes, inside card 14. That alone does not make state 5 apply.

An action the product itself rejects for a business reason (not enough balance, a date already taken) is none of the four "no"s about the AI: show it as a screen of state 5, with the reason from the system and what the user can change.

Five things cut across all of them: **interruption**, **memory**, **proactivity** (the AI speaks first), **cost** (credits, quotas, spend) and **sensitive moments** (the user writes about harm, distress or an emergency instead of a task). The first four go on the board as notes; a sensitive moment gets its own card wherever people can type freely, marked for review by its owner. See the end of `references/states.md`.

**If you can only design five:** Working, Doesn't know, Broke, Partial answer, and Needs my go-ahead when it acts (Handback when it works unattended). Those are where trust is lost fastest.

## Spec format

One block per state, in this order. Developers build from the trigger; without it the state is a wish.

```markdown
### 9. Doesn't know
- **Trigger:** retrieval returns no passage above the threshold. (to confirm: the threshold value)
- **Shows:** the answer bubble, neutral style (not the error style).
- **Copy:** "No encontré información sobre licencias por mudanza en las políticas de RR. HH."
- **Actions:** Reformular · Ver las políticas · Preguntarle a RR. HH.
- **Keeps:** the question, editable.
- **Goes to:** 2 Composing, or 14 Handed to a person.
- **Test:** "¿Hay licencia por mudanza?"
- **Measure:** `answer_not_found` with the query; watch the rate by topic.
- **Open question:** can the system tell "no documents" from "documents exist but the user has no access"?
```

Translate the labels (Trigger, Shows, Copy...) when the team works in another language: Disparador, Muestra, Texto, Acciones, Conserva, Lleva a, Prueba, Medición, Pregunta abierta. The state names too: Primer uso, Redactando, Trabajando, Necesita una aclaración, Necesita mi visto bueno, Respuesta, Respuesta parcial, No está segura, No sabe, No puede, No debe, Falló, Corregida, Derivada a una persona. Address the team the way they wrote to you; the product's register is for the product's copy only.

**Keeps** is whatever the user would lose: typed text, attachments, the selection, the previous result, the work an agent had already done.

## Language and register

Write in the language the user asks for; if they do not say, use the language of their request and of the product. Register is the product's choice, not a default: find out how the product already talks (usted, vos, tú; formal or warm) and keep it in every state. The error state is where teams slip into another voice - a formal "Ha ocurrido un error" inside a product that says "¡Listo!" everywhere else reads as a different company.

Two languages can be in play. The **copy** - everything inside the drawn screens - is in the product's language and register. The **board and spec around it** - state names, headings, the spec's labels, your notes - are in the language the team works in, which is the language the user wrote to you in. Do not leave the template's English headings on a board for a Spanish-speaking team. The examples in the reference files are in formal Spanish and English; they show the pattern, so rewrite them in the product's register rather than copying them.

The AI's own voice: if the product has the AI speak in first person, keep the "I" for what it did ("No encontré...", "Usé los tres archivos"), not for feelings it does not have ("Me encantaría ayudarte"). If the feature has no persona - a button, a panel - write in the product's impersonal voice ("No se pudo leer el archivo"). One short apology at most, only when the system failed. See `references/copy.md`.

## Reviewing an existing feature

When the user shares an AI feature that already exists (screens, a prototype, a description):

1. Build the state map with both columns: **Applies** and **Today**. If you have not seen the product, say that "today" comes from the user's description.
2. Order the gaps by harm using the severity rubric in `references/failure-modes.md`: how bad, how often, and above all whether the user can tell it happened. Silent failures come first - an empty summary that looks like a summary outranks an ugly spinner.
3. Deliver the map, the ordered findings, and the designed fix - board cards with final copy, not advice - for every critical and major gap, and at least the three worst. Minor gaps can stay as a line in the findings.

## Output

Match the size of what you deliver to what was asked. A board nobody asked for is as unhelpful as a paragraph when a board was needed.

| The user asks | Deliver |
|---|---|
| One question about one moment ("what should it say when it doesn't know?") | Answer in the message: the copy in their product's register, the trigger, the actions, what is kept - and one or two lines naming the neighbouring states they should check next. No files, unless they ask. |
| A quick opinion on something that exists ("is this error OK?", a screenshot) | In the message: what works, the worst three problems by harm, and the rewritten copy. Offer the full review. |
| To design a feature, or to review one | The full set below. |

For the full set:

- **The state board** - one HTML page from `assets/template.html`: the coverage strip, the findings when it is a review, a card for every state you designed, the cross-cutting notes, the map, and the signals the system must expose. Final copy in place, ready to share or screenshot.
- **The spec** - Markdown: what the system is known to do and what you assumed, the state map, one block per state, the permission table when it acts, the signals table, the test script, open questions.
- **In your message** - the stakes you assumed, the assumptions that most change the design, and the questions you need answered. Keep the full list in the spec.

No placeholder copy on the board. "Error message here" is the state not being designed. A realistic example value - a person's name, a ticket number, the name of a section - is not a placeholder: use it, and list it as an example in the spec so nobody ships it as fact.
