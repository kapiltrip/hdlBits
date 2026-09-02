# HDLBits Attempt 2

This directory is the working record for the second HDLBits pass. The tracker records problem order and progress, and its reached entries are reconciled against the original HDLBits pages and saved submissions. The review documents preserve every explicit question found in the submitted code plus the explanations that were worth revisiting.

## Current checkpoint

Verified on **2026-09-02**:

- **178** tracker entries in a continuous sequence from 1 through 178.
- **85 Done** and **93 Pending**.
- All **178 problem names** link to their matching HDLBits problem page.
- Among the 85 completed entries, **51** say `No questions asked` and **34** link to a relevant question or review document.
- Every entry from **1 through 85** now has a fresh successful submission in the current Attempt 2 window. The remaining **93** entries are Pending and keep the Notes / Discussion cell blank.
- Original HDLBits pages and saved-submission selectors were inspected for entries **1 through 93** in six separate Chrome audit tabs. Submitted code for the 85 reached entries contains **15 explicit questions or explanation requests**, all of which are now answered in the linked documents.

Open the [Attempt 2 tracker](HDLBits_Attempt_2_Tracker_Simple.xlsx) for the complete problem list.

## Question and review documents

| Tracker entries | Document | What is answered |
|---|---|---|
| 2, 4, 6 | [Serial receiver: loops versus clock cycles](HDLBits_Fsm_serialdata_For_Loops_vs_Clock_Cycles.pdf) | Why a procedural loop does not create future clocks, why repeated nonblocking increments read the same old value, how to capture one serial bit per edge, LSB-first reconstruction, stop/error recovery, and the parity extension. |
| 7, 13, 19-31, 36, 38 | [Combined questions and Day 2-3 review](HDLBits_Combined_Questions_and_Day2_Review.pdf) | Eight code-question groups: the Lemmings fall counter, bitwise versus logical mux operators, `genvar` versus a procedural loop variable, population-count initialization, mux selector hierarchy, `~` versus `!`, `&` versus `&&` in a condition, and intentional D-latch inference. The remaining referenced rows are explicitly included as review-only entries in the PDF's question map. |
| 8 | [HDLC Mealy-to-Moore deep dive](HDLBits_Fsm_hdlc_Mealy_to_Moore_Deep_Dive.pdf) | Moore versus Mealy output timing, why `reg` does not imply a flip-flop, why input-dependent output decoding fires before the sampling edge, why the naive Moore rewrite is still early, and why the working machine needs distinct event states. |
| 66, 67, 70 | [Day 4 vector, DFF, and PS/2 questions](HDLBits_Day4_Questions_Vector_DFF_PS2.pdf) | Indexed part-select direction and stride, D-flip-flop excitation, and a single-owner clocked PS/2 parser/datapath with correct byte timing and `done` behavior. |
| 54, 74, 75, 77 | [Recovered code questions](output/pdf/HDLBits_Recovered_Code_Questions_54_74_75_77.pdf) | The exact four missed code comments, direct answers, timing/state reasoning, corrected Verilog patterns, worked tables, observed mistakes, and a revision checklist. |
| 80 | [Entry 80 Moore serial two's-complement deep dive](output/pdf/HDLBits_Entry80_Moore_Serial_Twos_Complement_Deep_Dive.pdf) | The newly submitted request for a deep explanation: the LSB-first algorithm, why all three Moore states are necessary, every transition, post-edge timing, the corrected S2 branch, a Mealy comparison, and revision checks. |
| 81-85 | [Day 5 original-submission review](HDLBits_Day5_Original_Submissions_Review.md) | The original-page and submission-history audit through entry 93, corrected RTL and explanations for entries 81-85, and the complete Chrome evidence appendix. |

These groups account for all **34 tracker entries** whose Notes / Discussion cell links to a document. All 34 are now completed entries, and every such cell is a direct hyperlink to the named document.

## Verification record

- All 178 stored HDLBits problem targets were fetched successfully during this checkpoint and returned HTTP 200.
- The six PDFs contain **57 pages** in total. Every page was text-extracted and freshly rendered; no blank, clipped, overlapping, or unreadable page was found.
- The working HDLC Moore source passed **1,022 post-edge reference-model checks**. The earlier Mealy-style draft elaborates successfully, and its timing failure is intentionally preserved and explained in the HDLC PDF.
- The serial-loop self-check reproduced the documented single-edge failure and verified the counter-controlled eight-edge capture.
- The complete vector-reversal and PS/2 examples shown in the Day 4 PDF passed directed and randomized simulation checks.
- The Day 5 self-check passed the corrected behavior for entries 74, 75, 77, and 80-85, including randomized concatenation, sticky edge capture, reset timing, the Ringer truth table, and true one-hot Mealy encoding.
- The tracker contains **212 Excel `HYPERLINK` formulas**: 178 problem links and 34 document/review links. All have friendly cached labels, with zero error cells and zero `HYPERLINK is not implemented` diagnostics.
- Every one of the 93 inspected original HDLBits pages was compared with its displayed saved-submission history. Entries 1-85 have a successful submission in the current Attempt 2 window beginning 2026-08-29. Entries 86-93 show only older successes and therefore remain Pending.

## Evidence boundary

The HDLBits website is the authority for platform acceptance, and its saved-submission history now supports all 85 `Done` states. Local simulation is a separate check and was run only where source or a reusable testbench is preserved in this directory; it is not claimed as a local rerun of all 85 accepted submissions. Entries 86 through 178 have not yet been reached in Attempt 2, so they remain Pending without any current-window submission claim; entries 86-93 were additionally checked to confirm the progress frontier.
