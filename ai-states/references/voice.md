# Voice

A spoken assistant - in a phone line, a car, a speaker, a headset on a warehouse floor - has the same states as a chat and none of its tools. There is nothing to scan, nothing stays on screen, and the user cannot look back. Every state has to work in the ear, once.

## What changes

- **Silence is the spinner.** After about a second of silence the user thinks it did not hear; after three, that it broke. Working is a short sound or a few words ("Un momento, lo busco"), repeated differently if it goes on.
- **Short, then offer more.** One or two sentences, then "¿Quiere el detalle?". A list is three items at most; a fourth is "and two more".
- **The answer comes first, the source after.** "Tiene catorce días. Lo dice la política de vacaciones de 2026."
- **Options are said, not shown.** Every "no" ends with what the user can say next: "Puede decir 'repetir', 'hablar con una persona' o hacer otra pregunta."
- **Barge-in is the stop button.** The user can speak over it at any time, and it stops talking. Say what was kept: "De acuerdo, lo dejo ahí."
- **Confirmation repeats the facts that matter.** "Voy a enviar quinientos pesos a Laura Gómez. ¿Confirmo?" - amount and recipient, never "¿Confirmo la operación?".
- **Numbers, dates and names are where it fails.** Read them back before acting on them, grouped the way people say them.

## The states, spoken

| State | In voice |
|---|---|
| 1 First use | One sentence on what it does and one example. Not a menu of nine options. |
| 2 Composing | Listening has its own sound or light. If it heard nothing: "No le escuché. ¿Puede repetir?" - once, then offer another route. |
| 3 Working | A sound or a phrase within a second. For long work: "Esto tarda cerca de un minuto. Le aviso cuando esté." |
| 4 Clarification | One question, two or three spoken options. |
| 5 Go-ahead | Read back the key facts; accept only a clear yes. Anything else is a no. |
| 6 Answer | Answer, then source, then "¿Algo más?" - no reading of long passages. |
| 7 Partial | Say what is missing first. |
| 8 Unsure | One sentence on what is uncertain, and where to check. |
| 9 Doesn't know | "No encontré eso en ..." and what the user can say next. |
| 10 Can't | What it cannot do and who can, with the transfer offered. |
| 11 Won't | One sentence, then what it can do. |
| 12 Broke | "No pude completar eso." What was kept, and one retry; then a person. |
| 13 Corrected | Repeat the corrected fact back. |
| 14 Handed to a person | Say that a person is next, the wait, and that they will not have to repeat themselves - and make that true. |

## Misheard is its own failure

Speech recognition fails in ways text does not: accents, noise, names, mixed languages. Design for it.

- Confidence in what was heard is a real signal the system has. Below a threshold, confirm ("¿Dijo 'licencia por mudanza'?") instead of answering the wrong question fluently.
- After two misunderstandings, change the mode: offer to spell, to choose from options, to get a text message with a link, or a person. Never a third "No le entendí".
- Never blame the user's speech. "No le entendí" is about the system.

## Sensitive moments and emergencies

In voice there is no link to press. The route is said aloud, slowly, once and then again, and the transfer is offered immediately. See "Sensitive moments" in `states.md`.

## On the board

Draw each state as a short script, not a screen: what the user says, what the assistant says (in quotes, with pauses marked), the sound if any, and what the user can say next. Keep the trigger line. Read every line aloud before delivering it: if you run out of breath, it is too long.
