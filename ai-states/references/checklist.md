# Review checklist

Go through this on the rendered board and the spec before delivering, and when reviewing someone else's AI feature. Report what fails ordered by harm to the user at this feature's stakes, not as a list of style remarks.

A line that asks for something the system does not have (a usage limit, a human service) is answered in the map with "does not apply" and the reason - not by inventing the thing.

## The map

- [ ] All fourteen states are in the map, each marked *yes*, *no* (with a reason) or *only if* (with the signal it depends on).
- [ ] For a review, each one also says how it stands today: *designed*, *generic* or *missing*.
- [ ] If the AI acts or works unattended, the twelve delegation states are in the map too.
- [ ] Interruption, memory, proactivity and cost are covered as notes, or marked not applicable.
- [ ] Where people can type freely, a sensitive moment has its card, its route and its named owner, and is marked for that owner's review.
- [ ] If people may use it on a phone, the go-ahead and at least one "no" state were checked at phone width.
- [ ] The stakes are stated, and the states that high or medium stakes require are present.
- [ ] Every trigger names a real signal. Signals that do not exist yet are listed as *to build*; signals you could not confirm as *to confirm*.

## Failure modes

- [ ] Each failure in `failure-modes.md` that can happen here has a named defence, or a reason it cannot happen.
- [ ] The silent ones were looked at first: a fluent wrong answer, an omission, a partial result that looks whole.
- [ ] Checking an answer costs less than redoing the work: the user can get from a claim to its basis in one press.
- [ ] If the AI reads content it did not write (documents, web pages, e-mails), text inside that content cannot make it act.

## Before and during

- [ ] The first screen says what it does, on what, and its main limit.
- [ ] The examples are real tasks for this product, pressable.
- [ ] The user sees what context will be used before sending.
- [ ] No bare spinner past two seconds; past ten there is a way to stop or leave.
- [ ] Progress text names real steps, or is honestly generic.
- [ ] A clarification is one question with options.
- [ ] Anything with an effect outside the conversation shows exactly what will happen before it happens.
- [ ] The confirm button names the action; irreversible actions say so.

## Answer

- [ ] The answer shows what it is based on, in proportion to the stakes.
- [ ] Sources sit next to what they support and can be opened at the passage.
- [ ] A partial answer says what is missing before giving what there is.
- [ ] Uncertainty is stated in words about something specific; no percentages, no blanket hedging.
- [ ] The next actions (copy, edit, apply, regenerate) are next to the answer.
- [ ] Regenerating does not destroy the previous result.

## The four "no"s

- [ ] Doesn't know, can't, won't and broke each have their own message and their own next step.
- [ ] "Doesn't know" and "won't" do not use the error style or the word "error".
- [ ] Every "no" has something to press.
- [ ] "Broke" covers the failures this system has: at least a temporary failure and being offline, plus a usage limit and a too-long input where those exist.
- [ ] After any failure, what the user gave and the previous result are still there.
- [ ] The message stays where the answer would have been, not in a toast that disappears.
- [ ] A second failure offers something other than a third retry.

## After

- [ ] Correcting or disliking an answer produces a visible result, and the copy is honest about what it changes.
- [ ] A person can be reached where a human service exists; the message says who, with what context, and when.
- [ ] The person receiving a handoff gets the question, what the AI answered and why it was handed over.

## Delegation (when it acts)

- [ ] The autonomy level is stated, and the permission table says what it does without asking, what it asks first, and what it never does.
- [ ] Irreversible or costly actions always ask; reversible, cheap ones do not.
- [ ] While it works, the user can see what it is doing, pause it and stop it - and stopping says what is kept.
- [ ] A request for a decision can be understood without the rest of the run, comes with a recommendation, and says what happens if nobody answers.
- [ ] The handback says what was done, what was not, what was not verified and where to look first - with links to the evidence.
- [ ] Many changes are grouped and ranked by risk; there is no blind "accept all".
- [ ] Every action in the log can be undone, or says that it cannot.
- [ ] A run that fails while the user is away stops safely, reports where it stopped and can be resumed.
- [ ] What it learned or was permitted permanently is visible in one place and can be removed.
- [ ] Anything it sends to other people says who it is from, and the user saw it first when the stakes ask for that.

## Test and measure

- [ ] `scripts/check_board.py` reports nothing to fix.
- [ ] Every button on the board leads to a screen, or its screen is marked as an end; you played the main path and one failure path in the flow player.

- [ ] There is one test input for each state that applies, including one that plants an instruction in the content when the AI reads content.
- [ ] Each state names the event to log, so the team can see how often it happens.

## Copy

- [ ] Each message: what happened, why if useful, what to do - understandable from the first part alone.
- [ ] One register and one voice across all states, matching the rest of the product.
- [ ] First person only where an assistant is speaking; a button or a panel speaks in the product's impersonal voice.
- [ ] No feelings claimed, at most one apology, no blame on the user.
- [ ] Buttons are verbs that name the action; **Regenerar** and **Reintentar** are not mixed up.
- [ ] No placeholder text anywhere on the board. Realistic example values (a name, a ticket number, a section of the product) are fine when they are listed as examples in the spec.

## The board

- [ ] The coverage strip matches the map.
- [ ] One card per state that applies; the states that do not apply are in the map with their reason.
- [ ] Each card shows the real component in that state, on the feature's real surface - not a chat bubble for a feature that is a button.
- [ ] Each card has its trigger.
- [ ] No state is told by colour alone.
- [ ] The board's own words are in one language, the one the team works in; the copy is in the product's.
- [ ] The board agrees with itself: what one card promises (the sections of a summary, a button, a limit) another card delivers; the answer card follows the rules the other cards set; counts and numbering match between the board, the spec and your message.
- [ ] Copy that states a fact you assumed (who can see a conversation, opening hours, a limit) carries a visible "to confirm" on its card, not only in the spec.
- [ ] The board reads at a glance: someone who looks only at the cards understands what the feature does in every moment.
- [ ] You looked at the rendered image, not only the source: nothing overflows, overlaps or sits empty.

## Accessibility

- [ ] Streaming and new states are announced without stealing focus.
- [ ] Icon-only buttons have names.
- [ ] Motion in the working state respects reduced-motion settings.
- [ ] Text contrast holds in every state, including disabled and muted ones.
