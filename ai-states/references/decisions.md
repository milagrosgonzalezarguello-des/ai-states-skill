# Decisions, worked

The calls that two careful designers would make differently unless they agree on a rule. Use these defaults so the same feature gets the same design every time. Depart from one only when the brief gives a reason, and say so in the spec.

## Severity

| Gap | Rating | Why |
|---|---|---|
| A partial or empty result that looks complete (a scanned file summarised as two lines, an answer from 40 of 60 pages with no mark) | **Critical** | Serious and silent: nobody checks what looks finished. |
| Sources exist in the backend but are not shown, on a medium or high stakes answer | **Critical** if people act on the answer without checking (legal, money, health, policy); **Major** otherwise | Checking costs as much as redoing, so it is either skipped or the feature saves nothing. |
| One generic error for every failure | **Major** | Visible, but users retry things that will never work and lose time. |
| A bare spinner on every request, over 10 s | **Major** | Hits every use (the frequency rule). |
| A bare spinner on rare or short waits | **Minor** | |
| Missing "not found" state, the AI answers anyway | **Critical** at high stakes, **Major** otherwise | A fluent answer with nothing behind it. |
| A planted instruction could make it act, not observed | **Major · to test** | One level below observed, with the test that would confirm it. |
| Disclaimer under every answer | **Minor** | Noise, not harm - unless it is the only defence, then rate the missing defence. |
| No first-use description | **Minor** | |
| Thumbs that change nothing visible | **Minor** | |

When two gaps tie, the one the user cannot detect goes first.

## Stop

- **Stop keeps what is done.** A long job that is stopped shows what it finished as a partial result, marked as partial (state 7). It never discards work silently, and never shows the part as if it were the whole.
- **Exception:** if a part cannot be shown honestly (the parts depend on each other and a half result would mislead), Stop discards it, and the message says so: "Se detuvo. No se guardó un resumen a medias porque estaría incompleto."
- Stop never undoes actions already taken. For an agent, Stop halts new actions and lists what was already done, with its undo (D10).

## Waits

- No product time known: indicator after 1 s, steps after 2 s, "taking longer" plus a way to leave after 10 s.
- Product time known ("3 to 12 s"): steps after 2 s; "taking longer than usual" only after the usual maximum.
- Stop is available from the first moment a wait is longer than about 2 s.

## Regenerate or not

- Writing, ideas, tone: **Regenerar**, and the previous version stays reachable.
- Facts, rules, data, policy: no Regenerate. Offer **Reformular**, the source, or a person. An answer about a rule must not change because it was asked twice.

## Confirm or undo

| The action | Default |
|---|---|
| Reversible, cheap, inside the product (draft, label, match) | Do it, show it, offer undo. |
| Reversible only for a while (scheduled payment, undo-send window) | Ask first, with the deadline in the button's sentence. |
| Irreversible, or goes to other people (send, pay, delete, publish) | Ask first, with the exact content. Never "OK". |
| The user can earn a standing permission for it | Only for reversible actions or for-a-while actions with a long window; it expires; it is visible in one place (D11). Sending to other people stays "asks first". |

In an example on the board, show the default first. If you also show an earned permission, label it as a setting the user turned on.

## Prototype wiring

| Screen is reached by | Wire it with |
|---|---|
| A button the user presses | `data-go` on that button |
| Something the user types (a question that lands in "not found", a sensitive message) | a `.sim` row on the screen before it ("Then the user asks about..."), or `data-entry` if no screen comes before |
| Something the system decides (the answer arrives, a failure, a limit) | a `.sim` row on the waiting screen |
| A notification or a run that failed overnight | `data-entry` |
| A link that leaves the product (rules page, help centre) | a plain link `<a>`; it is not a flow step |

## Which "no"

| Situation | State |
|---|---|
| In scope, nothing found | 9 Doesn't know |
| Out of scope for this feature, someone else can | 10 Can't |
| The input cannot be processed (scan, password, format) | 10 Can't |
| A rule or policy blocks it | 11 Won't |
| The product rejects an action for a business reason (no balance, date taken) | A screen of state 5, with the system's reason |
| The system failed | 12 Broke |
| The user writes about harm, distress or an emergency | Sensitive moment - never any of the above |

## Coverage labels

| Situation | Coverage cell | Map, Applies |
|---|---|---|
| Designed, every signal exists | designed | yes |
| Designed, depends on a signal to confirm or to build | designed · signal to confirm (`if`) | yes, and the signal in the signals table |

The summary line then reads: "N states apply and are designed; M of them depend on a signal to confirm or build (see the last table); K do not apply."
| Applies only if a signal turns out to exist | to confirm (`if`) | only if |
| Replaced by a delegation state | covered by D4 (`covered`) | no - covered by D4 |
| Sensitive moment | designed · owner review (`review`) | yes · owner review |
| Cannot happen here | not applicable (`na`) | no, with the reason |
| Applies, left for the full version (quick mode) | for the full version (`later`) | yes · not drawn yet |

## Copy that states facts

Example people, companies and products are fictional: never a real celebrity, team, brand or company in example copy, even to show what a rule blocks ("a famous footballer", "a club crest" instead). Numbers, names, hours, prices, phone numbers: use what the brief gave. Otherwise use a realistic example marked "to confirm" on the card - except phone numbers and emergency numbers, which are never invented: draw the button with its label and no number.

## Languages

The board and spec are in the language the user wrote in. The product copy is in the product's language and register if the brief gives them; if not, the same language as the user, in the product's most likely register (English: "you"; Spanish: tú unless the brief or the market says usted or vos), marked as assumed.

## Addressing the team

The user's own register. If their message gives no clue, neutral Spanish with "ustedes"; never "vosotros" unless they used it.
