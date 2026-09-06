# Attempt 2 document review

Reviewed on 7 September 2026 against the saved tracker, all ten existing PDFs, the Day 5 Markdown review, the available Verilog and testbenches, and the relevant HDLBits problem statements.

At the initial review checkpoint, the tracker had 178 entries: 151 Done and 27 Pending. All 43 document links resolved to existing files and led to material for the matching entry. Of these links, 38 opened PDFs and five opened the Day 5 Markdown review. A PDF version of that review was added too. The remaining 108 completed entries said `No questions asked`; pending entries did not require invented question notes.

The workbook was not edited during that initial review. The later progress update below records the subsequent changes.

## Later Day 9 update — 7 September 2026

Marked entries 155–158 Done after Kapil's completion report and inspection of each current Chrome result panel showing `Status: Success!`: the 1101 recognizer, AND-gate testbench, Kmap3 and Always_if2. The sheet now has 155 Done and 23 Pending, with 45 document links and 110 completed entries marked `No questions asked`.

Added [Day 9 discussion](HDLBits_Day9_QA_Latches_and_Sequence_FSM.pdf), with links from entries 155 and 158. Pages 1–3 explain Always_if2 using the corrected editor code, a latch trace, complete defaults and operator/storage distinctions. Pages 4–5 answer the recognizer code's question about a cleaner implementation, with the complete cleaned FSM, transition table and an overlapping-prefix trace.

Local Icarus checks passed for all eight Always_if2 input combinations, shutdown recovery and the arrival latch trace. The cleaned recognizer passed all 4,096 twelve-bit streams against a sliding-window reference, plus sticky detection and synchronous reset checks. All five PDF pages and the updated tracker views were rendered and visually checked. The workbook comparison found only the four requested status cells, their discussion cells and the two progress totals changed; unrelated workbook package parts were preserved.

## Corrections and additions

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

Page numbers below refer to the revised PDFs. Day numbers come from the tracker, which may differ from a PDF's older filename.

| Entry | Sheet day | Problem | Document | Pages or section |
|---:|---|---|---|---|
| 2 | Day 1 | Serial receiver | [Serial input needs real clock edges](HDLBits_Fsm_serialdata_For_Loops_vs_Clock_Cycles.pdf) | 2-9; frame timing 10 |
| 4 | Day 1 | Serial receiver and datapath | [Serial input needs real clock edges](HDLBits_Fsm_serialdata_For_Loops_vs_Clock_Cycles.pdf) | 2-9; frame timing 10 |
| 6 | Day 1 | Serial receiver with parity checking | [Serial input needs real clock edges](HDLBits_Fsm_serialdata_For_Loops_vs_Clock_Cycles.pdf) | 10-11 |
| 7 | Day 1 | Lemmings 4 | [Loops, muxes and storage](HDLBits_Combined_Questions_and_Day2_Review.pdf) | 8 |
| 8 | Day 1 | Sequence recognition | [HDLC: getting the output cycle right](HDLBits_Fsm_hdlc_Mealy_to_Moore_Deep_Dive.pdf) | 2-16 |
| 13 | Day 1 | Mux | [Loops, muxes and storage](HDLBits_Combined_Questions_and_Day2_Review.pdf) | 7 |
| 19 | Day 2 | DFF with reset | [Loops, muxes and storage](HDLBits_Combined_Questions_and_Day2_Review.pdf) | 2, 9 |
| 20 | Day 2 | Simple wire | [Loops, muxes and storage](HDLBits_Combined_Questions_and_Day2_Review.pdf) | 2, 9 |
| 21 | Day 2 | NAND | [Loops, muxes and storage](HDLBits_Combined_Questions_and_Day2_Review.pdf) | 2, 9 |
| 22 | Day 2 | Simple FSM 2 (asynchronous reset) | [Loops, muxes and storage](HDLBits_Combined_Questions_and_Day2_Review.pdf) | 2, 9 |
| 23 | Day 2 | Combinational for-loop: Vector reversal 2 | [Loops, muxes and storage](HDLBits_Combined_Questions_and_Day2_Review.pdf) | 3-4 |
| 24 | Day 2 | DFF with reset value | [Loops, muxes and storage](HDLBits_Combined_Questions_and_Day2_Review.pdf) | 2, 9 |
| 25 | Day 2 | Four wires | [Loops, muxes and storage](HDLBits_Combined_Questions_and_Day2_Review.pdf) | 2, 9 |
| 26 | Day 2 | Combinational for-loop: 255-bit population count | [Loops, muxes and storage](HDLBits_Combined_Questions_and_Day2_Review.pdf) | 3, 6 |
| 27 | Day 2 | Simple FSM 2 (synchronous reset) | [Loops, muxes and storage](HDLBits_Combined_Questions_and_Day2_Review.pdf) | 2, 9 |
| 28 | Day 2 | DFF with asynchronous reset | [Loops, muxes and storage](HDLBits_Combined_Questions_and_Day2_Review.pdf) | 2, 9 |
| 29 | Day 2 | Mux | [Loops, muxes and storage](HDLBits_Combined_Questions_and_Day2_Review.pdf) | 7 |
| 30 | Day 2 | Generate for-loop: 100-bit binary adder 2 | [Loops, muxes and storage](HDLBits_Combined_Questions_and_Day2_Review.pdf) | 5 |
| 31 | Day 2 | Inverter | [Loops, muxes and storage](HDLBits_Combined_Questions_and_Day2_Review.pdf) | 10 |
| 36 | Day 2 | Add/sub | [Loops, muxes and storage](HDLBits_Combined_Questions_and_Day2_Review.pdf) | 11 |
| 38 | Day 3 | D Latch | [Loops, muxes and storage](HDLBits_Combined_Questions_and_Day2_Review.pdf) | 12 |
| 54 | Day 3 | Design a Moore FSM | [States, sampled edges and operators](HDLBits_Recovered_Code_Questions_54_74_75_77.pdf) | 2 |
| 66 | Day 4 | DFFs and gates | [Bytes, flip-flops and PS/2 packets](HDLBits_Day4_Questions_Vector_DFF_PS2.pdf) | 3 |
| 67 | Day 4 | Vector part select | [Bytes, flip-flops and PS/2 packets](HDLBits_Day4_Questions_Vector_DFF_PS2.pdf) | 2-3 |
| 70 | Day 4 | PS/2 packet parser and datapath | [Bytes, flip-flops and PS/2 packets](HDLBits_Day4_Questions_Vector_DFF_PS2.pdf) | 4-6 |
| 74 | Day 5 | Detect an edge | [States, sampled edges and operators](HDLBits_Recovered_Code_Questions_54_74_75_77.pdf) | 3 |
| 75 | Day 5 | Q8: Design a Mealy FSM | [States, sampled edges and operators](HDLBits_Recovered_Code_Questions_54_74_75_77.pdf) | 4 |
| 77 | Day 5 | Four-input gates | [States, sampled edges and operators](HDLBits_Recovered_Code_Questions_54_74_75_77.pdf) | 5 |
| 80 | Day 5 | Q5a: Serial two's complementer (Moore FSM) | [Moore serial two's complement](HDLBits_Entry80_Moore_Serial_Twos_Complement_Deep_Dive.pdf) | 2-8 |
| 81 | Day 5 | Combinational circuit 4 | [Day 5 review (PDF; Markdown still linked from sheet)](HDLBits_Day5_Original_Submissions_Review.pdf) | Entry 81 section |
| 82 | Day 5 | Vector concatenation operator | [Day 5 review (PDF; Markdown still linked from sheet)](HDLBits_Day5_Original_Submissions_Review.pdf) | Entry 82 section |
| 83 | Day 5 | Edge capture register | [Day 5 review (PDF; Markdown still linked from sheet)](HDLBits_Day5_Original_Submissions_Review.pdf) | Entry 83 section |
| 84 | Day 5 | Ring or vibrate? | [Day 5 review (PDF; Markdown still linked from sheet)](HDLBits_Day5_Original_Submissions_Review.pdf) | Entry 84 section |
| 85 | Day 5 | Q5b: Serial two's complementer (Mealy FSM) | [Day 5 review (PDF; Markdown still linked from sheet)](HDLBits_Day5_Original_Submissions_Review.pdf) | Entry 85 section |
| 87 | Day 5 | Dual-edge triggered flip-flop | [Dual-edge sampling and Circuit5](HDLBits_Day6_Non_FSM_QA_Dualedge_and_Circuit5.pdf) | 3-14 |
| 89 | Day 5 | Combinational circuit 5 | [Dual-edge sampling and Circuit5](HDLBits_Day6_Non_FSM_QA_Dualedge_and_Circuit5.pdf) | 15-17 |
| 90 | Day 6 | Q3a: FSM | [Counting three-sample groups](HDLBits_Entry90_Exams_2014_Q3FSM_Three_Sample_Window_Deep_Dive.pdf) | 2-12 |
| 102 | Day 6 | Q3c: FSM logic | [FSM widths and counter connections](HDLBits_Day7_QA_FSM_Warnings_and_Counter_Interface.pdf) | 2-3 |
| 107 | Day 6 | Q6b: FSM next-state logic | [FSM widths and counter connections](HDLBits_Day7_QA_FSM_Warnings_and_Counter_Interface.pdf) | 2, 4 |
| 109 | Day 7 | Counter 1-12 | [FSM widths and counter connections](HDLBits_Day7_QA_FSM_Warnings_and_Counter_Interface.pdf) | 5 |
| 123 | Day 7 | 12-hour clock | [Wire, reg and reset](HDLBits_Day8_QA_Wire_Reg_and_Shift_Reset.pdf) | 4-5 |
| 127 | Day 8 | 4-bit shift register | [Wire, reg and reset](HDLBits_Day8_QA_Wire_Reg_and_Shift_Reset.pdf) | 3 |
| 129 | Day 8 | Adder 2 | [Wire, reg and reset](HDLBits_Day8_QA_Wire_Reg_and_Shift_Reset.pdf) | 1-2 |

## What was tested

The saved Icarus tests passed for entries 74, 75, 77, 80-85, 87, 89 and 90. The HDLC source passed 1,022 post-edge reference checks. The serial-loop test reproduced the original one-edge failure and checked the eight-edge capture. The original Mealy trace reproduced the early discard pulse.

Additional tests used code extracted from the revised PDFs: 131,072 mux selections, 1,000 randomized byte reversals, 100 back-to-back PS/2 packets, a full 86,400-second clock cycle with reset/enable checks, and falls from 19 through 70 cycles. Odd-parity arithmetic was checked for all 256 bytes and both parity choices.

These are local RTL/example checks. Complete historical submissions are not saved for every tracker entry, so this review does not claim to have rerun all 151 completed problems or searched unsaved editor comments. The water-level snippet is conceptual. Vendor DDR examples still require the selected device's libraries and timing constraints for implementation checks.

## Sources for the corrections

- [HDLBits two-input mux](https://hdlbits.01xz.net/wiki/Bugs_mux2) and [four-input mux](https://hdlbits.01xz.net/wiki/Bugs_mux4).
- [Lemmings 4](https://hdlbits.01xz.net/wiki/Lemmings4).
- [Serial receiver](https://hdlbits.01xz.net/wiki/Fsm_serial), [datapath](https://hdlbits.01xz.net/wiki/Fsm_serialdata), and [parity](https://hdlbits.01xz.net/wiki/Fsm_serialdp).
- [BCD clock](https://hdlbits.01xz.net/wiki/Count_clock), [counter 1-12](https://hdlbits.01xz.net/wiki/Exams/ece241_2014_q7a), and [water-level FSM](https://hdlbits.01xz.net/wiki/Exams/ece241_2013_q4).

The edge-detector example was checked against [the official 8-bit interface](https://hdlbits.01xz.net/wiki/Edgedetect) and kept at its correct width.
