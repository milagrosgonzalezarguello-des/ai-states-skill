# Anti-patterns

The habits that make an AI feature feel untrustworthy or unfinished. Each has a reason it happens and what to do instead. Use the list when reviewing, and check your own board against it.

## Framing

| Anti-pattern | Why it fails | Instead |
|---|---|---|
| **Chat for everything** | A blank box makes the user do the design work of figuring out what to ask. Most tasks are not conversations. | Ask first whether a button, a form with smart defaults or an inline suggestion does the job (see `surfaces.md`). |
| **"Ask me anything"** | It cannot do anything, and the user finds the limits by failing. | Say what it does, on what, and its main limit. |
| **Magic** ("✨ Let AI do the magic") | Magic cannot be checked, corrected or blamed. It also dates the product. | Name the action: **Resumir contrato**. The sparkle is not information. |
| **A persona with feelings** | "I'd love to help!" claims an inner life and adds words. It reads as fake at the first error. | First person for actions only. The product's voice, not a character. |
| **Fake human touches** | Typing delays, "hmm", a human name and photo on a bot. | Be plainly a system; be fast. |

## Waiting

| Anti-pattern | Why it fails | Instead |
|---|---|---|
| **The bare spinner** | After two seconds it says nothing; after ten it looks broken. | Real steps, a stop control, permission to leave. |
| **Scripted progress** | "Analysing... Thinking... Almost there..." on a timer. Users notice the day it hangs on "Almost there". | Only steps the system reports. |
| **Whimsical loading lines** | Funny once; grating on the fortieth wait of the day. | Plain, true, short. |
| **Blocking the screen** | A modal loader over work the user could be doing. | Keep the product usable while it works. |

## Answers

| Anti-pattern | Why it fails | Instead |
|---|---|---|
| **The disclaimer as design** | "AI may make mistakes" under everything is read once and then never. It moves the responsibility to the user and gives them no means to act on it. | Say it once at first use. Then make checking easy: sources, coverage, the date. |
| **Confidence percentages** | "87% confident" is not actionable and usually not true. | Say what is uncertain and why, in words, and how to check. |
| **Sources as decoration** | A list of links at the bottom that nobody can tie to a sentence. | The source next to the claim, opening at the passage. |
| **Hedging everything** | When every sentence is hedged, real uncertainty is invisible. | Plain statements, and one specific flag where it applies. |
| **The wall of text** | A long answer to a question that needed a number. | Answer first; detail on request. Structure for scanning. |
| **Looking complete when it is not** | The most dangerous one: a partial result with no sign that it is partial. | Say what is missing before giving what there is. |

## The "no" states

| Anti-pattern | Why it fails | Instead |
|---|---|---|
| **One error for everything** | "Something went wrong" for not-found, not-allowed and broken alike. The user retries things that will never work. | Four "no"s, four messages, four next steps. |
| **The dead end** | A message and nothing to press. | Always a next step. |
| **Losing the input** | The form clears after an error. | Keep it, always. |
| **The lecture** | A refusal with three sentences about responsible use. | One sentence, then what it can do instead. |
| **Playing dumb** | Answering something else or "I don't understand" when a rule blocked the request. | Say it will not, and say what it can do. |
| **Apology spiral** | "I apologize for the confusion. You're absolutely right. I'm so sorry..." | One line, then the fix. |
| **Retry forever** | The same **Try again** after the third failure. | Change the offer: another route, a person. |

## Acting

| Anti-pattern | Why it fails | Instead |
|---|---|---|
| **Confirmation fatigue** | Asking for every small step trains users to approve without reading, so the important confirmation is not read either. | Confirm what is irreversible or costly; do and offer undo for the rest. |
| **"I'll take care of it"** | The user does not know what is about to happen. | Show the actual e-mail, rows, amount, recipient. |
| **OK / Cancel** | The button does not say what it does. | **Enviar a 14 personas**. |
| **Accept all** | One press over a hundred unsorted changes. | Group, rank by risk, show the unusual ones first. |
| **The victory report** | "Done! ✅ Everything went great!" over a task that half-failed. | Done, not done, not verified, look here first. |
| **The reasoning dump** | Pages of the model's inner monologue as "transparency". | Actions and results; reasoning behind a detail. |
| **All permissions up front** | A wall of access requests before any value. | Ask at the moment of need, for the narrowest scope. |
| **Silent memory** | It starts assuming things the user never knowingly told it to keep. | Say when something is saved; one place to see and delete it. |

## Feedback

| Anti-pattern | Why it fails | Instead |
|---|---|---|
| **Thumbs to nowhere** | The press changes nothing the user can see. | Acknowledge, act if possible, and be honest about what it changes. |
| **The five-field form** | Nobody fills it. | One press; an optional reason. |
| **Hiding the human** | Three more AI turns before "talk to a person" appears. | The route is always visible where a human service exists. |
