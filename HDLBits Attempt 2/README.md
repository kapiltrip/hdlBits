# HDLBits Attempt 2

This directory is the working record for the second HDLBits pass. The tracker records problem order and progress, and its reached entries are reconciled against the original HDLBits pages and saved submissions. The review documents preserve every explicit question found in the submitted code plus the explanations that were worth revisiting.

## Current checkpoint

Verified on **2026-09-06**:

- **178** tracker entries in a continuous sequence from 1 through 178.
- **140 Done** and **38 Pending**.
- All **178 problem names** link to their matching HDLBits problem page.
- Among the 140 completed entries, **97** say `No questions asked` and **43** link to a relevant question or review document.
- Entries **1-127, 129-131, 134-140, and 142-144** are Done. The latest visible Chrome result panels explicitly showed `Status: Success!` for entries 123, 131, 134, 135, 136, 137, 138, 139, 140, 142, 143, and 144. Their historical `Last success` dates were not used as new completion timestamps.
- Entries **128, 132-133, 141, and 145-178** remain Pending. In the final inspected open batch, entry 132 displayed an incorrect current result, while entries 128 and 133 had no current result panel. These pages were left open and unchanged. Older green page badges do not establish completion of the current pass.
- The current question-bearing entries 102, 107, and 109 share a Day 7 Q&A PDF covering Quartus width warnings, FSM next-state decoding, and the 1-12 counter interface.

Open the [Attempt 2 tracker](HDLBits_Attempt_2_Tracker_Simple.xlsx) for the complete problem list.

## Question and review documents

| Tracker entries | Document | What is answered |
|---|---|---|
| 2, 4, 6 | [Serial receiver: loops versus clock cycles](HDLBits_Fsm_serialdata_For_Loops_vs_Clock_Cycles.pdf) | Why a procedural loop does not create future clocks, why repeated nonblocking increments read the same old value, how to capture one serial bit per edge, LSB-first reconstruction, stop/error recovery, and the parity extension. |
| 7, 13, 19-31, 36, 38 | [Combined questions and Day 2-3 review](HDLBits_Combined_Questions_and_Day2_Review.pdf) | Eight code-question groups: the Lemmings fall counter, bitwise versus logical mux operators, `genvar` versus a procedural loop variable, population-count initialization, mux selector hierarchy, `~` versus `!`, `&` versus `&&` in a condition, and intentional D-latch inference. The remaining referenced rows are explicitly included as review-only entries in the PDF's question map. |
| 8 | [HDLC Mealy-to-Moore deep dive](HDLBits_Fsm_hdlc_Mealy_to_Moore_Deep_Dive.pdf) | Moore versus Mealy output timing, why `reg` does not imply a flip-flop, why input-dependent output decoding fires before the sampling edge, why the naive Moore rewrite is still early, and why the working machine needs distinct event states. |
| 66, 67, 70 | [Day 4 vector, DFF, and PS/2 questions](HDLBits_Day4_Questions_Vector_DFF_PS2.pdf) | Indexed part-select direction and stride, D-flip-flop excitation, and a single-owner clocked PS/2 parser/datapath with correct byte timing and `done` behavior. |
| 54, 74, 75, 77 | [Recovered code questions](HDLBits_Recovered_Code_Questions_54_74_75_77.pdf) | The exact four missed code comments, direct answers, timing/state reasoning, corrected Verilog patterns, worked tables, observed mistakes, and a revision checklist. |
| 80 | [Entry 80 Moore serial two's-complement deep dive](HDLBits_Entry80_Moore_Serial_Twos_Complement_Deep_Dive.pdf) | The newly submitted request for a deep explanation: the LSB-first algorithm, why all three Moore states are necessary, every transition, post-edge timing, the corrected S2 branch, a Mealy comparison, and revision checks. |
| 81-85 | [Day 5 original-submission review](HDLBits_Day5_Original_Submissions_Review.md) | The original-page and submission-history audit through entry 93, corrected RTL and explanations for entries 81-85, and the complete Chrome evidence appendix. |
| 87, 89 | [Day 6 non-FSM Q&A: Dualedge and Circuit5](HDLBits_Day6_Non_FSM_QA_Dualedge_and_Circuit5.pdf) | Why OR-ing the two edge registers fails; the clock-selected MUX and XOR-feedback approaches; the difference between simulation, generic FPGA synthesis, and real dedicated DDR I/O; AMD IDDR/ODDR and Intel/Altera DDIO examples; half-cycle timing, duty-cycle, glitch, metastability, reset, and startup concerns; plus complete Circuit5 waveform-to-mux inference and `case` theory. |
| 90 | [Entry 90 three-sample-window FSM deep dive](HDLBits_Entry90_Exams_2014_Q3FSM_Three_Sample_Window_Deep_Dive.pdf) | Both wrong attempts, why a procedural loop samples one value repeatedly, the four independent bugs in the three-state version, third-edge timing, nonblocking-assignment semantics, unconditional window reset, clean corrected RTL, and exhaustive verification. |
| 102, 107, 109 | [Day 7 Q&A: FSM warnings and counter interface](HDLBits_Day7_QA_FSM_Warnings_and_Counter_Interface.pdf) | Why Quartus warning 10230 reports 32-to-1 truncation for unsized literals, warning-free Q3c and Q6b next-state logic, why `clk` is intentionally unused in the combinational exercise, and how `Q`, `c_enable`, `c_load`, and `c_d` connect through the provided 1-12 counter hierarchy. |
| 123, 127, 129 | [Day 8 Q&A: wire, reg and shift-register reset](HDLBits_Day8_QA_Wire_Reg_and_Shift_Reset.pdf) | Net declaration assignments versus variable initialization, carry-chain wiring and generate bounds, why a constant continuous assignment cannot reset a shift register, and the clock's accepted seconds/minutes/hour rollover logic, packed-BCD comparisons, nonblocking-assignment timing, and AM/PM transition. |

These groups account for all **43 tracker entries** whose Notes / Discussion cell links to a document; all 43 are completed. Every such cell is a direct hyperlink to the named document.

## Verification record

- The full stored problem-target set retains its earlier successful HTTP verification; all 24 completion pages added at this checkpoint were read directly in Chrome with saved `Last success` records across the four batches.
- The ten PDFs contain **100 pages** in total. The updated five-page Day 8 Q&A was rendered and visually checked, following the earlier seven-page Day 7 check.
- The working HDLC Moore source passed **1,022 post-edge reference-model checks**. The earlier Mealy-style draft elaborates successfully, and its timing failure is intentionally preserved and explained in the HDLC PDF.
- The serial-loop self-check reproduced the documented single-edge failure and verified the counter-controlled eight-edge capture.
- The complete vector-reversal and PS/2 examples shown in the Day 4 PDF passed directed and randomized simulation checks.
- The Day 5 self-check passed the corrected behavior for entries 74, 75, 77, and 80-85, including randomized concatenation, sticky edge capture, reset timing, the Ringer truth table, and true one-hot Mealy encoding.
- The Day 6 FSM self-check passed all eight possible three-bit groups plus back-to-back windows and reproduced the saved reset-only-on-match failure. The non-FSM self-check passed the Dualedge MUX/XOR implementations and all 16 Circuit5 selector values while reproducing the stale-register OR failure.
- The tracker contains **221 Excel `HYPERLINK` formulas**: 178 problem links and 43 document/review links. All saved formula caches contain their friendly labels, with zero error cells. The latest file update preserves all unrelated tracker values, formulas, and status styling. Native Excel click testing was unavailable in this session.
- Entries 1-98 retain their earlier completion evidence. Entries 99-122 are marked Done from Kapil's current-pass completion confirmations, corroborated by the matching 24 HDLBits problem pages across the four batches and each page's saved `Last success` record captured across 2026-09-04 and 2026-09-05; no fabricated per-entry timestamps are claimed.
- Entries 123, 131, 134, 135, 136, 137, 138, 139, 140, 142, 143, and 144 were added from their visible current `Status: Success!` result panels on 2026-09-06. The tracker update changed only verified status cells, required blank-note cells, and the two summary counts; entry 123 retained its existing Day 8 Q&A link, and all unrelated tracker values and formulas were checked for unintended changes.

## Evidence boundary

The HDLBits website is the authority for platform acceptance. Earlier checkpoints support entries 1-98; Kapil's explicit current-pass completion reports support entries 99-122, with matching Chrome tabs and saved-success records used as evidence. Entries 124-127 and 129-130 are supported by their current Chrome simulation result panels inspected on 5 September 2026, and entries 123, 131, 134, 135, 136, 137, 138, 139, 140, 142, 143, and 144 by their current success panels inspected on 6 September 2026. Local simulation is a separate check and was run only where source or a reusable testbench is preserved in this directory; it is not claimed as a local rerun of all accepted submissions. Entries 128, 132-133, 141, and 145-178 remain Pending.
