# Attempt 2 document review

## Final completion checkpoint - 9 September 2026

The saved tracker now records **178 Done, 0 Pending**. Kapil explicitly confirmed Testbench2 (entry 166) and the entire second attempt complete. Chrome's latest stored successful Testbench2 submission, dated **28 June 2026 at 11:14:42 PM**, was loaded and its complete code inspected. It is later than the last non-success at **11:14:00 PM** on that date. The saved record verifies an accepted implementation; Kapil's present confirmation establishes the current-pass completion. No new submission was made, and the June date is not presented as September evidence. Entry 166 now reads Done / No questions asked. Earlier counts below are historical checkpoints.

The accepted testbench starts clk at 0 and toggles it every five time units. The in/s pairs are 0/2 at time 0, 0/6 at 10, 1/2 at 20, 0/7 at 30, 1/0 at 40 and 0/0 at 70. It instantiates q7 with named clk, in, s and out connections.

## Full collection presentation audit - 9 September 2026

After the completion commit, all **16 PDFs / 164 pages** were rendered with Poppler and visually inspected, including every front page and all body pages. The covers use white backgrounds, a thin navy rule, precise titles, linked contents and a consistent reading guide. Decorative teal accents and strong yellow highlights were replaced with navy or neutral gray. Blue hyperlinks and meaningful diagram/result colors were retained. In particular, the HDLC diagram's pale-yellow FLAG_PULSE state was preserved because its caption explicitly identifies it by color.

The review corrected the Day 9 note's stale prose reference: its clocked FSM is now correctly identified as **page 5**, after the added cover. Code, source screenshots, technical figures and historical evidence were preserved. The palette pass checks that text, image bytes, page geometry and navigation remain unchanged. The intentional page-reference correction is separately checked and its final page was re-rendered and inspected.

Navigation checks cover all **254 bookmarks, 250 internal PDF links and 58 tracker-to-document mappings**, including the actual destination page for each cover row and section/entry bookmark. Every page has one Contents link and one All notes link, and all fonts are embedded. The saved tracker was separately reopened and checked at **178 Done / 0 Pending**, with all **236 native hyperlinks** intact.

The published GitHub Markdown index was opened and its next-state link resolved to the correct timer PDF with `#page=10`. GitHub then reported `Unable to render code block`; this is a preview limitation, not evidence that the PDF's contents links failed. Browser policy prevented opening a local PDF for an interactive click test. PDF destinations were therefore verified from the saved files, and layout from Poppler renders. Open the downloaded PDF in a link-capable PDF reader for its built-in contents and bookmarks; the index already explains the preview limitation.

## Initial collection review - 7 September 2026

Reviewed on 7 September 2026 against the saved tracker, all ten existing PDFs, the Day 5 Markdown review, the available Verilog and testbenches, and the relevant HDLBits problem statements.

At the initial review checkpoint, the tracker had 178 entries: 151 Done and 27 Pending. All 43 document links resolved to existing files and led to material for the matching entry. Of these links, 38 opened PDFs and five opened the Day 5 Markdown review. A PDF version of that review was added too. The remaining 108 completed entries said `No questions asked`; pending entries did not require invented question notes.

The workbook was not edited during that initial review. The later progress update below records the subsequent changes.

## Later Day 9 update — 7 September 2026

Marked entries 155–158 Done after Kapil's completion report and inspection of each current Chrome result panel showing `Status: Success!`: the 1101 recognizer, AND-gate testbench, Kmap3 and Always_if2. The sheet now has 155 Done and 23 Pending, with 45 document links and 110 completed entries marked `No questions asked`.

Added [Day 9 discussion](HDLBits_Day9_QA_Latches_and_Sequence_FSM.pdf), with links from entries 155 and 158. Originally pages 1–3 (now pages 2–4) explain Always_if2 using the corrected editor code, a latch trace, complete defaults and operator/storage distinctions. Originally pages 4–5 (now pages 5–6) answer the recognizer code's question about a cleaner implementation, with the complete cleaned FSM, transition table and an overlapping-prefix trace.

Local Icarus checks passed for all eight Always_if2 input combinations, shutdown recovery and the arrival latch trace. The cleaned recognizer passed all 4,096 twelve-bit streams against a sliding-window reference, plus sticky detection and synchronous reset checks. All five PDF pages and the updated tracker views were rendered and visually checked. The workbook comparison found only the four requested status cells, their discussion cells and the two progress totals changed; unrelated workbook package parts were preserved.

## Entries 159-162 and the Kmap4 operator note - 7 September 2026

Marked entries 159-162 Done after inspecting each current Chrome result panel and confirming `Status: Success!`: Shift register, FSM: Enable shift register, Kmap4, and Case statement.

Entry 161 is now covered on [Note 13, pp. 2-3](HDLBits_Day10_Kmaps_Boolean_Forms_and_Rules90_110.pdf#page=2). It explains that `|` is Verilog OR, `+` is arithmetic addition, and a paper Boolean-algebra `+` must be translated to `|` in Verilog. The source screenshot and a small `1 | 1` versus `1 + 1` comparison make the distinction concrete. An exhaustive 16-row check also explains the subtle point: `+` can accidentally match this exact expression because its four product terms are mutually exclusive, but it still communicates the wrong operation.

## Entry 163 - 7 September 2026

Marked entry 163, 3-input LUT, Done after inspecting its current Chrome result panel and confirming `Status: Success!`.

## Entry 164 and the SOP/POS note - 7 September 2026

Marked entry 164, Minimum SOP and POS, Done after inspecting its current Chrome result panel and confirming `Status: Success!`. The tracker now records **161 Done and 17 Pending**.

Entry 164 is now covered on [Note 13, pp. 4-5](HDLBits_Day10_Kmaps_Boolean_Forms_and_Rules90_110.pdf#page=4). The note defines SOP, POS and De Morgan's law, explains why each is needed, and applies them to the accepted expressions. It explicitly separates the distributive-law step used to convert the accepted SOP to POS from De Morgan's law. It also corrects an imprecise sentence from the earlier short note: SOP is derived by grouping output-1 cells and POS by grouping output-0 cells, but both forms implement the same Boolean function.

## Correction to the later Day 10 update - 7 September 2026

Reverted the incorrect completion marks for entries 165 and 167-178 and cleared the added `No questions asked` text. The inspected `Last success` dates belonged to earlier work and did not prove second-attempt completion. The tracker is restored to **161 Done and 17 Pending**. Entries 141, 145, 151, and 165-178 remain Pending until second-attempt completion is established.

## Publication and indexing update

### Five confirmed second-attempt completions - 8 September 2026

Kapil explicitly identified these five problems as completed on the second attempt. Their latest saved successes are dated 7 September 2026, later than each respective last non-success. Times below are displayed by Chrome.

| Entry | Problem | Last successful submission |
|---|---|---|
| 167 | Always_case2 — Priority encoder | 7 September 2026, 9:34:45 PM |
| 169 | Exams/m2014_q3 — Karnaugh map | 7 September 2026, 9:36:41 PM |
| 173 | Exams/2012_q1g — Karnaugh map | 7 September 2026, 9:27:15 PM |
| 174 | Tb/tff — T flip-flop | 7 September 2026, 9:45:11 PM |
| 178 | Exams/ece241_2014_q3 — K-map implemented with a multiplexer | 7 September 2026, 10:37:02 PM |

Only these five entries were marked Done, bringing the tracker to **166 Done and 12 Pending**.

### Two further second-attempt completions - 8 September 2026

Kapil explicitly identified Always_casez and Always_nolatches as complete. Entry 171, Priority encoder with casez, had a saved success displayed as 7 September 2026, 9:41:14 PM, newer than its last non-success on 24 June. Entry 176, Avoiding latches, showed `Status: Success!` in its current compile-and-simulate result panel. Its previous-submission dropdown still displayed June dates, so the current result panel, not that old saved-success label, was used as evidence.

Only entries 171 and 176 were changed from Pending to Done in this update. The tracker now records **168 Done and 10 Pending**. Existing problem links and other entry statuses were preserved.

### Rules 90 and 110 completion and Day 10 consolidation - 8 September 2026

Entry 168, Rule 90, was marked Done after its current compile-and-simulate panel was rechecked and showed `Status: Success!`. The exact editor code uses a combinational `nextVal` vector and a clocked `q` register.

Entry 172, Rule 110, was then marked Done after its current compile-and-simulate panel was rechecked and also showed `Status: Success!`. Its accepted code and the successful seed-1 trace were used to preserve the important vector direction: `q[i+1]` is the left neighbour and `q[i-1]` is the right neighbour in that implementation.

The two short Day 10 PDFs were replaced by one nine-page [K-map operators, Boolean forms and cellular automata](HDLBits_Day10_Kmaps_Boolean_Forms_and_Rules90_110.pdf). Pages 6-7 explain Rule 90's XOR neighbourhood rule, zero-valued boundaries, simultaneous state update, and why `nextVal` was used. `nextVal` is the combinational candidate for the next 512-bit generation; `q` stores the current generation. It is helpful for the chosen current-state/next-state structure and waveform debugging, but is not mathematically required: the same XOR network can be written directly in the clocked assignment without adding another cycle or register bank. Pages 8-9 derive the accepted Rule 110 expression, explain its asymmetric neighbour direction and reduce both boundary assignments from the same truth-table rule.

This update brings the tracker to **170 Done and 8 Pending**. Only entries 168 and 172 were newly closed in this combined update; every other Pending entry was left unchanged. The combined note now holds the related short explanations for entries 161, 164, 168 and 172 in one reader-facing document.

### Review 2015 timer series and next-state timing - 9 September 2026

Added the fifteen-page [timer-series FSM and next-state note](HDLBits_Day11_Review2015_Timer_Series_and_Next_State.pdf). It treats entries 144, 149, 155, 160, 165 and 170 as one learning sequence: the period-1000 counter; the MSB-first shift/down register; 1101 recognition; an exact four-cycle shift enable; the complete controller; and the complete timer. Entry 155 is intentionally explained again even though Note 12 already contains a cleanup, because the transition out of 1101 recognition determines when the following delay bits begin.

Pages 3-7 cover the component exercises, including four-bit underflow, two nonblocking assignments in one process, the `next_state` question from the 1101 recognizer, and why a continuous `assign count = 0` would conflict with the clocked owner of `count`. Pages 8-11 build the full controller and give a precise decision table for using `state`, `next_state`, or both inside clocked logic. Pages 12-15 trace fourth-bit capture, derive the exact `(delay + 1) * 1000` duration, explain what `count` represents, and provide a complete reference implementation.

The current HDLBits result panels for entries 165, 170 and 175 showed `Status: Success!`, so those three statuses were changed from Pending to Done. Entry 175, the basic one-hot-equations exercise, is deliberately not part of the PDF and is recorded as `No questions asked`. The tracker now records **173 Done and 5 Pending**; entries 141, 145, 151, 166 and 177 remain Pending.

The note builder checks the 998,999,0,1 counter boundary, MSB-first capture of 1001, four-bit decrement underflow, recognition of 1101, the incorrect delay value caused by consuming the recognizer's final bit, and every delay from 0 through 15 for exact duration and 1000-cycle output plateaus. These model checks support the explanations; the successful HDLBits panels remain the authority for exercise acceptance.

### Earlier publication checks

All **14 study PDFs** now use a consistent cover and reading index, author attribution, section and tracker-entry bookmarks, clickable contents rows, and **Contents / All notes** links on every page. The collection has **145 pages**. The [document index](DOCUMENT_INDEX.md) adds topic routes and an exact mapping for all **54 linked tracker entries**, including the six Review 2015 series entries in Note 14.

Nine existing cover pages were replaced. The Day 5 submission review, Day 8 notes, Day 9 notes, combined Day 10 note and Review 2015 timer note each use an added contents page because their original first pages contain technical material. The Day 10 note has two answer pages per topic: Kmap4 at pages 2-3, SOP/POS at pages 4-5, Rule 90 at pages 6-7, and Rule 110 at pages 8-9. Note 14's tracker labels use its final physical pages 3-15. The posting plan's historical snapshot, Markdown indexes, internal page references and current tracker discussion labels remain aligned with their stated PDF pages.

The original body text, code, diagrams, source links and historical submission records were retained. Two overlong Day 5 verification-log lines were wrapped inside the page margins. The Day 5 Markdown review gained direct section links; literal operator pipes in its tables are escaped so GitHub keeps the columns aligned. Its PDF introduction now points readers to the Markdown companion correctly.

Fonts are embedded throughout the collection. A second renderer exposed substitution and spacing problems with the original unembedded fonts; embedding corrected that display while keeping text searchable. The embedding pass checks that text, bookmarks and link destinations survive, and does not downsample images.

Validation passed for all **227 bookmarks**, **218 internal PDF links**, **54 tracker mappings** and **241 local Markdown links** across the rebuilt 14-PDF collection. Every page of Note 14 and all 14 collection covers were rendered with Poppler for visual inspection; the duplicate-footer-link check also requires exactly one Contents link and one All notes link on every page. The current workbook's logical edits are the two summary totals; status cells for entries 165, 170 and 175; Note 14 links for entries 144, 149, 155, 160, 165 and 170; and `No questions asked` for entry 175 (`B3`, `D3`, `D170`, `D175`, `D180`, `E149`, `E154`, `E160`, `E165`, `E170`, `E175`, and `E180`). These are document and tracker checks, separate from the earlier RTL test results below.

The reproducible builder and maintenance instructions are in [internal/Documentation](internal/Documentation/README.md).

## Corrections and additions

### LFSR and Conway additions - 9 September 2026

The current collection has **16 PDFs, 164 pages and 58 linked tracker entries**. The tracker records **177 Done and 1 Pending**; entry 166 (Testbench2) remains unconfirmed. Entries 141, 145, 151 and 177 were marked Done from their current Chrome `Status: Success!` panels, not historical first-attempt dates.

[Note 15](HDLBits_Day12_LFSR_Taps_Shifts_and_Old_Value_Timing.pdf) covers all three LFSRs: one-based taps, bit-index conversion, schematic and board-pin mapping, complete RTL, nonblocking old-value behavior, exact small-state cycles and the 32-bit polynomial check. [Note 16](HDLBits_Day12_Conway_Grid_Indexing_and_Next_State.pdf) preserves the Conway editor's indexing question and discusses the complete solution: row/column flattening, toroidal neighbors, eight-neighbor counting, next-grid storage, loop execution, widths and boundary traces. The earlier timer-series note continues to cover repeated questions within the series and when a sequential block should inspect `state`, `next_state`, or both. The basic one-hot exercise remains excluded from that document as requested.

All 236 tracker links (178 problem links and 58 discussion links) now use native hyperlinks and friendly blue text. Existing destinations and labels are preserved, apart from the new LFSR/Conway discussion labels. Long discussion text wraps within its cell. The saved workbook was reimported and visually checked at the beginning, middle, LFSR rows and end; its formula-error and hyperlink-fallback scan found no matches. Structure, validation, panes and unrelated cell values were compared with the pre-edit workbook.

All 19 pages of the two new notes and all collection covers were rendered with Poppler and visually checked. The collection checker validates the 254 bookmarks, 250 internal PDF links, 58 tracker mappings, embedded fonts, page boundaries, footer links and local Markdown destinations. The prior 14-PDF figures above remain the historical timer checkpoint.

The LFSR builder checks the 31-state and seven-state cycles, first 32-bit transition and primitive-polynomial order. The saved Conway RTL passed **1,638 post-edge full-grid Icarus checks**, including all 512 center/neighbor patterns, 100 random five-generation runs, still-life and seam-crossing oscillator patterns, loading priority, consecutive loads and no state change between clock edges. These checks are separate from platform acceptance.

- Corrected the entry 13 mux polarity: `sel=0` selects `a`, and `sel=1` selects `b`. Updated the code and truth table together.
- Expanded entry 30's explanation of why carry signals are wires, and corrected the Norgate row's description to two-input NOR.
- Replaced the incomplete Lemmings counter excerpt with a clearly labeled monitor that counts the first falling cycle and saturates at 21. The explanation covers 20/21-cycle landing behavior and long falls.
- Added two serial-receiver pages covering start/stop timing, missing-stop recovery, byte validity, odd parity, and the accumulator value seen at the stop edge.
- Removed the hidden obsolete Day 8 paragraph saying entry 123 was unfinished. Clarified that last-assignment priority applies within one process; competing processes can race.
- Explained that entry 90 has two controller states plus counter/output memory. Separated functional errors from redundant assignments.
- Replaced dated progress summaries on PDF covers with entry references and reading guides. Kept historical submission records labeled by date.
- Made introductions, headings and explanations more natural while preserving original quoted questions, useful code, diagrams and timing tables.
- Added the Day 5 PDF, repaired unreadable table headers, and checked page breaks and layout.

## Where each linked entry is answered

The [document index](DOCUMENT_INDEX.md#find-a-tracker-entry) is the main entry lookup. This table uses the current physical PDF page numbers, which match the printed page counters. Sheet days can differ from the older days in filenames.

| Entry | Sheet day | Problem | Document and pages |
|---:|---|---|---|
| 2 | Day 1 | Serial receiver | [Note 01, pp. 2-10](HDLBits_Fsm_serialdata_For_Loops_vs_Clock_Cycles.pdf#page=2) |
| 4 | Day 1 | Serial receiver and datapath | [Note 01, pp. 2-10](HDLBits_Fsm_serialdata_For_Loops_vs_Clock_Cycles.pdf#page=2) |
| 6 | Day 1 | Serial receiver with parity checking | [Note 01, pp. 10-11](HDLBits_Fsm_serialdata_For_Loops_vs_Clock_Cycles.pdf#page=10) |
| 7 | Day 1 | Lemmings 4 | [Note 02, pp. 8](HDLBits_Combined_Questions_and_Day2_Review.pdf#page=8) |
| 8 | Day 1 | Sequence recognition | [Note 03, pp. 2-16](HDLBits_Fsm_hdlc_Mealy_to_Moore_Deep_Dive.pdf#page=2) |
| 13 | Day 1 | Mux | [Note 02, pp. 7](HDLBits_Combined_Questions_and_Day2_Review.pdf#page=7) |
| 19 | Day 2 | DFF with reset | [Note 02, pp. 2, 9](HDLBits_Combined_Questions_and_Day2_Review.pdf#page=2) |
| 20 | Day 2 | Simple wire | [Note 02, pp. 2, 9](HDLBits_Combined_Questions_and_Day2_Review.pdf#page=2) |
| 21 | Day 2 | NAND | [Note 02, pp. 2, 9](HDLBits_Combined_Questions_and_Day2_Review.pdf#page=2) |
| 22 | Day 2 | Simple FSM 2 (asynchronous reset) | [Note 02, pp. 2, 9](HDLBits_Combined_Questions_and_Day2_Review.pdf#page=2) |
| 23 | Day 2 | Combinational for-loop: Vector reversal 2 | [Note 02, pp. 3-4](HDLBits_Combined_Questions_and_Day2_Review.pdf#page=3) |
| 24 | Day 2 | DFF with reset value | [Note 02, pp. 2, 9](HDLBits_Combined_Questions_and_Day2_Review.pdf#page=2) |
| 25 | Day 2 | Four wires | [Note 02, pp. 2, 9](HDLBits_Combined_Questions_and_Day2_Review.pdf#page=2) |
| 26 | Day 2 | Combinational for-loop: 255-bit population count | [Note 02, pp. 3, 6](HDLBits_Combined_Questions_and_Day2_Review.pdf#page=3) |
| 27 | Day 2 | Simple FSM 2 (synchronous reset) | [Note 02, pp. 2, 9](HDLBits_Combined_Questions_and_Day2_Review.pdf#page=2) |
| 28 | Day 2 | DFF with asynchronous reset | [Note 02, pp. 2, 9](HDLBits_Combined_Questions_and_Day2_Review.pdf#page=2) |
| 29 | Day 2 | Mux | [Note 02, pp. 7](HDLBits_Combined_Questions_and_Day2_Review.pdf#page=7) |
| 30 | Day 2 | Generate for-loop: 100-bit binary adder 2 | [Note 02, pp. 5](HDLBits_Combined_Questions_and_Day2_Review.pdf#page=5) |
| 31 | Day 2 | Inverter | [Note 02, pp. 10](HDLBits_Combined_Questions_and_Day2_Review.pdf#page=10) |
| 36 | Day 2 | Add/sub | [Note 02, pp. 11](HDLBits_Combined_Questions_and_Day2_Review.pdf#page=11) |
| 38 | Day 3 | D Latch | [Note 02, pp. 12](HDLBits_Combined_Questions_and_Day2_Review.pdf#page=12) |
| 54 | Day 3 | Design a Moore FSM | [Note 04, pp. 2](HDLBits_Recovered_Code_Questions_54_74_75_77.pdf#page=2) |
| 66 | Day 4 | DFFs and gates | [Note 05, pp. 3](HDLBits_Day4_Questions_Vector_DFF_PS2.pdf#page=3) |
| 67 | Day 4 | Vector part select | [Note 05, pp. 2-3](HDLBits_Day4_Questions_Vector_DFF_PS2.pdf#page=2) |
| 70 | Day 4 | PS/2 packet parser and datapath | [Note 05, pp. 4-6](HDLBits_Day4_Questions_Vector_DFF_PS2.pdf#page=4) |
| 74 | Day 5 | Detect an edge | [Note 04, pp. 3](HDLBits_Recovered_Code_Questions_54_74_75_77.pdf#page=3) |
| 75 | Day 5 | Q8: Design a Mealy FSM | [Note 04, pp. 4](HDLBits_Recovered_Code_Questions_54_74_75_77.pdf#page=4) |
| 77 | Day 5 | Four-input gates | [Note 04, pp. 5](HDLBits_Recovered_Code_Questions_54_74_75_77.pdf#page=5) |
| 80 | Day 5 | Q5a: Serial two's complementer (Moore FSM) | [Note 06, pp. 2-8](HDLBits_Entry80_Moore_Serial_Twos_Complement_Deep_Dive.pdf#page=2) |
| 81 | Day 5 | Combinational circuit 4 | [Note 07, pp. 5](HDLBits_Day5_Original_Submissions_Review.pdf#page=5) |
| 82 | Day 5 | Vector concatenation operator | [Note 07, pp. 5](HDLBits_Day5_Original_Submissions_Review.pdf#page=5) |
| 83 | Day 5 | Edge capture register | [Note 07, pp. 6](HDLBits_Day5_Original_Submissions_Review.pdf#page=6) |
| 84 | Day 5 | Ring or vibrate? | [Note 07, pp. 6](HDLBits_Day5_Original_Submissions_Review.pdf#page=6) |
| 85 | Day 5 | Q5b: Serial two's complementer (Mealy FSM) | [Note 07, pp. 6-7](HDLBits_Day5_Original_Submissions_Review.pdf#page=6) |
| 87 | Day 5 | Dual-edge triggered flip-flop | [Note 08, pp. 3-14](HDLBits_Day6_Non_FSM_QA_Dualedge_and_Circuit5.pdf#page=3) |
| 89 | Day 5 | Combinational circuit 5 | [Note 08, pp. 15-17](HDLBits_Day6_Non_FSM_QA_Dualedge_and_Circuit5.pdf#page=15) |
| 90 | Day 6 | Q3a: FSM | [Note 09, pp. 2-12](HDLBits_Entry90_Exams_2014_Q3FSM_Three_Sample_Window_Deep_Dive.pdf#page=2) |
| 102 | Day 6 | Q3c: FSM logic | [Note 10, pp. 2-3](HDLBits_Day7_QA_FSM_Warnings_and_Counter_Interface.pdf#page=2) |
| 107 | Day 6 | Q6b: FSM next-state logic | [Note 10, pp. 4](HDLBits_Day7_QA_FSM_Warnings_and_Counter_Interface.pdf#page=4) |
| 109 | Day 7 | Counter 1-12 | [Note 10, pp. 5](HDLBits_Day7_QA_FSM_Warnings_and_Counter_Interface.pdf#page=5) |
| 123 | Day 7 | 12-hour clock | [Note 11, pp. 5-6](HDLBits_Day8_QA_Wire_Reg_and_Shift_Reset.pdf#page=5) |
| 127 | Day 8 | 4-bit shift register | [Note 11, pp. 4](HDLBits_Day8_QA_Wire_Reg_and_Shift_Reset.pdf#page=4) |
| 129 | Day 8 | Adder 2 | [Note 11, pp. 2-3](HDLBits_Day8_QA_Wire_Reg_and_Shift_Reset.pdf#page=2) |
| 141 | Day 8 | 5-bit LFSR | [Note 15, pp. 3-6](HDLBits_Day12_LFSR_Taps_Shifts_and_Old_Value_Timing.pdf#page=3) |
| 144 | Day 9 | Counter with period 1000 | [Note 14, p. 3](HDLBits_Day11_Review2015_Timer_Series_and_Next_State.pdf#page=3) |
| 145 | Day 9 | 3-bit LFSR | [Note 15, pp. 7-9](HDLBits_Day12_LFSR_Taps_Shifts_and_Old_Value_Timing.pdf#page=7) |
| 149 | Day 9 | 4-bit shift register and down counter | [Note 14, pp. 4-5](HDLBits_Day11_Review2015_Timer_Series_and_Next_State.pdf#page=4) |
| 151 | Day 9 | 32-bit LFSR | [Note 15, pp. 10-11](HDLBits_Day12_LFSR_Taps_Shifts_and_Old_Value_Timing.pdf#page=10) |
| 155 | Day 9 | FSM: Sequence 1101 recognizer | [Note 14, p. 6](HDLBits_Day11_Review2015_Timer_Series_and_Next_State.pdf#page=6) |
| 158 | Day 9 | If statement latches | [Note 12, pp. 2-4](HDLBits_Day9_QA_Latches_and_Sequence_FSM.pdf#page=2) |
| 160 | Day 9 | FSM: Enable shift register | [Note 14, p. 7](HDLBits_Day11_Review2015_Timer_Series_and_Next_State.pdf#page=7) |
| 161 | Day 10 | 4-variable | [Note 13, pp. 2-3](HDLBits_Day10_Kmaps_Boolean_Forms_and_Rules90_110.pdf#page=2) |
| 164 | Day 10 | Minimum SOP and POS | [Note 13, pp. 4-5](HDLBits_Day10_Kmaps_Boolean_Forms_and_Rules90_110.pdf#page=4) |
| 165 | Day 10 | FSM: The complete FSM | [Note 14, pp. 8-11](HDLBits_Day11_Review2015_Timer_Series_and_Next_State.pdf#page=8) |
| 168 | Day 10 | Rule 90 | [Note 13, pp. 6-7](HDLBits_Day10_Kmaps_Boolean_Forms_and_Rules90_110.pdf#page=6) |
| 170 | Day 10 | The complete timer | [Note 14, pp. 12-15](HDLBits_Day11_Review2015_Timer_Series_and_Next_State.pdf#page=12) |
| 172 | Day 10 | Rule 110 | [Note 13, pp. 8-9](HDLBits_Day10_Kmaps_Boolean_Forms_and_Rules90_110.pdf#page=8) |
| 177 | Day 10 | Conway's Game of Life 16x16 | [Note 16, pp. 2-7](HDLBits_Day12_Conway_Grid_Indexing_and_Next_State.pdf#page=2) |

## What was tested

The saved Icarus tests passed for entries 74, 75, 77, 80-85, 87, 89 and 90. The HDLC source passed 1,022 post-edge reference checks. The serial-loop test reproduced the original one-edge failure and checked the eight-edge capture. The original Mealy trace reproduced the early discard pulse.

Additional tests used code extracted from the revised PDFs: 131,072 mux selections, 1,000 randomized byte reversals, 100 back-to-back PS/2 packets, a full 86,400-second clock cycle with reset/enable checks, and falls from 19 through 70 cycles. Odd-parity arithmetic was checked for all 256 bytes and both parity choices.

For the combined Day 10 note, all 16 Kmap4 input combinations were checked against four-input parity and for mutual exclusivity of the submitted product terms. The entry 164 SOP and POS were compared for all 16 inputs and checked against every specified 0/1 row. Rule 90's eight neighbourhoods and the loop/vector implementations were compared on representative 512-bit states, including both boundaries. Rule 110's accepted expression was checked against all eight neighbourhoods, both boundary reductions and the ten-value seed-1 trace shown by the successful HDLBits simulation.

For the Review 2015 timer note, executable model checks cover the period-1000 boundary, four-bit serial order and underflow, 1101-to-capture transition, the state-versus-next-state delay-bit counterexample, and all sixteen legal delay values. Each value is held for exactly 1000 modeled counting cycles, including the final zero block.

These are local RTL/example checks. Complete historical submissions are not saved for every tracker entry, so this review does not claim to have rerun all 151 completed problems or searched unsaved editor comments. The water-level snippet is conceptual. Vendor DDR examples still require the selected device's libraries and timing constraints for implementation checks.

## Sources for the corrections

- [5-bit LFSR](https://hdlbits.01xz.net/wiki/Lfsr5), [3-bit LFSR circuit](https://hdlbits.01xz.net/wiki/Mt2015_lfsr), [32-bit LFSR](https://hdlbits.01xz.net/wiki/Lfsr32), and [Conway's Game of Life](https://hdlbits.01xz.net/wiki/Conwaylife).

- [HDLBits two-input mux](https://hdlbits.01xz.net/wiki/Bugs_mux2) and [four-input mux](https://hdlbits.01xz.net/wiki/Bugs_mux4).
- [Lemmings 4](https://hdlbits.01xz.net/wiki/Lemmings4).
- [Serial receiver](https://hdlbits.01xz.net/wiki/Fsm_serial), [datapath](https://hdlbits.01xz.net/wiki/Fsm_serialdata), and [parity](https://hdlbits.01xz.net/wiki/Fsm_serialdp).
- [BCD clock](https://hdlbits.01xz.net/wiki/Count_clock), [counter 1-12](https://hdlbits.01xz.net/wiki/Exams/ece241_2014_q7a), and [water-level FSM](https://hdlbits.01xz.net/wiki/Exams/ece241_2013_q4).
- [Kmap4](https://hdlbits.01xz.net/wiki/Kmap4), [minimum SOP and POS](https://hdlbits.01xz.net/wiki/Exams/ece241_2013_q2), [Rule 90](https://hdlbits.01xz.net/wiki/Rule90), and [Rule 110](https://hdlbits.01xz.net/wiki/Rule110).
- Review 2015 timer series: [period-1000 counter](https://hdlbits.01xz.net/wiki/Exams/review2015_count1k), [shift/down register](https://hdlbits.01xz.net/wiki/Exams/review2015_shiftcount), [1101 recognizer](https://hdlbits.01xz.net/wiki/Exams/review2015_fsmseq), [four-cycle enable](https://hdlbits.01xz.net/wiki/Exams/review2015_fsmshift), [complete controller](https://hdlbits.01xz.net/wiki/Exams/review2015_fsm), and [complete timer](https://hdlbits.01xz.net/wiki/Exams/review2015_fancytimer).

The edge-detector example was checked against [the official 8-bit interface](https://hdlbits.01xz.net/wiki/Edgedetect) and kept at its correct width.
