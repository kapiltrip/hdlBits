# HDLBits Attempt 2: LinkedIn Posting Plan and Ideas

**For Kapil's morning review.** A proposed 10-day series, with captions, document choices, visual ideas and a preparation checklist. Nothing has been posted or scheduled.

## The idea I would lead with

**“HDLBits, second pass: the questions behind the code.”**

Use the completion milestone to introduce the work, then let each post explain one question from your second attempt. Your strongest material is the connection between an original doubt, the hardware behavior, and the explanation you saved. The PDFs give readers something useful to study after the post.

Keep the voice straightforward: “This confused me. Here is the trace that helped.” Show your development as a VLSI student through concrete reasoning about clocks, state, storage and boundaries. Avoid claiming mastery or describing these exercises as a complete verification project.

**Recommended format:** one launch post, eight focused learning posts, and one closing post. Each has one visual or document, one takeaway and one question that invites a technical answer.

## What is ready, and what needs tomorrow's check

The repository snapshot reviewed for this plan is commit `c359d76`. Its [Attempt 2 README](HDLBits%20Attempt%202/README.md) records **155 Done and 23 Pending out of 178 tracker entries**, dated 7 September 2026. It contains **12 study PDFs**, and the [document review](HDLBits%20Attempt%202/DOCUMENT_REVIEW.md) records **45 document links** from the tracker. Those links are not 45 separate documents.

Before using a completion announcement, finish the remaining work and confirm the updated tracker against HDLBits. The current record lists entries 141, 145, 151 and 159–178 as pending. Describe the count as entries in your revision tracker; do not assume it is the current total number of exercises on the platform.

The captions below are drafts for you to review against your own experience. The launch caption deliberately works without an unverified completion claim. After finishing, you can replace its first sentence with: **“I've completed my second pass through the 178 entries in my HDLBits revision tracker.”**

## Document indexing update

All 12 full PDFs now have consistent reading covers, clickable contents, bookmarks and page counters. Use the [topic and tracker-entry index](HDLBits%20Attempt%202/DOCUMENT_INDEX.md) to find a precise explanation. The source-page references below reflect the new pagination: Day 8 wire/reg pages are 2–3; Day 9 latch pages are 2–4; the 1101 recognizer is on pages 5–6. Posting-day numbers remain independent of note numbers.

## How to share the documents alongside the posts

Use a short PDF document post when a topic benefits from several pages. Give it a clear reader-facing title, such as **“Why a Verilog Loop Does Not Capture Eight Serial Bits.”** Keep the existing repository filenames and links stable.

For a focused post, select relevant pages or prepare a small standalone excerpt with enough context to understand them. Label it “Selected pages from my Attempt 2 notes,” preserve source references and page numbers, and link to the full original PDF. The page ranges below are source material, not instructions to upload every page listed.

For simpler topics, one readable image and a link to the full notes are enough. Put the useful GitHub link in the caption so the resource is available even when the post is scheduled. Do not make readers comment or message you to obtain it.

For the launch and final post, link to the [Attempt 2 reading index](https://github.com/kapiltrip/hdlBits/tree/main/HDLBits%20Attempt%202). This gives readers the PDFs, tracker and explanation of the checks in one place.

## The 10-day sequence

**Day 0 is the day you finish and review the material. Day 1 is the following day.** This avoids committing to calendar dates before completion. Use one post per day for ten days. A practical starting slot is **7:30 PM IST**, chosen so you can return to replies; it is a planning choice, not a claim about the best time for LinkedIn reach.

| Day | Post topic | What readers see | Discussion question |
|---|---|---|---|
| 1 | Why I did a second pass | Series cover and an overview of the notes | Which RTL concept became clearer when you revisited it? |
| 2 | A loop does not create clock cycles | The loop mistake beside an eight-edge capture trace | How do you explain this to someone coming from C/C++? |
| 3 | Does `reg` mean a physical register? | Three small code examples and their hardware meaning | Which example helped you separate a Verilog declaration from hardware storage? |
| 4 | The missing assignment that kept a car “driving” | Original and corrected arrival trace | Which input transition would expose the latch? |
| 5 | Lemmings and the 20/21-cycle boundary | Landing timeline and saturating counter idea | What long-fall case would you add to the checks? |
| 6 | Recognizing a pattern in the right cycle | HDLC input, state and output timeline | What would you check when the pattern is right but the result fails? |
| 7 | Three samples with no wasted cycle | Two consecutive groups and their result cycles | At the third edge, which samples are already in the count? |
| 8 | The byte that makes a packet complete | PS/2 byte writes and `done` alignment | When should downstream logic treat the assembled packet as valid? |
| 9 | Two's complement, one bit at a time | LSB-first bit ribbon and Moore-state meaning | Why does the LSB-first order make this rule work? |
| 10 | The questions I am keeping for revision | Five takeaways and a final 1101 timing example | Which topic would you like to see traced in more detail? |

The posting days are editorial order. They are independent of the old “Day” labels in PDF filenames.

## Captions and document choices

Copy the caption text after reviewing it. Add the linked source below it and two or three relevant hashtags. Where an attachment is mentioned, prepare and preview it before scheduling.

### Day 1: introduce the second pass

> I've been revisiting HDLBits for a second attempt and writing down the questions that came up while solving.
>
> Some were small: does reg always mean a register? Others needed a clock-by-clock trace: when should an FSM output become valid, and which value does a counter use at the sampling edge?
>
> I've collected the explanations into study notes and PDFs alongside my revision tracker. Over the next ten days, I'll share a few of these questions and the reasoning that helped me.
>
> Which RTL concept became clearer for you on a second pass?

**Attach:** a simple series cover, or a short overview PDF with a cover, three topic previews and a reading-index page. These are proposed assets to make, not existing files. **Link:** [Attempt 2 notes and tracker](https://github.com/kapiltrip/hdlBits/tree/main/HDLBits%20Attempt%202).

### Day 2: eight loop iterations are not eight samples

> One question from my HDLBits revision: can a for loop collect the eight bits of a serial byte?
>
> In the clocked block I was examining, the loop had no timing control. All its iterations ran during the same activation, so changing the index did not wait for the next input bit.
>
> The fix was to preserve progress across clock edges and capture one bit on each data edge. Writing out the eight samples made the difference clear.
>
> How would you explain this to someone coming from C or C++?

**Source:** [Serial input needs real clock edges](HDLBits%20Attempt%202/HDLBits_Fsm_serialdata_For_Loops_vs_Clock_Cycles.pdf), pages 2–7. **Visual:** code on one page, eight numbered data edges on the next. State that start detection and stop validation sit outside these eight data samples.

### Day 3: read the assignments to understand the hardware

> Does declaring a signal as reg mean it becomes a physical register?
>
> This was one of the questions I documented during revision. The keyword permits procedural assignment in Verilog; the assignment behavior determines whether the design needs combinational logic, a latch or an edge-triggered register.
>
> Another useful distinction: a wire declaration assignment continuously follows its expression. A variable declaration initializer does not keep tracking later input changes.
>
> Which example helped this distinction click for you?

**Source:** [Wire, reg and reset](HDLBits%20Attempt%202/HDLBits_Day8_QA_Wire_Reg_and_Shift_Reset.pdf), pages 2–3. **Visual:** three stacked cards: continuous connection, fully assigned combinational process, clocked assignment. Label these as Verilog examples.

### Day 4: follow the missing assignment

> A useful latch example from HDLBits: the car reaches its destination, but keep_driving stays high.
>
> The incomplete block assigns the output only while arrived is low. When arrived becomes high, no assignment executes, so the previous value is retained.
>
> Adding always @(*) does not fill in the missing assignment. The corrected combinational description must define the output on that path too.
>
> Which input transition would you use to reveal this bug?

**Source:** [If statements and latches](HDLBits%20Attempt%202/HDLBits_Day9_QA_Latches_and_Sequence_FSM.pdf), pages 2–4. **Visual:** “driving with fuel → arrival → tank changes” with original and corrected outputs aligned below. Keep the intentional latch discussion distinct from accidental incomplete logic.

### Day 5: one extra falling cycle matters

> Lemmings 4 made me pay attention to exactly when counting begins.
>
> The rule depends on falling for more than 20 cycles, so the 20-cycle and 21-cycle cases must behave differently when landing. A much longer fall also matters: a wrapping counter can lose the fact that the threshold was crossed.
>
> My notes walk through the first falling cycle, the landing boundary and saturating the count once it reaches 21.
>
> What long-fall test would you add?

**Source:** [Loops, muxes and storage](HDLBits%20Attempt%202/HDLBits_Combined_Questions_and_Day2_Review.pdf), page 8. **Visual:** two aligned landing traces for 20 and 21 cycles, plus a small “21 → 21” saturation illustration. Copy the counting convention from the note so the first falling cycle is counted consistently.

### Day 6: make the output cycle visible

> In the HDLBits HDLC exercise, recognizing the bit pattern was only part of the job. The output also had to be valid in the required cycle.
>
> I documented an early output approach and the working Moore version, where event states preserve the detected discard or flag condition after the sampling edge.
>
> The most useful step was tracing input, current state and output together. The next input bit still needs to be processed while the event is being reported.
>
> What would you inspect first when the pattern is right but the result fails?

**Source:** [HDLC: getting the output cycle right](HDLBits%20Attempt%202/HDLBits_Fsm_hdlc_Mealy_to_Moore_Deep_Dive.pdf), pages 2–12. **Visual:** select one discard example and a following bit. Preserve the exact post-edge convention. Do not turn this particular fix into “Mealy is always wrong” or a claim about every Moore implementation.

### Day 7: include the third sample

> A three-sample FSM exercise raised two good questions: does the start edge count as sample one, and does the counter already include the third sample when I test it?
>
> In this exercise, sampling starts after entering the active state. At the third sampling edge, the stored count contains the first two samples, so the decision includes the current input as well.
>
> The next group begins on the next edge, without a spare reset cycle.
>
> How would you check this with two back-to-back groups?

**Source:** [Counting three-sample groups](HDLBits%20Attempt%202/HDLBits_Entry90_Exams_2014_Q3FSM_Three_Sample_Window_Deep_Dive.pdf), pages 2–3 and 9–12. **Visual:** start edge, group `101`, group `000`; show the result after each third sample. Label the stored count before the edge and the result after it.

### Day 8: align packet data and done

> Collecting three bytes is only useful if the packet is complete when done says it is valid.
>
> In my HDLBits PS/2 parser notes, I traced each byte into its part of the output register and followed the FSM into the done state. That made it easier to separate byte capture from packet-valid timing.
>
> This is a byte-level parser exercise: the incoming value is already a byte. Keeping that interface clear helps explain exactly what the circuit does.
>
> When should downstream logic treat the assembled packet as valid?

**Source:** [Bytes, flip-flops and PS/2 packets](HDLBits%20Attempt%202/HDLBits_Day4_Questions_Vector_DFF_PS2.pdf), pages 4–6. **Visual:** three colored bytes flowing into their destination slices, with sampling edges and `done` below. Distinguish the post-edge valid interval from what another flip-flop samples at that same edge.

### Day 9: explain why the states exist

> Two's complement has an interesting serial form when the input arrives least-significant bit first: copy the zeros and the first one, then invert the remaining bits.
>
> The HDLBits Moore exercise helped me connect this rule to state meaning. I needed to understand both which phase the machine remembered and which output bit each state represented.
>
> I wrote down the derivation from invert-plus-one, a bit-by-bit example and the reason for the three Moore states.
>
> Why does the LSB-first order make this rule work?

**Source:** [Moore serial two's complement](HDLBits%20Attempt%202/HDLBits_Entry80_Moore_Serial_Twos_Complement_Deep_Dive.pdf), pages 2–7. **Visual:** reuse the `8'h2C → 8'hD4` example, mark the first incoming one, and label serial time separately from conventional MSB-first binary notation.

### Day 10: close with a useful revision habit

> The questions I want to keep from this HDLBits pass are simple:
>
> What is sampled at this edge? Which value is old? What must the state remember? Is every combinational output assigned? What happens at the boundary?
>
> I used these questions throughout my notes, including the 1101 recognizer and its output timing. The explanations and tracker are collected in the repository for anyone revising similar topics.
>
> Which topic would you like to see traced in more detail?

**Source:** [1101 recognizer discussion](HDLBits%20Attempt%202/HDLBits_Day9_QA_Latches_and_Sequence_FSM.pdf), pages 5–6, and the [complete notes index](HDLBits%20Attempt%202/DOCUMENT_INDEX.md). **Visual:** the five questions on a closing card, with a small recognizer trace as evidence. In this exercise detection stays asserted until reset; do not draw it as a one-cycle pulse.

## Beautiful visual ideas to choose from

### 1. The original question as the cover

Use one real question from your notes as the headline: **“Why can't a loop receive eight serial bits?”** Under it, place a short readable code crop and “HDLBits · Attempt 2 · 02/10.” The next page answers the question through a trace. This creates a recognisable series from material you already have.

### 2. A waveform with a reading guide

Use two or three signals, numbered sampling edges and one highlighted interval. Put the assumption, “values shown after each rising edge,” directly beside the trace when applicable. End with a short statement such as “The counter still holds the first two samples here.” A static annotated trace is enough; animation is optional later.

### 3. Before, observation, correction

Three panels: the original assumption, the input sequence that exposes it, and the corrected reasoning. Label historical code as an original attempt. For the latch post, the observation is the arrival transition retaining a previous output; for the serial post, it is repeated reads within one activation.

### 4. A notebook and code pairing

Use a genuine handwritten sketch or your own explanation beside a clean code excerpt. If a note is a screenshot, crop it to the relevant portion and keep its text readable. Use handwriting where it adds reasoning, such as a state transition or sample count, rather than as decoration.

### 5. A single-page resource map

For the launch or closing post, make a short “Start here” page with three paths: **clock-cycle reasoning**, **FSM state and outputs**, and **storage and wiring**. Link each to the matching PDFs. This can become the first page readers save for later revision.

**Suggested visual style:** warm white background `#F7F5F0`, dark navy text `#162235`, teal highlight `#087F8C`, and amber `#B76E00` for a highlighted mistake. Use plain sans-serif text and monospace code. Treat portrait 4:5 pages as a design option, not a LinkedIn requirement. Use consistent page sizes, generous margins, one headline and one diagram per page. Keep code around 8–12 lines per slide when possible. These are design suggestions, not claims about algorithm performance.

## Extra ideas if you want alternatives

- **“Which value is newer?”** Use the [dual-edge note](HDLBits%20Attempt%202/HDLBits_Day6_Non_FSM_QA_Dualedge_and_Circuit5.pdf), pages 3–4, for a trace where OR cannot select the newest sample. Keep its FPGA implementation cautions attached if you discuss hardware use.
- **“The warning was telling me the width.”** Use [FSM widths and counter connections](HDLBits%20Attempt%202/HDLBits_Day7_QA_FSM_Warnings_and_Counter_Interface.pdf), pages 2–4, for one actual truncation example.
- **“A present input cannot replace remembered history.”** Use the water-level example in [States, sampled edges and operators](HDLBits%20Attempt%202/HDLBits_Recovered_Code_Questions_54_74_75_77.pdf), page 2.
- **“Why the parity check uses that value.”** Use the serial PDF, pages 10–11, for the accumulator and stop-edge explanation as a separate future post.
- **“An event that stays remembered.”** Use the sticky-edge section of the [Day 5 review](HDLBits%20Attempt%202/HDLBits_Day5_Original_Submissions_Review.pdf) to compare an edge event with stored event history.

Choose an alternative only if it is a clearer story than one of the planned topics. You do not need to publish every document in ten days.

## Preparing and scheduling the series

### Tomorrow's practical order

1. Finish the remaining HDLBits work and reconcile the tracker before making a completion claim.
2. Review this plan. Keep captions that reflect what you actually learned and adjust any phrasing that does not sound like you.
3. Choose one visual style. Make the launch asset and one sample technical post first; inspect both on your phone before making the rest.
4. Select the remaining source pages. Export short excerpts only where needed, preserving explanations and references. Budget a separate preparation session if the assets take longer than expected.
5. Attach each asset to its caption, add the direct GitHub resource link, and check the post preview.
6. Set Day 1, then schedule the ten dates. Return briefly after publication for technical replies.

**A reasonable minimum:** launch cover, existing readable PDFs for the deeper posts, and simple source-page images for the short ones. Ten newly designed decks are optional; completing HDLBits does not require another large design project before you can share it.

### LinkedIn steps

For a document post, start a post, open the additional content options, choose **Add a document / Document**, select the PDF and give it a descriptive title. LinkedIn supports PDF, DOC/DOCX and PPT/PPTX documents up to 100 MB and 300 pages, and recommends PDF. Uploaded documents cannot be replaced within the published post, so check the attachment first. See [LinkedIn's document instructions](https://www.linkedin.com/help/linkedin/answer/a518909), checked 7 September 2026 IST.

For scheduling, prepare the caption and attachment, use the **clock icon**, select the date and time, then choose **Next → Schedule**. LinkedIn's personal-profile help lists a scheduling window of 10 minutes to three months and bases timing on the device time zone. Confirm the device is set to **Asia/Kolkata** for the proposed IST slot. Check the saved queue through **View all scheduled posts**. The current help excludes events, jobs and services from scheduling; verify that the clock option remains available after attaching your chosen document. See [LinkedIn's scheduling instructions](https://www.linkedin.com/help/linkedin/answer/a1347212), checked 7 September 2026 IST.

If the mobile web composer lacks an attachment or scheduling control, prepare the post in the LinkedIn app or desktop composer and check the preview there. If a particular combination is unavailable, keep that caption and PDF ready for manual posting at the planned time.

### Keep the discussion useful

Use a small relevant hashtag set such as **#Verilog #RTLDesign #HDLBits**. Swap one for **#DigitalDesign** or **#VLSI** where appropriate. This is an editorial choice, not a reach guarantee. Tag people only when their involvement is relevant and accurately described.

Spend roughly 10–15 minutes on replies when convenient. Ask a follow-up about the specific edge, input sequence or implementation someone mentions. If a correction arrives, check it, acknowledge it and update the linked note if necessary. Record useful questions as future revision topics.

Judge the series by meaningful technical conversations, whether readers use the notes, and whether you can explain the examples more clearly afterward. Record impressions and other analytics that LinkedIn exposes, but do not infer document downloads or interview outcomes from likes.

## Morning review checklist

- [ ] I like the series name: “HDLBits, second pass: the questions behind the code.”
- [ ] The tracker and completion wording reflect my actual finished work.
- [ ] The ten topics feel representative of what I learned.
- [ ] Each caption has one useful point and a question I can discuss.
- [ ] Every linked document is the intended version and opens correctly.
- [ ] Every attachment is readable on a phone and retains relevant source credit.
- [ ] HDLBits exercises, my explanations and any example checks are described accurately.
- [ ] Day 1 and the ten posting times are chosen in IST.
- [ ] Each queued post shows the correct caption, attachment and date.

**My suggested first choice tomorrow:** approve the theme and Day 2 visual style, finish the remaining problems, then prepare the launch and technical attachments using this file as the working plan.
