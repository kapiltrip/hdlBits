# HDLBits Attempt 2 - document index

**Kapil Tripathi | Verilog and digital design**

13 study PDFs explain the questions behind this second pass through HDLBits. Start with a topic below, browse the collection, or jump to one of the **49 tracker entries with discussion links**. These are study notes based on HDLBits exercises; the original problem statements belong to HDLBits.

[Browse all PDFs](#the-complete-collection) · [Find an entry](#find-a-tracker-entry) · [Tracker](HDLBits_Attempt_2_Tracker_Simple.xlsx) · [Review record](DOCUMENT_REVIEW.md) · [LinkedIn plan](../LinkedIn_Attempt_2_Posting_Plan_and_Ideas.md)

## Start with a question

- **Why does a loop not receive eight serial bits?** [Note 01, pp. 2-7](HDLBits_Fsm_serialdata_For_Loops_vs_Clock_Cycles.pdf#page=2).
- **When do I use generate rather than a procedural loop?** [Note 02, pp. 3-6](HDLBits_Combined_Questions_and_Day2_Review.pdf#page=3).
- **Why does reg not always mean a physical register?** [Note 11, pp. 2-3](HDLBits_Day8_QA_Wire_Reg_and_Shift_Reset.pdf#page=2).
- **How does a missing assignment create a latch?** [Note 12, pp. 2-4](HDLBits_Day9_QA_Latches_and_Sequence_FSM.pdf#page=2).
- **What changes at the Lemmings 20/21-cycle boundary?** [Note 02, pp. 8](HDLBits_Combined_Questions_and_Day2_Review.pdf#page=8).
- **Why does the HDLC output appear in the wrong cycle?** [Note 03, pp. 2-11](HDLBits_Fsm_hdlc_Mealy_to_Moore_Deep_Dive.pdf#page=2).
- **Why does a Moore two's-complement machine need three states?** [Note 06, pp. 2-5](HDLBits_Entry80_Moore_Serial_Twos_Complement_Deep_Dive.pdf#page=2).
- **How do I include the third sample without a gap?** [Note 09, pp. 2-3, 7-10](HDLBits_Entry90_Exams_2014_Q3FSM_Three_Sample_Window_Deep_Dive.pdf#page=2).
- **When are PS/2 packet data and done valid?** [Note 05, pp. 4-6](HDLBits_Day4_Questions_Vector_DFF_PS2.pdf#page=4).
- **Why can OR not select the newest dual-edge sample?** [Note 08, pp. 3-4](HDLBits_Day6_Non_FSM_QA_Dualedge_and_Circuit5.pdf#page=3).
- **How do I read FSM width warnings and counter wiring?** [Note 10, pp. 2-5](HDLBits_Day7_QA_FSM_Warnings_and_Counter_Interface.pdf#page=2).
- **How should the 1101 recognizer hold its result?** [Note 12, pp. 5-6](HDLBits_Day9_QA_Latches_and_Sequence_FSM.pdf#page=5).
- **What is different about reduction, bitwise and logical operators?** [Note 04, pp. 5](HDLBits_Recovered_Code_Questions_54_74_75_77.pdf#page=5).
- **Why does Kmap4 use | instead of +?** [Note 13, pp. 2-3](HDLBits_Day10_Kmaps_Boolean_Forms_and_Rules90_110.pdf#page=2).
- **What are SOP, POS and De Morgan's law, and why do I need them?** [Note 13, pp. 4-5](HDLBits_Day10_Kmaps_Boolean_Forms_and_Rules90_110.pdf#page=4).
- **Why did I use nextVal in Rule 90, and is it required?** [Note 13, pp. 6-7](HDLBits_Day10_Kmaps_Boolean_Forms_and_Rules90_110.pdf#page=6).
- **How does the Rule 110 expression match its truth table?** [Note 13, pp. 8-9](HDLBits_Day10_Kmaps_Boolean_Forms_and_Rules90_110.pdf#page=8).
- **Which small mistakes explain sticky capture and one-hot encoding?** [Note 07, pp. 5-7](HDLBits_Day5_Original_Submissions_Review.pdf#page=5).

## The complete collection

Note numbers are catalogue identifiers, separate from tracker entries and posting days. Older day labels remain in filenames so existing links keep working.

| Note | PDF | Pages | What it explains |
|---|---|---:|---|
| 01 | [Serial input needs real clock edges](HDLBits_Fsm_serialdata_For_Loops_vs_Clock_Cycles.pdf) | 11 | From the original for-loop mistake to one-bit-per-edge capture, complete frames and odd-parity timing. |
| 02 | [Loops, muxes and storage](HDLBits_Combined_Questions_and_Day2_Review.pdf) | 12 | Connect Verilog statements to the hardware they describe: vector loops, carry chains, mux selection, operators and storage. |
| 03 | [HDLC: get the output cycle right](HDLBits_Fsm_hdlc_Mealy_to_Moore_Deep_Dive.pdf) | 16 | Follow discard, flag and error detection from the first attempts through a working Moore machine and timing traces. |
| 04 | [States, sampled edges and operators](HDLBits_Recovered_Code_Questions_54_74_75_77.pdf) | 6 | Four questions from saved submissions: remembered history, sampled edges, asynchronous reset and operator classes. |
| 05 | [Bytes, flip-flops and PS/2 packets](HDLBits_Day4_Questions_Vector_DFF_PS2.pdf) | 6 | Choose the right bits, capture them at the right edge, and follow a three-byte packet until its data becomes valid. |
| 06 | [Two's complement, one bit at a time](HDLBits_Entry80_Moore_Serial_Twos_Complement_Deep_Dive.pdf) | 8 | Understand the LSB-first algorithm, why the Moore machine needs three states, and what each transition remembers. |
| 07 | [Small RTL mistakes, explained](HDLBits_Day5_Original_Submissions_Review.pdf) | 12 | Day 5 questions and submission notes: operators, concatenation width, sticky edge capture and one-hot Mealy encoding. |
| 08 | [Dual-edge sampling and waveform reasoning](HDLBits_Day6_Non_FSM_QA_Dualedge_and_Circuit5.pdf) | 19 | Select the newest sample, distinguish simulation from FPGA implementation, and infer Circuit5 from its waveform. |
| 09 | [Three samples, no wasted cycle](HDLBits_Entry90_Exams_2014_Q3FSM_Three_Sample_Window_Deep_Dive.pdf) | 12 | Separate controller state, sample position and accumulated data, then follow adjacent three-sample groups without gaps. |
| 10 | [FSM widths and counter connections](HDLBits_Day7_QA_FSM_Warnings_and_Counter_Interface.pdf) | 7 | Read truncation warnings, derive next-state bits, and trace each control signal through a parent and child counter. |
| 11 | [Wire, reg and reset behavior](HDLBits_Day8_QA_Wire_Reg_and_Shift_Reset.pdf) | 6 | Distinguish a continuous connection from initialization, follow a carry wire, and check shift-register and BCD-clock reset. |
| 12 | [Missing assignments and the 1101 FSM](HDLBits_Day9_QA_Latches_and_Sequence_FSM.pdf) | 6 | Trace the latch created by a missing assignment, then follow a five-state recognizer with detection held until reset. |
| 13 | [K-map operators, Boolean forms and cellular automata](HDLBits_Day10_Kmaps_Boolean_Forms_and_Rules90_110.pdf) | 9 | Connect four Day 10 questions: operator intent in Kmap4, equivalent SOP/POS forms, and simultaneous next-state logic in Rules 90 and 110. |

Each PDF has a clickable contents page, section and tracker-entry bookmarks, embedded fonts, a consistent page counter, and **Contents / All notes** links in the footer. Text and diagrams remain searchable/vector content where present in the source. Page numbers here match the printed counter and physical PDF page.

Page-fragment links (`#page=N`) work in supporting PDF viewers. If GitHub's preview ignores the fragment, download the PDF and use its contents page, bookmarks or printed page number. The contents labels and page numbers also work as a visual guide in document previews that do not support links.

## Find a tracker entry

Entry numbers below come from the revision tracker, not the HDLBits website's ordering. Shared PDFs answer multiple questions. The workbook is the source for progress; this index does not announce completion.

| Entry | HDLBits problem | Note and answer pages |
|---:|---|---|
| 2 | [Serial receiver](https://hdlbits.01xz.net/wiki/fsm_serial) | [Note 01, pp. 2-10](HDLBits_Fsm_serialdata_For_Loops_vs_Clock_Cycles.pdf#page=2) |
| 4 | [Serial receiver and datapath](https://hdlbits.01xz.net/wiki/fsm_serialdata) | [Note 01, pp. 2-10](HDLBits_Fsm_serialdata_For_Loops_vs_Clock_Cycles.pdf#page=2) |
| 6 | [Serial receiver with parity checking](https://hdlbits.01xz.net/wiki/fsm_serialdp) | [Note 01, pp. 10-11](HDLBits_Fsm_serialdata_For_Loops_vs_Clock_Cycles.pdf#page=10) |
| 7 | [Lemmings 4](https://hdlbits.01xz.net/wiki/lemmings4) | [Note 02, pp. 8](HDLBits_Combined_Questions_and_Day2_Review.pdf#page=8) |
| 8 | [Sequence recognition](https://hdlbits.01xz.net/wiki/fsm_hdlc) | [Note 03, pp. 2-16](HDLBits_Fsm_hdlc_Mealy_to_Moore_Deep_Dive.pdf#page=2) |
| 13 | [Mux](https://hdlbits.01xz.net/wiki/bugs_mux2) | [Note 02, pp. 7](HDLBits_Combined_Questions_and_Day2_Review.pdf#page=7) |
| 19 | [DFF with reset](https://hdlbits.01xz.net/wiki/dff8r) | [Note 02, pp. 2, 9](HDLBits_Combined_Questions_and_Day2_Review.pdf#page=2) |
| 20 | [Simple wire](https://hdlbits.01xz.net/wiki/wire) | [Note 02, pp. 2, 9](HDLBits_Combined_Questions_and_Day2_Review.pdf#page=2) |
| 21 | [NAND](https://hdlbits.01xz.net/wiki/bugs_nand3) | [Note 02, pp. 2, 9](HDLBits_Combined_Questions_and_Day2_Review.pdf#page=2) |
| 22 | [Simple FSM 2 (asynchronous reset)](https://hdlbits.01xz.net/wiki/fsm2) | [Note 02, pp. 2, 9](HDLBits_Combined_Questions_and_Day2_Review.pdf#page=2) |
| 23 | [Combinational for-loop: Vector reversal 2](https://hdlbits.01xz.net/wiki/vector100r) | [Note 02, pp. 3-4](HDLBits_Combined_Questions_and_Day2_Review.pdf#page=3) |
| 24 | [DFF with reset value](https://hdlbits.01xz.net/wiki/dff8p) | [Note 02, pp. 2, 9](HDLBits_Combined_Questions_and_Day2_Review.pdf#page=2) |
| 25 | [Four wires](https://hdlbits.01xz.net/wiki/wire4) | [Note 02, pp. 2, 9](HDLBits_Combined_Questions_and_Day2_Review.pdf#page=2) |
| 26 | [Combinational for-loop: 255-bit population count](https://hdlbits.01xz.net/wiki/popcount255) | [Note 02, pp. 3, 6](HDLBits_Combined_Questions_and_Day2_Review.pdf#page=3) |
| 27 | [Simple FSM 2 (synchronous reset)](https://hdlbits.01xz.net/wiki/fsm2s) | [Note 02, pp. 2, 9](HDLBits_Combined_Questions_and_Day2_Review.pdf#page=2) |
| 28 | [DFF with asynchronous reset](https://hdlbits.01xz.net/wiki/dff8ar) | [Note 02, pp. 2, 9](HDLBits_Combined_Questions_and_Day2_Review.pdf#page=2) |
| 29 | [Mux](https://hdlbits.01xz.net/wiki/bugs_mux4) | [Note 02, pp. 7](HDLBits_Combined_Questions_and_Day2_Review.pdf#page=7) |
| 30 | [Generate for-loop: 100-bit binary adder 2](https://hdlbits.01xz.net/wiki/adder100i) | [Note 02, pp. 5](HDLBits_Combined_Questions_and_Day2_Review.pdf#page=5) |
| 31 | [Inverter](https://hdlbits.01xz.net/wiki/notgate) | [Note 02, pp. 10](HDLBits_Combined_Questions_and_Day2_Review.pdf#page=10) |
| 36 | [Add/sub](https://hdlbits.01xz.net/wiki/bugs_addsubz) | [Note 02, pp. 11](HDLBits_Combined_Questions_and_Day2_Review.pdf#page=11) |
| 38 | [D Latch](https://hdlbits.01xz.net/wiki/exams/m2014_q4a) | [Note 02, pp. 12](HDLBits_Combined_Questions_and_Day2_Review.pdf#page=12) |
| 54 | [Design a Moore FSM](https://hdlbits.01xz.net/wiki/exams/ece241_2013_q4) | [Note 04, pp. 2](HDLBits_Recovered_Code_Questions_54_74_75_77.pdf#page=2) |
| 66 | [DFFs and gates](https://hdlbits.01xz.net/wiki/exams/ece241_2014_q4) | [Note 05, pp. 3](HDLBits_Day4_Questions_Vector_DFF_PS2.pdf#page=3) |
| 67 | [Vector part select](https://hdlbits.01xz.net/wiki/vector2) | [Note 05, pp. 2-3](HDLBits_Day4_Questions_Vector_DFF_PS2.pdf#page=2) |
| 70 | [PS/2 packet parser and datapath](https://hdlbits.01xz.net/wiki/fsm_ps2data) | [Note 05, pp. 4-6](HDLBits_Day4_Questions_Vector_DFF_PS2.pdf#page=4) |
| 74 | [Detect an edge](https://hdlbits.01xz.net/wiki/edgedetect) | [Note 04, pp. 3](HDLBits_Recovered_Code_Questions_54_74_75_77.pdf#page=3) |
| 75 | [Q8: Design a Mealy FSM](https://hdlbits.01xz.net/wiki/exams/ece241_2013_q8) | [Note 04, pp. 4](HDLBits_Recovered_Code_Questions_54_74_75_77.pdf#page=4) |
| 77 | [Four-input gates](https://hdlbits.01xz.net/wiki/gates4) | [Note 04, pp. 5](HDLBits_Recovered_Code_Questions_54_74_75_77.pdf#page=5) |
| 80 | [Q5a: Serial two's complementer (Moore FSM)](https://hdlbits.01xz.net/wiki/exams/ece241_2014_q5a) | [Note 06, pp. 2-8](HDLBits_Entry80_Moore_Serial_Twos_Complement_Deep_Dive.pdf#page=2) |
| 81 | [Combinational circuit 4](https://hdlbits.01xz.net/wiki/sim/circuit4) | [Note 07, pp. 5](HDLBits_Day5_Original_Submissions_Review.pdf#page=5) |
| 82 | [Vector concatenation operator](https://hdlbits.01xz.net/wiki/vector3) | [Note 07, pp. 5](HDLBits_Day5_Original_Submissions_Review.pdf#page=5) |
| 83 | [Edge capture register](https://hdlbits.01xz.net/wiki/edgecapture) | [Note 07, pp. 6](HDLBits_Day5_Original_Submissions_Review.pdf#page=6) |
| 84 | [Ring or vibrate?](https://hdlbits.01xz.net/wiki/ringer) | [Note 07, pp. 6](HDLBits_Day5_Original_Submissions_Review.pdf#page=6) |
| 85 | [Q5b: Serial two's complementer (Mealy FSM)](https://hdlbits.01xz.net/wiki/exams/ece241_2014_q5b) | [Note 07, pp. 6-7](HDLBits_Day5_Original_Submissions_Review.pdf#page=6) |
| 87 | [Dual-edge triggered flip-flop](https://hdlbits.01xz.net/wiki/dualedge) | [Note 08, pp. 3-14](HDLBits_Day6_Non_FSM_QA_Dualedge_and_Circuit5.pdf#page=3) |
| 89 | [Combinational circuit 5](https://hdlbits.01xz.net/wiki/sim/circuit5) | [Note 08, pp. 15-17](HDLBits_Day6_Non_FSM_QA_Dualedge_and_Circuit5.pdf#page=15) |
| 90 | [Q3a: FSM](https://hdlbits.01xz.net/wiki/exams/2014_q3fsm) | [Note 09, pp. 2-12](HDLBits_Entry90_Exams_2014_Q3FSM_Three_Sample_Window_Deep_Dive.pdf#page=2) |
| 102 | [Q3c: FSM logic](https://hdlbits.01xz.net/wiki/exams/2014_q3c) | [Note 10, pp. 2-3](HDLBits_Day7_QA_FSM_Warnings_and_Counter_Interface.pdf#page=2) |
| 107 | [Q6b: FSM next-state logic](https://hdlbits.01xz.net/wiki/exams/m2014_q6b) | [Note 10, pp. 4](HDLBits_Day7_QA_FSM_Warnings_and_Counter_Interface.pdf#page=4) |
| 109 | [Counter 1-12](https://hdlbits.01xz.net/wiki/exams/ece241_2014_q7a) | [Note 10, pp. 5](HDLBits_Day7_QA_FSM_Warnings_and_Counter_Interface.pdf#page=5) |
| 123 | [12-hour clock](https://hdlbits.01xz.net/wiki/count_clock) | [Note 11, pp. 5-6](HDLBits_Day8_QA_Wire_Reg_and_Shift_Reset.pdf#page=5) |
| 127 | [4-bit shift register](https://hdlbits.01xz.net/wiki/shift4) | [Note 11, pp. 4](HDLBits_Day8_QA_Wire_Reg_and_Shift_Reset.pdf#page=4) |
| 129 | [Adder 2](https://hdlbits.01xz.net/wiki/module_fadd) | [Note 11, pp. 2-3](HDLBits_Day8_QA_Wire_Reg_and_Shift_Reset.pdf#page=2) |
| 155 | [FSM: Sequence 1101 recognizer](https://hdlbits.01xz.net/wiki/exams/review2015_fsmseq) | [Note 12, pp. 5-6](HDLBits_Day9_QA_Latches_and_Sequence_FSM.pdf#page=5) |
| 158 | [If statement latches](https://hdlbits.01xz.net/wiki/always_if2) | [Note 12, pp. 2-4](HDLBits_Day9_QA_Latches_and_Sequence_FSM.pdf#page=2) |
| 161 | [4-variable](https://hdlbits.01xz.net/wiki/kmap4) | [Note 13, pp. 2-3](HDLBits_Day10_Kmaps_Boolean_Forms_and_Rules90_110.pdf#page=2) |
| 164 | [Minimum SOP and POS](https://hdlbits.01xz.net/wiki/exams/ece241_2013_q2) | [Note 13, pp. 4-5](HDLBits_Day10_Kmaps_Boolean_Forms_and_Rules90_110.pdf#page=4) |
| 168 | [Rule 90](https://hdlbits.01xz.net/wiki/rule90) | [Note 13, pp. 6-7](HDLBits_Day10_Kmaps_Boolean_Forms_and_Rules90_110.pdf#page=6) |
| 172 | [Rule 110](https://hdlbits.01xz.net/wiki/rule110) | [Note 13, pp. 8-9](HDLBits_Day10_Kmaps_Boolean_Forms_and_Rules90_110.pdf#page=8) |

The [Day 5 Markdown review](HDLBits_Day5_Original_Submissions_Review.md) is an alternative to Note 07 and has its own section index. Its historical submission appendix preserves the original evidence and dates.

## Sharing and revision

For a LinkedIn attachment, use the reader-facing title on the PDF cover. For a focused post, choose one question and its trace or counterexample; the full note supplies the surrounding explanation and sources. The [posting plan](../LinkedIn_Attempt_2_Posting_Plan_and_Ideas.md) maps these notes to the proposed series.

For revision, try the linked problem before opening the explanation. Then check the state meaning, sampling edge, bit width, reset and boundary case that mattered. The [review record](DOCUMENT_REVIEW.md) distinguishes earlier RTL checks from this indexing and layout update.
