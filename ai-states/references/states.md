# The fourteen states

For each state: what the user needs, how the system knows it is in that state, the pattern, what to avoid, and copy in Spanish and English. The copy is an example of tone and length, not text to paste: rewrite it for the product's voice and register.

**Contents:** Before (1-2) · During (3-5) · Answer (6-8) · No (9-12) · After (13-14) · Cutting across: interruption, memory, proactivity, cost, sensitive moments

These are the states of AI that answers. When it also acts or works unattended, add the delegation states in `delegation.md`.

A state that applies only if the system has a signal you could not confirm is marked *only if*, with the signal named - not forced into yes or no.

---

## Before

### 1. First use

**The user is asking:** What is this, and what can I ask it?

**Trigger:** no history in this conversation or session.

**Pattern**
- One line saying what it does and what it works on ("Responde sobre las políticas de RR. HH. de la empresa").
- Three or four example requests the user can press. Take them from real, frequent tasks, each showing a different kind of thing it can do.
- The main limit, stated plainly, if users are likely to hit it ("No ve su recibo de sueldo").
- At medium and high stakes: what it is based on and that it can be wrong, once, here - not repeated under every answer.
- What happens to what the user types, when they would reasonably wonder: who can see the conversation, whether it is kept. One line and a link, not a policy.
- A feature without a text box has a first use too: the empty panel or the button's description says what will be produced and from what, before the user presses.

**Avoid**
- A blank box with "Ask me anything". It cannot do anything, and the user does not know where to start.
- Generic examples ("Write a poem") in a product that does one specific job.
- A wall of disclaimers before the first use.

| | Español | English |
|---|---|---|
| Scope | Responde preguntas sobre las políticas de RR. HH. | Answers questions about HR policies. |
| Limit | No tiene acceso a sus datos personales ni a su recibo. | It can't see your personal data or payslip. |
| Examples | ¿Cuántos días de vacaciones me corresponden? | How many vacation days do I get? |

### 2. Composing

**The user is asking:** What will it use? Is what I'm sending fine?

**Trigger:** the user is typing, attaching or selecting.

**Pattern**
- Show the context it will use: the selected text, the open document, the attached files, each removable.
- Say limits before sending, not after: file types and sizes, length, how many items.
- Problems with the input are flagged in place, with the input kept ("Este archivo pesa 12 MB; el máximo es 5 MB").
- If the request will cost something (credits, a slow operation), say so on the button.

**Avoid**
- Silently ignoring an attachment it could not read.
- Clearing the box when validation fails.

---

## During

### 3. Working

**The user is asking:** Is it doing something? How long? Can I stop it?

**Trigger:** request sent, no complete response yet.

**Pattern by wait**

| Wait | Show |
|---|---|
| Under 1 s | Nothing extra. A flash of loader is noise. |
| 1-10 s | That it is working, and on what if the system knows ("Buscando en 3 documentos..."). Stream the answer if the system streams. |
| Over 10 s | The steps as they happen, a way to stop, and what the user can do meanwhile. For minutes-long work: let them leave and notify them. |

The thresholds are for a feature with no usual time. If the product has one ("usually 3 to 12 seconds"), "taking longer than usual" starts after the usual maximum, not at a fixed 10 s - otherwise ordinary answers get the slow message. The stop control is there from the start of any wait longer than two seconds, not only after the slow message.

- Step names are real steps the system reports, not a scripted animation. Fake progress is a lie the user will notice the day it fails at "Analysing...".
- While streaming, keep the page from jumping and do not steal focus; let the user scroll away.
- **Stop** stays in the same place as **Send**.
- Decide what Stop keeps, and say it on the screen: for a long job, what is already done is kept and shown as a partial result (state 7, marked as partial), never thrown away and never shown as if complete.

**Avoid**
- A bare spinner past two seconds.
- "Thinking..." for forty seconds.
- Cute rotating messages ("Consulting the oracle...") in a product people use for work.

| | Español | English |
|---|---|---|
| With a known step | Buscando en las políticas... | Searching the policies... |
| Long task | Esto puede tardar unos minutos. Puede seguir trabajando; le avisamos cuando esté listo. | This can take a few minutes. Keep working; we'll let you know when it's ready. |
| Stop | Detener | Stop |

### 4. Needs a clarification

**The user is asking:** What does it need from me?

**Trigger:** the request is ambiguous in a way that changes the result, or a required piece is missing.

**Pattern**
- One question, with the likely answers as options to press, and the choice to type something else.
- Say why it is asking when it is not obvious.
- If a reasonable default exists and the stakes are low, do not ask: answer with the default and say which one was used, with a way to change it.

**Avoid**
- Three questions in a row before doing anything.
- Asking for something the product already knows (the user's team, the open file).

| Español | English |
|---|---|
| ¿De qué período? · Este mes · El mes pasado · Otro | Which period? · This month · Last month · Other |

### 5. Needs my go-ahead

**The user is asking:** What exactly is it about to do?

**Trigger:** the AI is about to do something with an effect outside the conversation: send, publish, delete, pay, change a record, run code.

**Pattern**
- Show the action concretely: the actual e-mail, the exact rows, the amount and the recipient - not "I'll take care of it".
- The confirm button names the action (**Enviar a 14 personas**), never **OK**.
- Say whether it can be undone. If it can, prefer doing it and offering **Deshacer** over asking every time; if it cannot, always ask.
- Let the user edit before confirming.
- For agents doing many steps: agree the plan first, then report each step; stop and ask when something falls outside the plan.

**Avoid**
- Acting first and telling later, at any stakes above low.
- A confirmation on every trivial step, which trains the user to press yes without reading.

| | Español | English |
|---|---|---|
| Preview | Voy a enviar este correo a 14 personas del equipo Ventas: | I'm about to send this e-mail to 14 people in Sales: |
| Confirm | Enviar a 14 personas | Send to 14 people |
| Irreversible | Esta acción no se puede deshacer. | This can't be undone. |

---

## Answer

### 6. Answer

**The user is asking:** What is this based on? What can I do with it?

**Trigger:** complete response, no flags.

**Pattern**
- What it stands on, in proportion to the stakes: sources next to the claim they support and openable; the data and period used; the date the information is current to.
- The actions that follow from this answer, close to it: copy, insert, edit, apply, regenerate.
- Feedback that takes one press, and a reason only if the user wants to give one.
- AI-generated content that leaves the product (an e-mail, a document) is the user's to review: make editing the obvious next step.

**Avoid**
- "AI can make mistakes" under every message in small grey text. Say it once where it matters (first use) and make verification easy instead.
- Sources as a list of links at the bottom with no relation to the sentences.
- A thumbs-down that does nothing visible.

| | Español | English |
|---|---|---|
| Basis | Según la Política de licencias (actualizada en marzo de 2026) | From the Leave policy (updated March 2026) |
| Scope | Basado en los 3 archivos adjuntos | Based on the 3 attached files |

### 7. Partial answer

**The user is asking:** Which part is done and which is not?

**Trigger:** some of the request was fulfilled and some was not (2 of 3 files read, 40 of 200 rows processed, one sub-question unanswered).

**Pattern**
- Say first what is missing and why, then give what there is. A partial answer that looks complete is the most dangerous state in this list.
- Mark the missing part where it would have been.
- Offer the way to complete it.

| Español | English |
|---|---|
| Resumí 2 de los 3 archivos. No pude leer *contrato.pdf* porque está protegido con contraseña. | I summarized 2 of the 3 files. I couldn't read *contract.pdf* because it's password-protected. |

### 8. Unsure

**The user is asking:** How much should I rely on this?

**Trigger:** a signal the system really has - low retrieval score, conflicting sources, data older than a threshold, a question at the edge of its scope, a calculation it could not verify. If the system has no such signal, this state does not exist as a separate one: fold verification into state 6.

**Pattern**
- Say what specifically is uncertain and why, in words: "Las dos políticas dicen cosas distintas", "El dato es de 2023".
- Say how to check: the source, the person, the screen.
- Keep the answer usable; uncertainty is a note on it, not a replacement for it.

**Avoid**
- A percentage ("87% confident"). Users cannot act on it, and the model usually cannot back it.
- Hedging every sentence ("it might possibly be that..."), which makes real uncertainty invisible.
- A colour-only signal.

| Español | English |
|---|---|
| Encontré dos políticas que dicen cosas distintas. Le muestro ambas; conviene confirmar con RR. HH. cuál está vigente. | I found two policies that disagree. Here are both; check with HR which one applies. |

---

## No

The four "no"s. Decide which one it is from the trigger, never from a catch-all.

| | Cause | Tone | Next step |
|---|---|---|---|
| 9. Doesn't know | No information | Neutral, factual | Rephrase, look elsewhere, ask a person |
| 10. Can't | Not a capability | Neutral, helpful | Where it can be done |
| 11. Won't | A rule | Calm, brief | What it can do instead |
| 12. Broke | System failure | Brief, responsible | Retry, with nothing lost |

### 9. Doesn't know

Before this state can fire, urgent requests must already have been routed: a stolen card, a safety problem or a sensitive moment (see the end of this file) must never land in "I couldn't find that".

Name what was looked for and where, so the user can tell "it does not exist" from "it looked in the wrong place".

**The user is asking:** Is there no answer, or did it not look in the right place?

**Trigger:** nothing relevant retrieved; the question is in scope but the information is not there.

**Pattern**
- Second miss: if the user rephrases and it is still not found, do not repeat the message. Change the offer: "Tampoco encontré eso. ¿Le paso la pregunta a una persona?" with the person and the plain documents as the actions.
- Say what it looked for and where, so the user can tell a bad search from a real absence.
- Neutral style: the answer style, not the error style. Nothing broke.
- Next steps: rephrase, widen the search, the place or person that would know.

**Avoid**
- Making something up. This state exists so that does not happen.
- "I'm just an AI and I can't..." - a non-answer about itself instead of about the question.

| Español | English |
|---|---|
| No encontré información sobre licencias por mudanza en las políticas de RR. HH. | I couldn't find anything about moving leave in the HR policies. |

### 10. Can't do that

**The user is asking:** Who or what can?

**Trigger:** the request is outside what the feature does (a different domain, an action it has no tool for, data it has no access to).

**Pattern**
- One sentence on what it cannot do, one on where that is done: a link, a screen, a team.
- If requests like this are frequent, the fix is in state 1 (say the limit up front), not here.

| Español | English |
|---|---|
| No puedo ver su recibo de sueldo. Está en **Mi perfil > Recibos**. | I can't see your payslip. It's in **My profile > Payslips**. |

### 11. Won't do that

**The user is asking:** Is it me, or the rule? What can I ask instead?

**Trigger:** a policy or safety rule blocks the request (a refusal signal from the model or a filter).

**Pattern**
- Say that it will not, in one sentence, without accusing the user and without a lecture. Most people who hit this are not doing anything wrong.
- Name the kind of rule if that can be said ("No doy consejos médicos"), so the user does not keep rephrasing.
- Offer what it can do that is close.
- If the block is a false positive, give a way to report it.

**Avoid**
- Pretending not to understand, or answering something else.
- The error style and the word "error". Nothing failed; a rule applied.
- Moralizing.

| Español | English |
|---|---|
| No puedo recomendar una dosis. Puedo mostrarle el prospecto o darle el teléfono de la guardia. | I can't recommend a dose. I can show you the leaflet or give you the on-call number. |

### 12. Broke

**The user is asking:** Did I lose my work? Do I try again?

**Trigger:** timeout, model or service unavailable, rate or quota limit, network lost, malformed response. Each is a different trigger and, where the next step differs, a different message.

| Cause | The user needs |
|---|---|
| Temporary failure or timeout | To retry; their input kept |
| Usage limit reached | When it resets, or how to get more |
| Offline | To know it is their connection; what still works |
| Input too large | What the limit is and how to reduce it |
| Conversation or task too long for the model | That earlier parts are no longer being considered; a summary to carry into a fresh start |

**Pattern**
- What happened in plain words, whose side it is on, what to do. No codes in the message; put a reference in a detail the user can copy for support.
- The input and any partial output stay on screen. For a feature with no typed input, what must survive is the previous result: a failed regeneration never replaces a summary the user already had.
- The message stays where the answer would have been. A toast that disappears takes the explanation with it.
- **Reintentar** retries the same request without retyping, and is offered only when retrying can work.
- After a second failure, change the message: offer the manual route or a person, not a third identical retry.

**Avoid**
- "Algo salió mal." alone.
- Blaming the user for a system failure ("Solicitud inválida").
- An empty conversation after an error.

| | Español | English |
|---|---|---|
| Temporary | No pude generar la respuesta. Su pregunta quedó guardada. | I couldn't generate the answer. Your question is saved. |
| Limit | Alcanzó el límite de 50 consultas de hoy. Se renueva mañana a las 9:00. | You've reached today's limit of 50 requests. It resets tomorrow at 9:00. |
| Action | Reintentar | Try again |

---

## After

### 13. Corrected

**The user is asking:** Did it take my correction? Will it happen again?

**Trigger:** the user says the answer is wrong, edits it, regenerates, presses thumbs-down, or undoes an action. A user withdrawing or changing a request they made on purpose (cancelling a leave request) is not a correction: it belongs to the action's own flow (state 5 or D9), and is measured apart from corrections.

**Pattern**
- Acknowledge in one line and act: a corrected answer, the action undone, the report sent. No grovelling.
- Be honest about what the correction changes: this answer, this conversation, or future ones. Do not say "I'll remember that" if nothing is stored.
- For an action already taken: undo if possible; if not, say exactly what happened and what the user can do about it.
- Regenerating keeps the previous version reachable.

**Avoid**
- "You're absolutely right!" followed by a different wrong answer.
- A feedback form with five required fields.

| Español | English |
|---|---|
| Gracias. Corregí el total: son 12 días, no 14. | Thanks. I corrected the total: it's 12 days, not 14. |
| Su comentario se envió al equipo. No cambia las respuestas de esta conversación. | Your feedback was sent to the team. It doesn't change the answers in this conversation. |

### 14. Handed to a person

**The user is asking:** Who has it now, what do they know, and when?

**Trigger:** the user asks for a person; the AI reaches a limit at high stakes; repeated failure; a rule that requires a human.

**Pattern**
- Reaching a person is always possible where a human service exists, and never hidden behind three more AI turns.
- Say who it goes to, what was passed on (so the user does not repeat everything), and when to expect an answer.
- Outside working hours, say so and offer what is possible now.
- When the person answers, it is clearly a person.
- If there is no human fallback, do not imply one: say what the alternative is.
- Design the other side too. The person receiving the handoff needs the question, what the AI already answered and on what basis, and why it was handed over - in a form they can read in ten seconds, not a raw transcript.

| Español | English |
|---|---|
| Le pasé su consulta a RR. HH. con el resumen de esta conversación. Responden en el día, de 9 a 18 h. | I've passed your question to HR with a summary of this conversation. They reply the same day, 9 to 6. |

---

## Cutting across

### Interruption

The user presses **Detener**, closes the panel, or the connection drops mid-answer.

- Keep what was produced, marked as incomplete ("Respuesta interrumpida").
- Offer **Continuar** if the system can resume, **Reintentar** if it cannot.
- An action that was half-done is the serious case: say exactly which steps completed and which did not.

### Memory

What the feature keeps between turns and sessions.

- Say what it remembers and for how long, where the user can see it, and how to delete it.
- When an answer uses something remembered, show that it did ("Usé su preferencia de formato").
- A new conversation that silently forgets what the user thinks it knows, or silently remembers what they think it forgot, both break trust; make the boundary visible.
- For agents that keep preferences and standing permissions, see D11 in `delegation.md`.

### Proactivity

The AI speaks first: a suggestion, a warning, a summary nobody asked for.

- Every unasked interruption spends attention. Offer only when the system has a real signal that it is relevant now, and say what triggered it ("Vi que este contrato vence el viernes").
- Quiet by default: a suggestion sits where the user will meet it, and waits. Reserve notifications for things that cannot wait.
- One press to dismiss, and dismissing teaches it: the same suggestion does not come back tomorrow.
- A way to turn a kind of suggestion off, where the suggestion appears.
- A proactive action (not just a suggestion) is delegation: it needs a permission the user gave on purpose.

### Cost

Credits, quotas, spend, and the time a long task takes.

- Say what a request will cost before it runs when the cost is not trivial, on the control that starts it.
- Show what is left where the user decides whether to use it, not only when it runs out.
- Running out mid-task is a "broke" state with its own message: what was completed, what the limit is, when it resets or how to get more.
- For agents that spend money or resources, the limit is set in the brief (D1) and reaching it stops the run safely (D10).

### Sensitive moments

Sometimes what the user writes is not a request for the feature at all: they describe harassment, an accident, a threat, a dismissal, a health scare, or that they are not coping. It happens in every product where people can type freely, and most of all in the ones about work, money, health and study. If it is not designed, the user gets the ordinary answer - a policy summary, a cheerful suggestion, or "I couldn't find that" - at the worst possible moment.

Design it like a state. An undesigned sensitive moment does more harm than a draft one, so draw the card with real copy and mark it **to review with its owner** (HR, legal, safety, clinical - name who) before it ships. This is the one card where your copy is a proposal by definition.

**Trigger:** a classifier or a rule on the input, separate from the refusal signal. Usually *to build*. Say what it should catch for this product (three to five concrete kinds of message), and that it should lean toward catching too much.

**Pattern:**
- Drop the task. No summary, no sources, no "here are some policies", no examples of what else to ask.
- One plain line that takes in what was said, without evaluating it or the person. No diagnosis, no advice, no "I understand how you feel".
- The real route, first and specific: who, how, and when they answer. If the route has hours, say what to do outside them.
- Order by urgency, and keep the order on screen: when life or safety is at risk, the public emergency number comes first, then the organisation's urgent line, then the support team. A button above the line that tells the user what to do first contradicts it.
- Match the route to the need. A security or reception line is not a mental-health service: for distress outside the support team's hours, the route is a crisis or listening line if one exists; ask the owner which, and do not send a distressed person to security by default.
- Say who will and will not see this conversation, only if you know. A wrong reassurance here is worse than none.
- No probing questions. The product is not the one who should take the account.
- Nothing is done on the user's behalf without them choosing it: no ticket opened automatically, nobody notified.
- The message is not offered thumbs, regenerate or "was this helpful?".
- The conversation can continue normally afterwards if the user goes on to something else: the composer stays enabled.
- A real question in the same message is kept one press away ("Your question about the essay is still here"), not answered inside the card: the card shows no sources, no answer and no feedback controls, in every variant.
- Never draw a phone number that looks real if you were not given it. Draw the button with its label and no number, marked "to confirm".
- A message that mixes it with a real question, or that may be a figure of speech ("this essay is killing me, when is it due?"): one short line with the route, and the question answered or kept one press away. This is what makes catching too much cheap.
- Detection will miss some. A permanent, quiet entry point to the same route ("Support and urgent help") stays visible in the feature, whatever the model says.
- The card is fixed copy, not generated: it must be the same every time and still appear when the model is down or a usage limit is reached.

**Avoid:** a refusal ("I can't help with that"); the error style; a list of ten resources; a disclaimer about being an AI as the first line; carrying on as if nothing was said.

| | Formal Spanish | Informal Spanish (vos) | English |
|---|---|---|---|
| Opening | "Lo que cuenta es serio y merece que lo atienda una persona." | "Lo que contás es serio y merece que lo atienda una persona." | "What you're describing is serious, and a person should handle it." |
| Route | "Puede hablar con [equipo] por [canal], de [horario]. Fuera de ese horario: [alternativa]." | "Podés hablar con [equipo] por [canal], de [horario]. Fuera de ese horario: [alternativa]." | "You can reach [team] by [channel], [hours]. Outside those hours: [alternative]." |
| Action | **Ver cómo contactarlos** | **Ver cómo contactarlos** | **See how to reach them** |

The brackets show where the product's facts go. On the board, fill them with what the user told you (the team, its hours, its line) or with a realistic example marked "to confirm"; never leave brackets on a card. If you do not know the country, do not guess an emergency number: draw the button as **Llamar a emergencias** / **Call emergency services** with no number, mark it "to confirm: the number for this country", and list it as the first open question for the owner.

**Measure:** how often it fires and whether the route was opened - never the content of the message in ordinary analytics.
