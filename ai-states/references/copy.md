# Writing for AI states

The words in these states are read at the worst moment: the user is waiting, confused or annoyed. They scan, they do not read.

## The order of a message

**What happened, why (if it helps), what to do.** In that order, and the first part alone must make sense.

- "No encontré esa política. Pruebe con otro nombre o consulte a RR. HH."
- Not: "Para poder brindarle una respuesta adecuada, sería necesario contar con..."

The action goes on a button, with a verb that names it: **Reintentar**, **Reformular**, **Hablar con una persona** - not **OK**, **Aceptar** or **Cerrar** as the only choice.

## Say which "no" it is

The user decides what to do next from the first words, so the four must not sound alike.

| State | Starts like | Never |
|---|---|---|
| Doesn't know | "No encontré..." / "I couldn't find..." | "Error" |
| Can't | "No puedo ver / hacer..." / "I can't..." + where it can be done | "No entiendo su consulta" |
| Won't | "No puedo ayudar con..." / "I can't help with..." + what it can do | A lecture, or pretending not to understand |
| Broke | "No pude generar..." / "Couldn't..." + input is safe | "Algo salió mal" alone, or a code |

## Be specific

Each of these is a real improvement the user can act on:

| Vague | Specific |
|---|---|
| Procesando... | Leyendo 3 archivos... |
| No se pudo completar la solicitud. | No pude leer *contrato.pdf*: está protegido con contraseña. |
| Límite alcanzado. | Alcanzó el límite de 50 consultas de hoy. Se renueva mañana a las 9:00. |
| La IA puede cometer errores. | Revise los montos antes de enviar: los calculé a partir del PDF. |
| Intente más tarde. | El servicio no responde. Su borrador quedó guardado; reintente en unos minutos. |

Only be specific about what the system knows. "Leyendo 3 archivos" needs the system to report that step.

## The AI's voice

- **First person only if there is someone speaking.** An assistant in a chat can say "No encontré". A button, a panel or a background job has no "I": write it in the product's impersonal voice - "No se pudo leer el archivo", "Resumen generado a partir de 42 de 60 páginas", "Couldn't read this file". Do not invent a persona to carry a message.
- **First person for actions, not feelings.** "No encontré", "Usé", "Voy a enviar" are clear about who did what. "Me encantaría", "Lamento profundamente", "¡Qué buena pregunta!" claim feelings and add reading.
- **One apology, only when the system failed.** Not for not knowing, not for a rule, not three times.
- **No blame.** "No entendí la fecha" rather than "Ingresó una fecha inválida". For system failures the subject is the system.
- **No fake modesty and no fake confidence.** "Soy solo una IA" tells the user nothing about this answer; "Definitivamente" on a guess is worse.
- **Same voice as the rest of the product.** The AI is a feature of the product, not a guest with its own personality, unless the product decided otherwise.
- **Humour only where the product already has it, and never in the "no" states.** A joke on an error reads as not caring.

## Uncertainty in words

Say what is uncertain and why, once, next to the thing it applies to.

- Good: "El dato es de 2023; puede haber cambiado."
- Good: "Las dos fuentes no coinciden. Le muestro ambas."
- Bad: "Es posible que quizás..." in every sentence.
- Bad: "87% de confianza."

A general disclaimer belongs once, at first use. A specific warning belongs on the specific answer.

## Working states

- Name the real step if the system reports it; otherwise a plain "Generando la respuesta..." is honest.
- Present progressive, no exclamation marks, no countdown the system cannot keep.
- For long work, give the user something true about time: "Suele tardar entre 1 y 2 minutos."

## Buttons and labels

- Verb first, the object when it is not obvious: **Enviar a 14 personas**, **Deshacer**, **Ver fuente**.
- **Regenerar** / **Regenerate** for another answer to the same request; **Reintentar** / **Try again** after a failure. They are different actions; do not use one word for both.
- **Detener** / **Stop**, not **Cancelar**, while it is generating: cancel suggests the request is discarded, stop keeps what there is.
- Feedback: **Útil** / **No útil**, or icons with those names as accessible labels.

## Register

Whichever the product uses, keep it through every state.

| | Formal (usted) | Informal (vos) | Informal (tú) | English |
|---|---|---|---|---|
| Doesn't know | No encontré eso. Pruebe con otras palabras. | No encontré eso. Probá con otras palabras. | No encontré eso. Prueba con otras palabras. | I couldn't find that. Try different words. |
| Broke | Su pregunta quedó guardada. | Tu pregunta quedó guardada. | Tu pregunta quedó guardada. | Your question is saved. |
| Go-ahead | ¿Envío este correo? | ¿Mando este correo? | ¿Envío este correo? | Send this e-mail? |

## Reports from an agent

A handback is read by someone who was not watching. Write it like a good handover note.

- The outcome first, in one line: "Concilié 212 de 215 facturas."
- Then what was not done and why, before the detail of what was.
- Facts, not adjectives: "Envié 14 correos" rather than "Todo salió perfecto".
- Say what was checked and what was not: "No verifiqué los montos en moneda extranjera."
- A request for a decision stands alone: what it was doing, what it found, the options, its recommendation, what happens meanwhile.
- No emoji as status. A check mark on a half-failed task is a lie in one character.

## Length

A state message is one or two short sentences. If it needs more, the extra goes behind **Ver detalle**. The exception is state 5 (go-ahead), where the preview must be complete.

## Accessibility of the words

- Streaming text is announced politely, in chunks, not character by character; the final answer is announced once.
- A state is never told by colour alone: the words say which state it is.
- Buttons with only an icon (copy, regenerate, thumbs) have a text name.
- Focus goes to the new message on errors and on requests for confirmation, and stays put while an answer streams.
