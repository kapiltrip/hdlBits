# HDLBits Attempt 2 - day-wise reading index

**Kapil Tripathi | Verilog and digital design**

One reading PDF per day, across **10 days**. Related short notes are combined; original questions, complete code, diagrams, traces and historical evidence stay with their explanations. Day 10 holds all the later series and ends with an LFSR definition/reference section.

[Find a question](#find-a-question) · [Choose a day](#choose-a-day) · [Find an entry](#find-a-tracker-entry) · [Tracker](HDLBits_Attempt_2_Tracker_Simple.xlsx)

## Find a question


### Day 1

- [Why does the serial loop sample only one input value?](output/pdf/HDLBits_Day_01.pdf#page=3) - p. 3.
- [Which HDLC patterns must be reported, and when?](output/pdf/HDLBits_Day_01.pdf#page=13) - p. 13.

### Day 2

- [When do I need genvar and elaboration?](output/pdf/HDLBits_Day_02.pdf#page=3) - p. 3.
- [Why use bitwise operators, and how do mux selectors divide work?](output/pdf/HDLBits_Day_02.pdf#page=7) - p. 7.
- [Why does the Lemmings counter not need another reset?](output/pdf/HDLBits_Day_02.pdf#page=8) - p. 8.

### Day 3

- [Why does an incomplete assignment intentionally create a latch?](output/pdf/HDLBits_Day_03.pdf#page=2) - p. 2.
- [Why can water-level inputs not replace FSM history?](output/pdf/HDLBits_Day_03.pdf#page=3) - p. 3.

### Day 4

- [What do +: and -: mean in an indexed part-select?](output/pdf/HDLBits_Day_04.pdf#page=2) - p. 2.
- [Why must a clocked PS/2 data register hold unmatched bytes?](output/pdf/HDLBits_Day_04.pdf#page=4) - p. 4.

### Day 5

- [Does edge detection compare two consecutive clock samples?](output/pdf/HDLBits_Day_05.pdf#page=3) - p. 3.
- [How do reduction, bitwise and logical operators differ?](output/pdf/HDLBits_Day_05.pdf#page=5) - p. 5.
- [Why does the Moore complementer need three states?](output/pdf/HDLBits_Day_05.pdf#page=8) - p. 8.
- [How do sticky capture, ring/vibrate and one-hot state work?](output/pdf/HDLBits_Day_05.pdf#page=18) - p. 18.

### Day 6

- [Why can OR not select the newest dual-edge sample?](output/pdf/HDLBits_Day_06.pdf#page=4) - p. 4.
- [Why must the third decision include the current input?](output/pdf/HDLBits_Day_06.pdf#page=27) - p. 27.

### Day 7

- [What does the width warning mean in the problem map?](output/pdf/HDLBits_Day_07.pdf#page=2) - p. 2.
- [How do load, enable and data connect to the counter?](output/pdf/HDLBits_Day_07.pdf#page=5) - p. 5.

### Day 8

- [Why can this continuously driven wire not be a reg initializer?](output/pdf/HDLBits_Day_08.pdf#page=2) - p. 2.
- [Why does reset belong in the shift-register storage block?](output/pdf/HDLBits_Day_08.pdf#page=4) - p. 4.

### Day 9

- [Why must combinational outputs be assigned on every path?](output/pdf/HDLBits_Day_09.pdf#page=2) - p. 2.
- [How should I write the complete 1101 recognizer?](output/pdf/HDLBits_Day_09.pdf#page=5) - p. 5.

### Day 10

- [Why does the K-map expression use | instead of +?](output/pdf/HDLBits_Day_10.pdf#page=4) - p. 4.
- [What are SOP, POS and De Morgan's law?](output/pdf/HDLBits_Day_10.pdf#page=6) - p. 6.
- [Why did I use nextVal, and is it required?](output/pdf/HDLBits_Day_10.pdf#page=9) - p. 9.
- [Why does the Rule 110 expression match the truth table?](output/pdf/HDLBits_Day_10.pdf#page=11) - p. 11.
- [How do I get four capture cycles without multiple drivers?](output/pdf/HDLBits_Day_10.pdf#page=17) - p. 17.
- [When should the clocked block inspect state, next_state or both?](output/pdf/HDLBits_Day_10.pdf#page=21) - p. 21.
- [Why does the fourth captured bit need old delay plus current data?](output/pdf/HDLBits_Day_10.pdf#page=22) - p. 22.
- [Why does tap position k become Verilog index k-1?](output/pdf/HDLBits_Day_10.pdf#page=28) - p. 28.
- [How do I translate the Mt2015 schematic into D-input equations?](output/pdf/HDLBits_Day_10.pdf#page=31) - p. 31.
- [Why do the XORs read old q rather than a partly shifted q?](output/pdf/HDLBits_Day_10.pdf#page=35) - p. 35.
- [Why is a Conway cell at row * 16 + col?](output/pdf/HDLBits_Day_10.pdf#page=37) - p. 37.
- [Why must every neighbor come from the old generation?](output/pdf/HDLBits_Day_10.pdf#page=39) - p. 39.
- [What is an LFSR, and what do seed, tap, period and lockup mean?](output/pdf/HDLBits_Day_10.pdf#page=43) - p. 43.
- [How do feedback forms and tap choices determine the period?](output/pdf/HDLBits_Day_10.pdf#page=44) - p. 44.
- [Where are LFSRs useful, and how should I code their state?](output/pdf/HDLBits_Day_10.pdf#page=45) - p. 45.


## Choose a day

Reading days follow the review sequence, not a new completion calendar. The tracker retains its original day labels: an exercise can be revisited in a later reading day. Earlier mixed notes were grouped by topic; the Day 2-3 latch page is now with state history on Day 3. All later K-map, timer, LFSR and Conway material is together on Day 10, as requested.

| Day | Open the combined PDF | Pages | Contents |
|---:|---|---:|---|
| 1 | [Serial reception and HDLC timing](output/pdf/HDLBits_Day_01.pdf) | 27 | Capture bits on real edges, assemble complete frames, and place pattern outputs in the required cycle. |
| 2 | [Loops, muxes and Verilog operators](output/pdf/HDLBits_Day_02.pdf) | 11 | Procedural and generate loops, carry wiring, population count, mux selection and the Lemmings boundary. |
| 3 | [Latch storage and state history](output/pdf/HDLBits_Day_03.pdf) | 3 | Two small explanations together: intentional latch storage and why current water-level inputs cannot replace state history. |
| 4 | [Vectors, flip-flops and PS/2 packets](output/pdf/HDLBits_Day_04.pdf) | 6 | Indexed byte slices, D-input equations and packet data ownership, with complete code and clock traces. |
| 5 | [Sampled edges, serial complement and RTL questions](output/pdf/HDLBits_Day_05.pdf) | 24 | Keep the recovered questions, detailed Moore complementer, small RTL mistakes and dated submission evidence together. |
| 6 | [Dual-edge sampling and three-sample FSMs](output/pdf/HDLBits_Day_06.pdf) | 31 | Read waveforms, distinguish FPGA resources from simulation behavior, and include the third sample without losing a cycle. |
| 7 | [FSM widths and counter connections](output/pdf/HDLBits_Day_07.pdf) | 7 | Interpret width warnings, derive next-state bits and trace load, enable and data through a counter interface. |
| 8 | [Wire, reg and reset behavior](output/pdf/HDLBits_Day_08.pdf) | 6 | Separate wiring from initialization, understand stored values and check shift-register and BCD-clock reset behavior. |
| 9 | [Missing assignments and the 1101 FSM](output/pdf/HDLBits_Day_09.pdf) | 6 | Trace accidental latch behavior and review the five-state recognizer before its later use in the timer series. |
| 10 | [Boolean forms, timers, LFSRs and Conway](output/pdf/HDLBits_Day_10.pdf) | 45 | The final connected series: K-maps, Rules 90 and 110, timer control, three LFSRs and Conway. End with an LFSR definitions and revision reference. |

Each PDF has one reading cover, clickable contents, hierarchical bookmarks, continuous page numbering and **Contents / All days** footer links. Larger days also have a detailed section index. The displayed page numbers match physical PDF pages.

For reliable page jumps, download a PDF and use its built-in contents or bookmarks. Links ending in `#page=N` work in supporting PDF viewers; GitHub previews may ignore the page fragment.


## Find a tracker entry

58 entries have discussion links. The 1101 explanation is intentionally revisited in the timer series; both locations are listed. Entries without a question remain in the tracker, without invented notes.

| Entry | Problem | Tracker day | Answer location |
|---:|---|---|---|
| 2 | [Serial receiver](https://hdlbits.01xz.net/wiki/fsm_serial) | Day 1 | [Day 1, pp. 3-11](output/pdf/HDLBits_Day_01.pdf#page=3) |
| 4 | [Serial receiver and datapath](https://hdlbits.01xz.net/wiki/fsm_serialdata) | Day 1 | [Day 1, pp. 3-11](output/pdf/HDLBits_Day_01.pdf#page=3) |
| 6 | [Serial receiver with parity checking](https://hdlbits.01xz.net/wiki/fsm_serialdp) | Day 1 | [Day 1, pp. 11-12](output/pdf/HDLBits_Day_01.pdf#page=11) |
| 7 | [Lemmings 4](https://hdlbits.01xz.net/wiki/lemmings4) | Day 1 | [Day 2, pp. 8](output/pdf/HDLBits_Day_02.pdf#page=8) |
| 8 | [Sequence recognition](https://hdlbits.01xz.net/wiki/fsm_hdlc) | Day 1 | [Day 1, pp. 13-27](output/pdf/HDLBits_Day_01.pdf#page=13) |
| 13 | [Mux](https://hdlbits.01xz.net/wiki/bugs_mux2) | Day 1 | [Day 2, pp. 7](output/pdf/HDLBits_Day_02.pdf#page=7) |
| 19 | [DFF with reset](https://hdlbits.01xz.net/wiki/dff8r) | Day 2 | [Day 2, pp. 2, 9](output/pdf/HDLBits_Day_02.pdf#page=2) |
| 20 | [Simple wire](https://hdlbits.01xz.net/wiki/wire) | Day 2 | [Day 2, pp. 2, 9](output/pdf/HDLBits_Day_02.pdf#page=2) |
| 21 | [NAND](https://hdlbits.01xz.net/wiki/bugs_nand3) | Day 2 | [Day 2, pp. 2, 9](output/pdf/HDLBits_Day_02.pdf#page=2) |
| 22 | [Simple FSM 2 (asynchronous reset)](https://hdlbits.01xz.net/wiki/fsm2) | Day 2 | [Day 2, pp. 2, 9](output/pdf/HDLBits_Day_02.pdf#page=2) |
| 23 | [Combinational for-loop: Vector reversal 2](https://hdlbits.01xz.net/wiki/vector100r) | Day 2 | [Day 2, pp. 3-4](output/pdf/HDLBits_Day_02.pdf#page=3) |
| 24 | [DFF with reset value](https://hdlbits.01xz.net/wiki/dff8p) | Day 2 | [Day 2, pp. 2, 9](output/pdf/HDLBits_Day_02.pdf#page=2) |
| 25 | [Four wires](https://hdlbits.01xz.net/wiki/wire4) | Day 2 | [Day 2, pp. 2, 9](output/pdf/HDLBits_Day_02.pdf#page=2) |
| 26 | [Combinational for-loop: 255-bit population count](https://hdlbits.01xz.net/wiki/popcount255) | Day 2 | [Day 2, pp. 3, 6](output/pdf/HDLBits_Day_02.pdf#page=3) |
| 27 | [Simple FSM 2 (synchronous reset)](https://hdlbits.01xz.net/wiki/fsm2s) | Day 2 | [Day 2, pp. 2, 9](output/pdf/HDLBits_Day_02.pdf#page=2) |
| 28 | [DFF with asynchronous reset](https://hdlbits.01xz.net/wiki/dff8ar) | Day 2 | [Day 2, pp. 2, 9](output/pdf/HDLBits_Day_02.pdf#page=2) |
| 29 | [Mux](https://hdlbits.01xz.net/wiki/bugs_mux4) | Day 2 | [Day 2, pp. 7](output/pdf/HDLBits_Day_02.pdf#page=7) |
| 30 | [Generate for-loop: 100-bit binary adder 2](https://hdlbits.01xz.net/wiki/adder100i) | Day 2 | [Day 2, pp. 5](output/pdf/HDLBits_Day_02.pdf#page=5) |
| 31 | [Inverter](https://hdlbits.01xz.net/wiki/notgate) | Day 2 | [Day 2, pp. 10](output/pdf/HDLBits_Day_02.pdf#page=10) |
| 36 | [Add/sub](https://hdlbits.01xz.net/wiki/bugs_addsubz) | Day 2 | [Day 2, pp. 11](output/pdf/HDLBits_Day_02.pdf#page=11) |
| 38 | [D Latch](https://hdlbits.01xz.net/wiki/exams/m2014_q4a) | Day 3 | [Day 3, pp. 2](output/pdf/HDLBits_Day_03.pdf#page=2) |
| 54 | [Design a Moore FSM](https://hdlbits.01xz.net/wiki/exams/ece241_2013_q4) | Day 3 | [Day 3, pp. 3](output/pdf/HDLBits_Day_03.pdf#page=3) |
| 66 | [DFFs and gates](https://hdlbits.01xz.net/wiki/exams/ece241_2014_q4) | Day 4 | [Day 4, pp. 3](output/pdf/HDLBits_Day_04.pdf#page=3) |
| 67 | [Vector part select](https://hdlbits.01xz.net/wiki/vector2) | Day 4 | [Day 4, pp. 2-3](output/pdf/HDLBits_Day_04.pdf#page=2) |
| 70 | [PS/2 packet parser and datapath](https://hdlbits.01xz.net/wiki/fsm_ps2data) | Day 4 | [Day 4, pp. 4-6](output/pdf/HDLBits_Day_04.pdf#page=4) |
| 74 | [Detect an edge](https://hdlbits.01xz.net/wiki/edgedetect) | Day 5 | [Day 5, pp. 3](output/pdf/HDLBits_Day_05.pdf#page=3) |
| 75 | [Q8: Design a Mealy FSM](https://hdlbits.01xz.net/wiki/exams/ece241_2013_q8) | Day 5 | [Day 5, pp. 4](output/pdf/HDLBits_Day_05.pdf#page=4) |
| 77 | [Four-input gates](https://hdlbits.01xz.net/wiki/gates4) | Day 5 | [Day 5, pp. 5](output/pdf/HDLBits_Day_05.pdf#page=5) |
| 80 | [Q5a: Serial two's complementer (Moore FSM)](https://hdlbits.01xz.net/wiki/exams/ece241_2014_q5a) | Day 5 | [Day 5, pp. 7-13](output/pdf/HDLBits_Day_05.pdf#page=7) |
| 81 | [Combinational circuit 4](https://hdlbits.01xz.net/wiki/sim/circuit4) | Day 5 | [Day 5, pp. 17](output/pdf/HDLBits_Day_05.pdf#page=17) |
| 82 | [Vector concatenation operator](https://hdlbits.01xz.net/wiki/vector3) | Day 5 | [Day 5, pp. 17](output/pdf/HDLBits_Day_05.pdf#page=17) |
| 83 | [Edge capture register](https://hdlbits.01xz.net/wiki/edgecapture) | Day 5 | [Day 5, pp. 18](output/pdf/HDLBits_Day_05.pdf#page=18) |
| 84 | [Ring or vibrate?](https://hdlbits.01xz.net/wiki/ringer) | Day 5 | [Day 5, pp. 18](output/pdf/HDLBits_Day_05.pdf#page=18) |
| 85 | [Q5b: Serial two's complementer (Mealy FSM)](https://hdlbits.01xz.net/wiki/exams/ece241_2014_q5b) | Day 5 | [Day 5, pp. 18-19](output/pdf/HDLBits_Day_05.pdf#page=18) |
| 87 | [Dual-edge triggered flip-flop](https://hdlbits.01xz.net/wiki/dualedge) | Day 5 | [Day 6, pp. 4-15](output/pdf/HDLBits_Day_06.pdf#page=4) |
| 89 | [Combinational circuit 5](https://hdlbits.01xz.net/wiki/sim/circuit5) | Day 5 | [Day 6, pp. 16-18](output/pdf/HDLBits_Day_06.pdf#page=16) |
| 90 | [Q3a: FSM](https://hdlbits.01xz.net/wiki/exams/2014_q3fsm) | Day 6 | [Day 6, pp. 21-31](output/pdf/HDLBits_Day_06.pdf#page=21) |
| 102 | [Q3c: FSM logic](https://hdlbits.01xz.net/wiki/exams/2014_q3c) | Day 6 | [Day 7, pp. 2-3](output/pdf/HDLBits_Day_07.pdf#page=2) |
| 107 | [Q6b: FSM next-state logic](https://hdlbits.01xz.net/wiki/exams/m2014_q6b) | Day 6 | [Day 7, pp. 4](output/pdf/HDLBits_Day_07.pdf#page=4) |
| 109 | [Counter 1-12](https://hdlbits.01xz.net/wiki/exams/ece241_2014_q7a) | Day 7 | [Day 7, pp. 5](output/pdf/HDLBits_Day_07.pdf#page=5) |
| 123 | [12-hour clock](https://hdlbits.01xz.net/wiki/count_clock) | Day 7 | [Day 8, pp. 5-6](output/pdf/HDLBits_Day_08.pdf#page=5) |
| 127 | [4-bit shift register](https://hdlbits.01xz.net/wiki/shift4) | Day 8 | [Day 8, pp. 4](output/pdf/HDLBits_Day_08.pdf#page=4) |
| 129 | [Adder 2](https://hdlbits.01xz.net/wiki/module_fadd) | Day 8 | [Day 8, pp. 2-3](output/pdf/HDLBits_Day_08.pdf#page=2) |
| 141 | [5-bit LFSR](https://hdlbits.01xz.net/wiki/lfsr5) | Day 8 | [Day 10, pp. 27-30](output/pdf/HDLBits_Day_10.pdf#page=27) |
| 144 | [Counter with period 1000](https://hdlbits.01xz.net/wiki/exams/review2015_count1k) | Day 9 | [Day 10, pp. 13](output/pdf/HDLBits_Day_10.pdf#page=13) |
| 145 | [3-bit LFSR](https://hdlbits.01xz.net/wiki/mt2015_lfsr) | Day 9 | [Day 10, pp. 31-33](output/pdf/HDLBits_Day_10.pdf#page=31) |
| 149 | [4-bit shift register and down counter](https://hdlbits.01xz.net/wiki/exams/review2015_shiftcount) | Day 9 | [Day 10, pp. 14-15](output/pdf/HDLBits_Day_10.pdf#page=14) |
| 151 | [32-bit LFSR](https://hdlbits.01xz.net/wiki/lfsr32) | Day 9 | [Day 10, pp. 34-35](output/pdf/HDLBits_Day_10.pdf#page=34) |
| 155 | [FSM: Sequence 1101 recognizer](https://hdlbits.01xz.net/wiki/exams/review2015_fsmseq) | Day 9 | [Day 9, pp. 5-6 (earlier question)](output/pdf/HDLBits_Day_09.pdf#page=5); [Day 10, pp. 16](output/pdf/HDLBits_Day_10.pdf#page=16) |
| 158 | [If statement latches](https://hdlbits.01xz.net/wiki/always_if2) | Day 9 | [Day 9, pp. 2-4](output/pdf/HDLBits_Day_09.pdf#page=2) |
| 160 | [FSM: Enable shift register](https://hdlbits.01xz.net/wiki/exams/review2015_fsmshift) | Day 9 | [Day 10, pp. 17](output/pdf/HDLBits_Day_10.pdf#page=17) |
| 161 | [4-variable](https://hdlbits.01xz.net/wiki/kmap4) | Day 9 | [Day 10, pp. 4-5](output/pdf/HDLBits_Day_10.pdf#page=4) |
| 164 | [Minimum SOP and POS](https://hdlbits.01xz.net/wiki/exams/ece241_2013_q2) | Day 10 | [Day 10, pp. 6-7](output/pdf/HDLBits_Day_10.pdf#page=6) |
| 165 | [FSM: The complete FSM](https://hdlbits.01xz.net/wiki/exams/review2015_fsm) | Day 10 | [Day 10, pp. 18-21](output/pdf/HDLBits_Day_10.pdf#page=18) |
| 168 | [Rule 90](https://hdlbits.01xz.net/wiki/rule90) | Day 10 | [Day 10, pp. 8-9](output/pdf/HDLBits_Day_10.pdf#page=8) |
| 170 | [The complete timer](https://hdlbits.01xz.net/wiki/exams/review2015_fancytimer) | Day 10 | [Day 10, pp. 22-25](output/pdf/HDLBits_Day_10.pdf#page=22) |
| 172 | [Rule 110](https://hdlbits.01xz.net/wiki/rule110) | Day 10 | [Day 10, pp. 10-11](output/pdf/HDLBits_Day_10.pdf#page=10) |
| 177 | [Conway's Game of Life 16x16](https://hdlbits.01xz.net/wiki/conwaylife) | Day 10 | [Day 10, pp. 37-42](output/pdf/HDLBits_Day_10.pdf#page=37) |

## Sources and review records

The original 16 PDFs remain unchanged at their existing paths for compatibility and reproducibility; the ten day-wise files above are the primary reading set. No technical source page was discarded. Original PDF page references in historical appendices identify those retained sources unless explicitly updated to a day-wise destination.

The [Day 5 Markdown companion](HDLBits_Day5_Original_Submissions_Review.md) preserves the original discussion and dated submission appendix. The [review record](DOCUMENT_REVIEW.md) separates technical tests, platform evidence and document/navigation checks. The [posting plan](../LinkedIn_Attempt_2_Posting_Plan_and_Ideas.md) is a separate editorial proposal, not this reading-day index.
