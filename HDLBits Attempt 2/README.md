# HDLBits Attempt 2

Use the [tracker](HDLBits_Attempt_2_Tracker_Simple.xlsx) for problem order and progress. The notes below explain the questions and mistakes from this pass.

As of 7 September 2026, the sheet records **155 Done and 23 Pending** out of 178 entries. All 45 document links have matching explanations. The [document review](DOCUMENT_REVIEW.md) maps each entry to its pages and records the corrections and checks.

## Study PDFs

The day labels in older filenames describe the original review sessions. Entry numbers below follow the tracker.

| Entries | Read this | Main topics |
|---|---|---|
| 2, 4, 6 | [Serial input needs real clock edges](HDLBits_Fsm_serialdata_For_Loops_vs_Clock_Cycles.pdf) | Loops, one-bit-per-edge capture, framing recovery and parity |
| 7, 13, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 36, 38 | [Loops, muxes and storage](HDLBits_Combined_Questions_and_Day2_Review.pdf) | Loops, carry wiring, muxes, operators, Lemmings fall count and latches |
| 8 | [HDLC: getting the output cycle right](HDLBits_Fsm_hdlc_Mealy_to_Moore_Deep_Dive.pdf) | Moore/Mealy timing, event states and continuous input |
| 54, 74, 75, 77 | [States, sampled edges and operators](HDLBits_Recovered_Code_Questions_54_74_75_77.pdf) | Water-level history, sampled edges, asynchronous reset and operators |
| 66, 67, 70 | [Bytes, flip-flops and PS/2 packets](HDLBits_Day4_Questions_Vector_DFF_PS2.pdf) | Part-selects, DFF excitation, packet byte timing and done |
| 80 | [Moore serial two's complement](HDLBits_Entry80_Moore_Serial_Twos_Complement_Deep_Dive.pdf) | Why three Moore states are needed and when the output changes |
| 81, 82, 83, 84, 85 | [Day 5 questions and submission notes](HDLBits_Day5_Original_Submissions_Review.pdf) | OR versus addition, concatenation, sticky edges, ring/vibrate and one-hot Mealy encoding |
| 87, 89 | [Dual-edge sampling and Circuit5](HDLBits_Day6_Non_FSM_QA_Dualedge_and_Circuit5.pdf) | Latest-edge selection, DDR resources and waveform-to-mux reasoning |
| 90 | [Counting three-sample groups](HDLBits_Entry90_Exams_2014_Q3FSM_Three_Sample_Window_Deep_Dive.pdf) | Three real samples, old register values and restarting every group |
| 102, 107, 109 | [FSM widths and counter connections](HDLBits_Day7_QA_FSM_Warnings_and_Counter_Interface.pdf) | Width warnings, next-state outputs and the counter hierarchy |
| 123, 127, 129 | [Wire, reg and shift-register reset](HDLBits_Day8_QA_Wire_Reg_and_Shift_Reset.pdf) | Net wiring, reset behavior and BCD clock rollover |
| 155, 158 | [If statements, latches and the 1101 recognizer](HDLBits_Day9_QA_Latches_and_Sequence_FSM.pdf) | Missing assignments, arrival trace, combinational defaults, reg/wire and FSM cleanup |

The [Day 5 Markdown review](HDLBits_Day5_Original_Submissions_Review.md) remains available through its existing tracker links. Its PDF includes the same explanations and historical submission table.

## Verification

The PDFs were checked against the sheet and available source, revised for clearer language, rendered, and visually reviewed. Saved simulations and the additional tests described in [DOCUMENT_REVIEW.md](DOCUMENT_REVIEW.md) passed. The initial document review left the tracker unchanged; the later Day 9 update marked entries 155–158 Done and linked the two new discussions.

## Completion records

The HDLBits website is the authority for platform acceptance. Earlier checkpoints support entries 1-98; Kapil's explicit current-pass completion reports support entries 99-122, with matching Chrome tabs and saved-success records used as evidence. Entries 124-127 and 129-130 are supported by their current Chrome simulation result panels inspected on 5 September 2026; entries 123, 128, 131, 132, 134-140, and 142-144 by their current success panels inspected on 6 September 2026; and entries 133, 146-150, and 152-158 by their current success panels inspected on 7 September 2026. Local simulation is a separate check and was run only where source or a reusable testbench is preserved in this directory; it is not claimed as a local rerun of all accepted submissions. Entries 141, 145, 151, and 159-178 remain Pending.
