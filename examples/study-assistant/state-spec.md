# Study Assistant: state spec

Companion to `board.html` (the state board, playable with **Try the flow**) and `state-tests.json`.

## 1. What we know and what we assumed

**Given:** a chat in the student portal for about 12,000 students, many on phones. It answers questions about courses, deadlines and regulations from the official documents. Students can type anything. Student Services has a counselling team (Mon to Fri, 9:00 to 17:00). There is a 24/7 campus security line.

**Assumed (each one marked "to confirm" on the board):**

| # | Assumption | Changes |
|---|---|---|
| A1 | The product's copy is in English, plain and friendly, addressing the student as "you". | Every screen |
| A2 | It answers only. It cannot see grades, timetable or the student record, and it cannot register, pay or submit anything. | 1, 10; state 5 does not apply |
| A3 | Retrieval-augmented generation over an index of official documents, with a score per passage and metadata (title, section, page, academic year, date current to). | 6, 7, 8, 9 |
| A4 | The answer streams; retrieval can emit step events. | 3 |
| A5 | The portal can pass the signed-in student's level and faculty. | 2, 4 |
| A6 | Student Services handles general enquiries through a portal enquiry system ("My Enquiries"), Mon to Fri 9:00 to 17:00, replying within about 2 working days. | 14 |
| A7 | The country, and so the emergency number, is unknown. No phone number is drawn anywhere. | S |
| A8 | Whether a 24-hour listening or crisis line is recommended by Counselling is unknown. | S |
| A9 | Who can read conversations and how long they are kept is unknown. | 1, S |
| A10 | No per-student usage limit and no cost to students. | 12, Cost |

**Stakes:** medium overall; high for deadlines and rules that affect progression (resits, extensions, extenuating circumstances, attendance, academic integrity), because students act on them and a wrong date can cost a year. For a read-only feature this means evidence in the path (the source next to each claim, the date the documents are current to), a clear "not found", and a route to a person. There is nothing to confirm before acting, because it does not act.

**Surface:** chat. Chat is right here: questions are open-ended and need follow-ups. The example questions on first use do the work a button would. Every screen is drawn at phone width; sources open as a sheet over the chat.

## 2. State map

| # | State | Applies | Why / signal |
|---|---|---|---|
| S | Sensitive moment | Yes · owner review | Free text from 12,000 students under exam pressure. Classifier to build. Owners: Counselling team lead and Campus Security. |
| 1 | First use | Yes | Empty conversation. |
| 2 | Composing | Yes | Scope chip from portal (A5). |
| 3 | Working | Yes | Streaming, step events (A4). |
| 4 | Needs a clarification | Yes | Rules differ by level and faculty. |
| 5 | Needs my go-ahead | No | It takes no actions. Sending a question to Student Services is previewed inside card 14. |
| 6 | Answer | Yes | Passage scores and metadata (A3). |
| 7 | Partial answer | Yes | Per-part retrieval result, to build. |
| 8 | Unsure | Yes | Document dates (to confirm) and conflict check (to build). |
| 9 | Doesn't know | Yes | Retrieval threshold, to confirm. |
| 10 | Can't do that | Yes | Intent class "own record or action", to build. |
| 11 | Won't do that | Yes | Refusal flag, to confirm; academic-integrity rule. |
| 12 | Broke | Yes | Typed errors, to build; offline is frequent on phones. |
| 13 | Corrected | Yes | Disagreement detection and Not helpful. |
| 14 | Handed to a person | Yes | Hand-off to the enquiry system, to build. |
| D1-D12 | Delegation | No | Not an agent: one question, one answer, no tools that change anything. |

Coverage: 13 states apply (8 designed, 5 designed with a signal to confirm or build: 7, 8, 11, 12, 14), 1 does not apply (5), plus the sensitive moment, designed and waiting for owner review.

## 3. Failure modes and their defences

| Failure | Can happen here? | Defence |
|---|---|---|
| Confidently wrong (a wrong deadline) | Yes, the most harmful one | Source chip next to each claim, opening at the passage (6); "not found" as a real state (9); no Regenerate on facts |
| Omission (answers half a question) | Yes | Partial answer says what is missing first (7) |
| Stale (last year's handbook) | Yes, every September | Date current to on every answer (6); Unsure when the best source is from a previous year (8) |
| Misread intent (wrong level or faculty) | Yes | "Answering for" chip (2); one clarifying question (4) |
| Inconsistent (different answer when asked again) | Yes | No Regenerate on rules; Rephrase and Ask Student Services instead |
| Follows planted instructions | Low: the documents are official. Students can paste text | Answers only from retrieved passages; test T-inject |
| Lost context | Low: short conversations | Not designed separately; if it happens it is a 12 screen with a fresh start |
| Uneven quality (international students, other languages) | Yes | Test with non-native English; route to Student Services (14); see open question Q9 |
| A message about harm answered as a policy question | Yes | Sensitive moment (S), run before retrieval, fixed copy |
| Overreach, runs away, wrong memory | No | It takes no actions and keeps no memory across conversations |

## 4. States

### S. Sensitive moment (owner review: Counselling team lead and Campus Security)
- **Trigger:** a classifier on the student's message, run before retrieval and separate from the refusal flag, leaning toward catching too much. Categories: (a) thoughts of suicide, self-harm or not wanting to be alive; (b) danger or an emergency now (someone hurt, a threat, being followed); (c) sexual harassment, assault, stalking or abuse, including by staff or students; (d) severe distress or not coping; (e) threats to harm others; (f) low-severity figures of speech with a real question ("stats is killing me"). The variant is chosen by category and by whether Counselling is open. (to build: the classifier; to confirm: the categories, with the owners)
- **Shows:** a fixed card in the calm "support" style (not the error style), never generated. No sources, no answer, no Helpful / Not helpful, no Regenerate, no suggested questions. The composer stays enabled.
- **Copy (distress, in hours):** "What you're going through sounds really heavy, and you deserve to talk to a person about it." Routes, in this order: "If you might act on these thoughts or you're in danger now" **Call emergency services** · "Talk to the Counselling team today. Open now, until 17:00 (Mon to Fri, 9:00 to 17:00)" **See how to reach them**.
- **Copy (distress, out of hours):** same opening, ending "...about it tonight." Routes: emergency services · "Talk to someone now, any time of day. A free listening line, open 24 hours" **Call the 24-hour support line** · "Counselling team. Opens Monday at 9:00" **See how to reach them**. Campus Security is not offered as the route for distress (it is not a mental-health service), unless the owners decide otherwise.
- **Copy (danger or harassment):** "That sounds frightening, and it isn't something you should have to handle alone." Routes: "If you're in danger right now" **Call emergency services** · "Campus Security. Open 24 hours, every day" **Call Campus Security** · "Support with what has been happening. Counselling, Mon to Fri, 9:00 to 17:00" **See how to reach them**.
- **Copy (figure of speech + question):** "If things are getting too much, Counselling and urgent help are one tap away, any time." **Support and urgent help**, then a row: "Your question about the PSY2041 exam is still here." **Answer my question** (leads to a normal answer, state 6). The same "still here" row is added under any variant whose message also contains a question.
- **Permanent entry:** "Support and urgent help" in the chat header on every screen, whatever the classifier says. It opens a sheet: in danger or hurt right now (emergency services) · unsafe on campus (Campus Security, 24 hours) · need to talk tonight or at the weekend (24-hour listening line) · Counselling team, Mon to Fri 9:00 to 17:00 (**Book an appointment**, **Call Counselling**).
- **Actions:** call buttons as phone links; no numbers drawn until confirmed. Nothing is reported, opened or forwarded on the student's behalf; a sensitive message is never sent to Student Services through state 14 automatically.
- **Keeps:** the conversation; any real question in the message, one press away.
- **Goes to:** outside the product (a call), or back to the chat (the student can carry on).
- **Announces:** "Support options follow." once, assertively; focus moves to the card's first line, so a screen-reader user hears the acknowledgement before the routes.
- **Test:** T-S-distress-hours, T-S-distress-night, T-S-safety, T-S-figure-of-speech, T-S-model-down.
- **Measure:** `sensitive_card_shown` with category and variant, and `sensitive_route_opened` with the route. Never the message text in ordinary analytics. Watch: routes never opened; misses found only under the owners' governance.
- **Must still work when:** the model is down, a limit is reached, or retrieval fails. The card is static content served by the app.
- **Open questions for the owners:** Q1 to Q6.

### 1. First use
- **Trigger:** no messages in this conversation.
- **Shows:** a first assistant message, four example chips, a one-line accuracy note with the "Who can see this chat" link, the composer.
- **Copy:** "I answer questions about courses, deadlines and university rules, using the official documents for 2026/27. I show you where each answer comes from." / "I can't see your grades, timetable or student record, and I can't register you for anything." / "Answers can be wrong; check the source before you act on a deadline." Chips: "When is the resit deadline for Semester 1?" · "What happens if I fail a module?" · "How do I apply for an extension?" · "How many credits do I need to pass the year?"
- **Actions:** the chips; **Support and urgent help** in the header.
- **Goes to:** 2, 3, 4.
- **Announces:** the scope line once; focus in the composer.
- **Test:** T01. **Measure:** `first_use_shown`; chip pressed vs typed first message.
- **Open question:** what "Who can see this chat" says (Q7). Replace the chips with the most frequent real questions after launch.

### 2. Composing
- **Trigger:** the student is typing.
- **Shows:** the "Answering for: Undergraduate · Faculty of Science · 2026/27 · Change" chip (from the portal, A5), the sources searched, the length limit.
- **Copy:** "Searches: Academic Regulations, Module Catalogue, Academic Calendar. Up to 1,000 characters." Over the limit: "1,240 of 1,000 characters. Shorten it to send."
- **Actions:** **Send**; **Change** on the scope chip.
- **Keeps:** the typed text, always, including over the limit.
- **Goes to:** 3.
- **Test:** T02. **Measure:** `input_too_long`; scope changed.

### 3. Working
- **Trigger:** question sent, answer not complete. Under 1 s nothing; from 2 s the steps and **Stop**; after 10 s "taking longer than usual". If the usual time is known, use its maximum instead of 10 s.
- **Shows:** steps reported by retrieval ("Searching the Academic Regulations", "Reading 3 sections", "Writing the answer"), then the streamed answer. **Stop** sits where **Send** was.
- **Copy (slow):** "This is taking longer than usual. You can leave this page; the answer will be here when you come back." (to confirm: the server finishes the answer if the page closes)
- **Copy (stopped):** tag "Stopped · incomplete" over the text produced so far; no sources, no feedback.
- **Actions:** **Stop**; after stopping, **Try again** and **Edit question**.
- **Keeps:** the question and any text produced.
- **Goes to:** 6 to 12, or the stopped screen.
- **Announces:** "Searching" once, politely; the finished answer once; focus stays in the composer.
- **Test:** T03. **Measure:** time to first token, time to complete, `answer_stopped` by wait time.

### 4. Needs a clarification
- **Trigger:** the retrieved rules differ by a value the question does not give (level, faculty, year of entry) and the scope chip does not set it.
- **Copy:** "The rules are different for each level of study. Which one are you on?" Chips: Undergraduate · Postgraduate taught · Research degree; or type.
- **Keeps:** the original question; the choice fills the scope chip for this conversation.
- **Goes to:** 6.
- **Test:** T04. **Measure:** `clarification_asked`, answered, abandoned.

### 6. Answer
- **Trigger:** complete answer, each claim tied to a passage above the threshold, no conflict or age flag.
- **Shows:** the answer itself on the first line (the deadline, the rule); a source chip after each claim that opens a sheet with the quoted passage and **Open the full document**; "From documents current to 1 September 2026."
- **Copy (example):** "**Register for Semester 1 resits by 22 January 2027, 17:00.** [Academic Calendar 2026/27, p. 4] You register in the portal under My Studies › Assessments. Late registration is only accepted with approved extenuating circumstances. [Academic Regulations, 7.3]"
- **Actions:** **Copy** · **Helpful** · **Not helpful** · **Ask Student Services**. No **Regenerate**: an answer about a rule must not change when asked again.
- **Goes to:** 13, 14, the next question.
- **Announces:** the answer once when complete; source chips are links named like "Source: Academic Calendar 2026/27, page 4".
- **Test:** T06, T-inject. **Measure:** `source_opened` per answer (how often students verify), copied, Not helpful.

### 7. Partial answer
- **Trigger:** a multi-part question where at least one part has no passage above the threshold. (to build: per-part result)
- **Copy:** "I found the resit dates but nothing on the cost of resits." Then "Dates: Semester 1 resits run 15 to 26 February 2027. [source]" and "Cost: not in the documents I can search."
- **Actions:** **Ask Student Services about the cost** · **See the fees page**.
- **Keeps:** the question and the part found.
- **Goes to:** 14, the next question.
- **Test:** T07. **Measure:** `answer_partial` by topic (finds missing documents).

### 8. Unsure
- **Trigger:** two passages give different values for the same rule, or the best passage is from a previous academic year. (to confirm: dates in the index; to build: conflict check)
- **Copy:** "Two documents say different things. Check with your department which one applies to you." Both values, each with its source; "The handbook is from last year."
- **Actions:** **Ask Student Services** · **Helpful** · **Not helpful**.
- **Goes to:** 14.
- **Test:** T08. **Measure:** `answer_unsure` by document pair; send the pairs to the document owners.
- **Never:** a confidence percentage.

### 9. Doesn't know
- **Trigger:** in scope, the sensitive check did not fire, no passage above the threshold. (to confirm: threshold)
- **Copy (first miss):** "I couldn't find anything about dogs or pets in the library in the 2026/27 regulations, policies or module catalogue."
- **Copy (second miss):** "I didn't find that either. Student Services can answer this; I can send them your question."
- **Shows:** answer style with a "Not found" tag, not the error style.
- **Actions:** **Rephrase** · **Ask Student Services** · **Search the documents myself**; on the second miss **Send to Student Services** is primary.
- **Keeps:** the question, in the composer, editable.
- **Goes to:** 2, 14.
- **Announces:** "Not found. Options follow." politely; focus stays in the composer.
- **Test:** T09. **Measure:** `answer_not_found` by topic; a high rate on one topic means a missing document.
- **Open question:** can the index tell "no document" from "a document exists but is not indexed"?

### 10. Can't do that
- **Trigger:** the question needs the student's own record or an action (grades, timetable, registering, paying). (to build: intent class)
- **Copy:** "I can't see your grades. They're in My Studies › Results."
- **Actions:** **Open My Studies › Results** · **Ask how grades are calculated**.
- **Goes to:** the portal page, or 6.
- **Test:** T10. **Measure:** `answer_cant` by request type.

### 11. Won't do that
- **Trigger:** refusal flag, or the academic-integrity rule (writing or completing assessed work). (to confirm: refusal flag separate from an empty answer)
- **Copy:** "I can't write assessed work for you. I can tell you the word count rules, the submission deadline, or what the Academic Integrity Policy allows."
- **Shows:** "Not allowed" tag, rule style; no lecture, no accusation.
- **Actions:** two chips with nearby questions; **This shouldn't have been blocked**.
- **Test:** T11. **Measure:** `answer_refused`; false-block reports.

### 12. Broke
- **Trigger:** typed error from the service. (to build)
- **Copy (timeout or unavailable):** "Sorry, I couldn't get an answer just now. Your question is saved." **Try again**.
- **Copy (offline):** "Your phone lost its connection, so the question wasn't sent. It's saved here; send it again when you're back online." **Send again**.
- **Copy (second failure):** "The assistant isn't responding right now. The rules on changing modules are in the Academic Regulations, or Student Services can answer." **Open the Academic Regulations** · **Ask Student Services** · **Try again later**.
- **Copy (daily limit, only if one exists):** "You've used today's 40 questions. You can ask again from 00:00." (example numbers)
- **Shows:** in the thread where the answer would be, never a toast.
- **Keeps:** the question and every earlier answer.
- **Goes to:** 3, 14.
- **Announces:** the message assertively; focus moves to it.
- **Test:** T12a, T12b. **Measure:** `answer_failed` by cause; retry success rate.
- **Note:** the sensitive card and the help sheet keep working during any failure.

### 13. Corrected
- **Trigger:** the student says the answer is wrong, or presses **Not helpful**.
- **Copy (disagrees):** "I checked again. The Academic Calendar 2026/27 says 22 January 2027, 17:00. [source] Your lecturer may mean a different deadline. If the calendar is out of date, report it and confirm with Student Services before you rely on either date."
- **Copy (after a report or Not helpful):** "Thanks. Your report went to the team that looks after the assistant's documents. It doesn't change answers in this chat." Optional reasons: Wrong date or fact · Didn't answer my question · Out of date.
- **Never:** adopting the student's date for a rule; "You're absolutely right"; "I'll remember that".
- **Goes to:** 14, the next question.
- **Test:** T13. **Measure:** `answer_disputed`, `answer_reported` by document; reports that lead to a document fix.

### 14. Handed to a person
- **Trigger:** the student asks for a person, presses **Ask Student Services**, or a second not-found. (to build: hand-off to the enquiry system)
- **Copy (before):** "I'll send this to Student Services with your name and student number:" Preview: the question; what the assistant found.
- **Actions (before):** **Send to Student Services** · **Edit question** · **Don't send**.
- **Copy (after):** "Sent to Student Services, reference SS-48213. They usually reply within 2 working days, as a message in My Enquiries. They work Monday to Friday, 9:00 to 17:00." (reference, reply time and hours are examples, to confirm)
- **Adviser side:** a ticket with the student, the question, why it was handed over, what the assistant answered, what it searched, and **Read the full chat**.
- **Announces:** the confirmation with its reference, politely.
- **Test:** T14. **Measure:** `handoff_sent`, turns before reaching a person.

## 5. Across all states

- **Interruption:** Stop keeps the text marked "Stopped · incomplete". Closing the page mid-answer: the answer finishes and is there on return (to confirm). A dropped connection is 12b.
- **Memory:** inside a conversation, the scope and earlier questions; nothing across conversations unless decided. Never "I'll remember".
- **Proactivity:** not applicable. Deadline reminders, if wanted, belong to portal notifications with their own opt-in.
- **Cost:** free to students. A daily limit, if any, is a 12 screen; the sensitive card and help sheet are exempt.

## 6. Signals the system must expose

| Signal | Used by | Status |
|---|---|---|
| Sensitive-message classifier, before retrieval, with categories | S | To build |
| Fixed card content served without the model | S, 12 | To build |
| Retrieval score per passage, and the threshold | 6, 7, 9 | To confirm |
| Document metadata: title, section, page, academic year, date current to | 6, 8 | To confirm |
| Step events from retrieval; streaming | 3 | To confirm |
| Result per part of a multi-part question | 7 | To build |
| Conflict between passages on the same rule | 8 | To build |
| Intent class "own record or action" | 10 | To build |
| Refusal flag, separate from an empty answer | 11 | To confirm |
| Error type: timeout, model unavailable, offline, daily limit | 12 | To build |
| Level and faculty of the signed-in student | 2, 4 | To confirm |
| Hand-off to the Student Services enquiry system, returning a reference | 14 | To build |

## 7. Test script

`state-tests.json` has 20 tests: five for the sensitive moment (in hours, out of hours, safety, figure of speech, model down), one for each other state, two for Broke, and one planted instruction. Run them with the skill's `run_tests.py`:

    python run_tests.py state-tests.json --url <assistant endpoint>

or `--cmd "<command that takes the input and prints the answer>"`. Tests whose setup needs a condition (offline, a timeout, the model down, the clock set to Saturday night) are listed to run by hand. They check that the assistant lands in the right state, not that its answers are correct; accuracy needs its own evaluation set built from real student questions.

## 8. Open questions

For the owners of the sensitive moment (Counselling team lead, Campus Security, and whoever owns safeguarding):

- **Q1.** The emergency number for the country.
- **Q2.** Out of hours, which 24-hour listening or crisis line Counselling recommends for students, and its number. If there is none, what the out-of-hours route for distress is (it should not default to Campus Security).
- **Q3.** Campus Security's number, and what to say it offers (an escort, a response on campus).
- **Q4.** How students reach Counselling: booking link, phone, drop-in.
- **Q5.** The categories the classifier must catch and the order of routes for each; who reviews misses, under what governance.
- **Q6.** Whether sensitive conversations are stored and who can read them, and whether the card should say so. Until answered, the card says nothing about it.

For the product and engineering team:

- **Q7.** Who can read assistant conversations and for how long (for "Who can see this chat").
- **Q8.** Does the portal pass level and faculty? Is there a per-student daily limit? Does retrieval expose scores, dates and step events?
- **Q9.** Is the product English only? Students may write in other languages; decide whether it answers in their language or says it answers in English.
- **Q10.** Student Services' hours, enquiry channel and reply time.

## 9. Example values (do not ship as fact)

Course code PSY2041; Academic Calendar 2026/27 p. 4; Academic Regulations 7.3; resit registration 22 January 2027, 17:00; resits 15 to 26 February 2027; documents current to 1 September 2026; Attendance Policy 80%, Psychology Handbook 2025/26 75%; reference SS-48213; reply within 2 working days; 1,000-character limit; 40 questions a day; BSc Psychology, Faculty of Science.
