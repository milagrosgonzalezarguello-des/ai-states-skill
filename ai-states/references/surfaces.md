# Surfaces

The same states look different depending on where the AI lives. Identify the surface first; it tells you which states carry the weight and where each one is shown.

## First: is chat the right surface?

A text box is the easiest thing to ship and often the wrong thing to use. It makes the user work out what to ask, how to phrase it, and what the product can do. Before designing a chat, check whether the job is better served by:

- **A button** - when the request is always the same ("Resumir este contrato"). Nothing to type, nothing to guess.
- **A form with smart defaults** - when the request has a few known parameters (period, tone, length). Controls are faster and clearer than describing them in a sentence.
- **An inline suggestion** - when the AI's output belongs inside what the user is already editing.
- **A proactive suggestion** - when the product can tell that help is relevant now.
- **Chat** - when requests are open-ended, need follow-up, or the user is exploring.

Most good AI features mix them: a button to start, controls to adjust, and a text box only for what the controls cannot say. If the user asked for "a chatbot", design it, and say where one of the others would serve better.

## Chat (assistant, support bot, copilot panel)

A conversation with a text box.

- Every state is a message or a change in the composer, so the risk is that they all look alike. Give the "no" states and the go-ahead their own visual treatment inside the thread.
- **Weight on:** 1 First use (the empty thread), 3 Working (streaming), 9-11 the three polite "no"s, 14 Handed to a person.
- The composer carries state too: disabled while working with **Detener** in place of **Enviar**; kept and editable after a failure.
- Errors appear in the thread where the answer would have been, not in a toast that disappears.

## Inline assist (rewrite, autocomplete, "improve this", smart reply)

The AI changes or suggests content inside something the user is editing.

- There is often no room for a message; states are shown on the content itself: a highlighted suggestion, a diff, a ghost text.
- **Weight on:** 2 Composing (what selection it will use), 5 Go-ahead (accept or reject the change - the original is always recoverable), 13 Corrected (undo).
- Working must not block typing. If the user keeps typing, the suggestion is discarded silently; that is not an error.
- "No" states are quiet: a short line near the control, never a modal over the user's work.

## One-shot generation ("Generate summary", "Create with AI" button)

The user presses a button and gets an artefact.

- **Weight on:** 3 Working (often long - show steps, let the user leave), 7 Partial, 12 Broke (with the inputs kept), and regenerating without losing the previous result.
- The result needs a clear mark of what it was generated from and when, because it will be read later, out of context.
- The empty state of the place where the artefact will appear is state 1: say what will be generated and from what before the user presses.
- There is no question, so the "no" states map to the input instead: the whole input cannot be processed (a scanned file with no text, an unsupported format) is **10 Can't**, with what would make it work; part of it cannot is **7 Partial**, with what was left out; a rule blocks this content is **11 Won't**. **9 Doesn't know** applies to a specific thing the output should contain and the source does not ("No termination clause found") - show it as an explicit line, not as an absence.
- The voice is the product's impersonal voice, since there is no assistant speaking: "No se pudo leer el archivo", not "No pude leer".
- Messages live in the panel where the result goes, not in a toast.

## AI search and answers over data

A question answered from documents or records, with sources.

- **Weight on:** 6 Answer (sources next to claims), 8 Unsure (conflicting or old sources), 9 Doesn't know (the most frequent "no" - and the one that makes the rest credible).
- Access matters: "nothing found" and "found, but you have no access" are different triggers. Decide with the team whether the second can be said.
- Always offer the plain results as a fallback to the generated answer.

## Agent (acts on the user's behalf, several steps, tools)

The AI does things: sends, books, edits records, runs code - sometimes while the user is away.

- This surface has its own map: the twelve delegation states in `delegation.md`. Use it together with the answer states.
- **Weight on:** D2 Plan and D3 Permission before it starts, D4 Working unattended (a live log of real actions), D5 Needs you, D7 Handback, D9 Undo.
- The user needs a place to see what it is doing now and what it did: an activity log with each action, its result, and its undo.
- Define what it may do without asking, what it must ask for, and what it may never do. That permission table is part of the spec.
- With several agents or tasks running, the surface is a list, not a chat: each task, its state in a word, and whether it is waiting for the user - with the requests gathered in one queue.

## Voice

Spoken, no screen or a small one.

- There is nothing to scan, so every state is shorter and options are at most three.
- Working is a sound or a short phrase; silence over two seconds feels broken.
- Go-ahead repeats the key fact back ("Envío 500 pesos a Laura Gómez. ¿Confirmo?").
- Errors say what to say next, not just what went wrong.

## Mixed surfaces

Most real features combine two (a chat panel that also edits the document; a search that can act on a result). Map the states for each surface the user touches, and check the handover between them: where does a failure in the action show up when the user has already closed the panel?
