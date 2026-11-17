# Failure modes and severity

A system error announces itself. The failures that hurt users of AI features are the ones that look like success. Go through this list for every feature: each row is a way the model fails, whether the user can tell, and which state or pattern is the defence.

## How the model fails

| Failure | What happens | Can the user tell? | Defence |
|---|---|---|---|
| **Confidently wrong** | A fluent, well-formatted answer that is false | No | Sources next to claims (6); cheap verification; "not found" as a real state (9) so it has an alternative to inventing |
| **Omission** | A summary or extraction that leaves out the thing that mattered | No | Say what was covered and what was not (7); structured output with explicit "not found" lines; page or item coverage |
| **Stale** | Correct once, out of date now | Rarely | The date the information is current to (6); unsure when older than a threshold (8) |
| **Misread intent** | A good answer to a different question | Sometimes | Restate the request when ambiguity changes the result (4, D1); show what was used (2) |
| **Overreach** | It does more than asked: edits beyond the selection, sends when asked to draft | After the fact | Plan and limits (D1, D2); go-ahead (5); autonomy level per action; undo (D9) |
| **Under-delivery** | It stops early and reports success | No | Handback that separates done, not done, not verified (D7) |
| **Inconsistent** | The same question gets a different answer tomorrow | When they notice | Keep versions on regenerate; stable structure; for decisions, pin the result that was used |
| **Lost context** | It forgets the start of a long conversation or task | Late | Say when context is full and offer a summary or a fresh start (12); show what it is working from (2) |
| **Follows planted instructions** | Text inside a document, e-mail or web page tells it what to do, and it obeys | No | Content is data, never commands: actions suggested by content the agent read need the user's go-ahead (5, D5); show where an instruction came from |
| **Wrong memory** | It applies a remembered preference that is wrong or no longer true | When shown | Show when memory was used; one place to edit it (D11) |
| **Runs away** | It loops, repeats an action, or keeps spending | Late | Step, time and spend limits with their own messages (D10) |
| **Uneven quality** | It works better for some users, languages or cases than others | Not individually | Test with the real range of users and languages; route the weak cases to a person (14) |

Polish makes all of these worse. A hesitant answer invites checking; a confident, cleanly formatted one does not. Do not make output look more certain than the system is.

## Calibrated trust

The aim is not that users trust the feature. It is that they trust it **as much as it deserves, case by case**.

- **Over-trust** is accepting without looking. It grows with fluent output, with long streaks of correct answers, and with one-press acceptance. Counter it where a mistake matters: put the evidence in the path, not behind a link; ask the user to confirm the two facts that carry the decision; never offer "accept all" over unsorted work.
- **Under-trust** is redoing everything by hand. It grows after one unexplained error. Counter it by making the basis visible and by being honest about limits, so the user learns where it is reliable.
- The practical test: **checking must cost less than redoing.** If verifying a summary means rereading the contract, the feature saves nothing; if each sentence opens the page it came from, it does.
- Friction is a tool. Add it where the stakes are high and remove it where they are low; the same confirmation everywhere protects nothing.

## Severity: ordering findings in a review

Score each gap on three questions and order by the result. This is what "ordered by harm" means.

| Question | Low | High |
|---|---|---|
| **How bad is it when it happens?** | The user loses a minute | Money, legal exposure, safety, something sent to others, something that cannot be undone |
| **Can the user tell it happened?** | It is obvious (an error message) | It looks like success |
| **How often?** | An edge case | The normal path, or a common input |

- **Critical:** serious and silent. A wrong or incomplete result presented as complete; an action taken without the user seeing what it would do. These come first whatever their frequency.
- **Major:** serious but visible, or silent and frequent. The user is stopped with no way forward; work is lost; a generic error hides a cause the user could fix.
- **Minor:** visible, recoverable, occasional. Wording, missing examples, a loader without steps on a short wait.

Two cases the three levels do not settle by themselves:

- **Something that hits every use** moves up one level: a bare spinner for a minute on every request is major, not minor.
- **A risk you have not seen happen** (a planted instruction, an omission the model could make) is rated one level below what it would be if observed, and labelled *to test*, with the test that would confirm it. Otherwise every review ends with five criticals and the real one is lost among them.

Silent beats loud: a bare spinner is annoying, but an empty summary of a scanned contract that looks like a summary is dangerous. Reviews that lead with the spinner have the order wrong.

## Sensitive moments

Some inputs are not requests for the feature at all: a user in distress, describing harm, or in an emergency. A product for work rarely designs for this and should, briefly: recognise it, drop the task framing, give the real resource (a person, a number, a service) and do not carry on with the summary. Decide with the team who owns this and what the route is; do not improvise copy for it. On the board this is a note with the trigger, the route and the owner to be named - the one place where a card without final copy is right - and an open question in the spec.
