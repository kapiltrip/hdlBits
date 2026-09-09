# HDLBits Attempt 2

**The questions behind the code - study notes by Kapil Tripathi.**

Start with the **[document index](DOCUMENT_INDEX.md)**: find a topic, browse all 16 PDFs, or jump to the answer pages for any of the 58 tracker entries with discussion links. Each PDF has a reading cover, clickable contents, section and entry bookmarks, and consistent page numbering.

Use the [tracker](HDLBits_Attempt_2_Tracker_Simple.xlsx) for problem order and progress. At the final 9 September 2026 completion checkpoint, it records **178 Done and 0 Pending out of 178 entries**. The [review record](DOCUMENT_REVIEW.md) documents the evidence, earlier technical corrections and presentation checks.

The [LinkedIn posting plan](../LinkedIn_Attempt_2_Posting_Plan_and_Ideas.md) contains the proposed 10-day series, draft captions, document choices and review checklist.

## Study PDFs

Note numbers identify this collection; they are separate from tracker entries and posting days. Existing filenames are retained, including their older review-day labels.

| Note | Read this | Pages |
|---|---|---:|
| 01 | [Serial input needs real clock edges](HDLBits_Fsm_serialdata_For_Loops_vs_Clock_Cycles.pdf) | 11 |
| 02 | [Loops, muxes and storage](HDLBits_Combined_Questions_and_Day2_Review.pdf) | 12 |
| 03 | [HDLC: get the output cycle right](HDLBits_Fsm_hdlc_Mealy_to_Moore_Deep_Dive.pdf) | 16 |
| 04 | [States, sampled edges and operators](HDLBits_Recovered_Code_Questions_54_74_75_77.pdf) | 6 |
| 05 | [Bytes, flip-flops and PS/2 packets](HDLBits_Day4_Questions_Vector_DFF_PS2.pdf) | 6 |
| 06 | [Two's complement, one bit at a time](HDLBits_Entry80_Moore_Serial_Twos_Complement_Deep_Dive.pdf) | 8 |
| 07 | [Small RTL mistakes, explained](HDLBits_Day5_Original_Submissions_Review.pdf) | 12 |
| 08 | [Dual-edge sampling and waveform reasoning](HDLBits_Day6_Non_FSM_QA_Dualedge_and_Circuit5.pdf) | 19 |
| 09 | [Three samples, no wasted cycle](HDLBits_Entry90_Exams_2014_Q3FSM_Three_Sample_Window_Deep_Dive.pdf) | 12 |
| 10 | [FSM widths and counter connections](HDLBits_Day7_QA_FSM_Warnings_and_Counter_Interface.pdf) | 7 |
| 11 | [Wire, reg and reset behavior](HDLBits_Day8_QA_Wire_Reg_and_Shift_Reset.pdf) | 6 |
| 12 | [Missing assignments and the 1101 FSM](HDLBits_Day9_QA_Latches_and_Sequence_FSM.pdf) | 6 |
| 13 | [K-map operators, Boolean forms and cellular automata](HDLBits_Day10_Kmaps_Boolean_Forms_and_Rules90_110.pdf) | 9 |
| 14 | [Timer-series FSMs and next-state timing](HDLBits_Day11_Review2015_Timer_Series_and_Next_State.pdf) | 15 |
| 15 | [LFSR taps, shifts and old-value timing](HDLBits_Day12_LFSR_Taps_Shifts_and_Old_Value_Timing.pdf) | 12 |
| 16 | [Conway: grid indexing and next-state timing](HDLBits_Day12_Conway_Grid_Indexing_and_Next_State.pdf) | 7 |

The [Day 5 Markdown review](HDLBits_Day5_Original_Submissions_Review.md) has its own entry index and remains the destination of its existing tracker links.

## Reading and sharing

Open a PDF's contents page or bookmarks to jump to a section. Every footer links back to **Contents** and **All notes**. The [topic and entry index](DOCUMENT_INDEX.md) provides exact answer pages and original HDLBits problem links. In a preview that ignores links, use the printed page numbers or download the PDF.

For a LinkedIn document attachment, use the title on the PDF cover. These are full study notes; the posting plan suggests focused pages for each post. Source references, original questions and dated submission records remain with their explanations.

## Verification

The [document review](DOCUMENT_REVIEW.md) separates earlier local RTL simulations from the current checks of PDF content, links, page references and layout. The indexing update preserves the earlier technical body pages while rebuilding consistent covers and navigation. Note 14 links the six Review 2015 timer-series entries. Note 15 links entries 141, 145 and 151 to the 5-bit, schematic-based 3-bit and 32-bit LFSR explanations. Note 16 answers entry 177's indexing and complete-solution questions, including toroidal neighbors, old-versus-next generation timing, loop execution, arithmetic widths and the seed-7 boundary trace.

## Completion records

On 8 September, entries **167, 169, 173, 174, and 178** were marked Done after Kapil identified these exact second-attempt completions and their latest saved submissions were verified as successful on 7 September. Later, entries **171 and 176** were marked Done after Kapil's explicit completion report: Always_casez had a saved success dated 7 September, and Always_nolatches showed a current `Status: Success!` result panel. Entries **168 (Rule 90)** and **172 (Rule 110)** were then marked Done after their current compile-and-simulate panels were rechecked and showed `Status: Success!`.

On 9 September, the current result panels for entries **165 (the complete controller), 170 (the complete timer), and 175 (one-hot logic equations)** showed `Status: Success!`, so those three entries were marked Done. Entry 175 is intentionally recorded as `No questions asked` and is not included in Note 14; the note stops with the six non-basic series entries through the complete timer. At that checkpoint, entries **141, 145, 151, 166, and 177** remained Pending.

Later on 9 September, entries **141 (5-bit LFSR), 145 (3-bit LFSR), and 151 (32-bit LFSR)** were marked Done after their current Chrome result panels showed `Status: Success!`. Note 15 explains their common Galois update method, one-based tap numbering, schematic-to-equation translation, nonblocking old-value timing, exact 5-bit and 3-bit cycles, and the 32-bit tap check. Entries **166 and 177** remain Pending at this checkpoint.

At the final 9 September check, entry **177 (Conwaylife)** also showed `Status: Success!` in its current Chrome result panel and was marked Done. The editor's row/column-index question and request to discuss the solution are covered in Note 16. Local Icarus simulation separately passed 1,638 full-grid edge checks. The tracker now uses native clickable hyperlinks with readable labels, including all existing problem and discussion links.

Finally, Kapil explicitly confirmed entry **166 (Testbench2)** and the whole second attempt complete. Its latest stored successful submission was loaded and inspected in Chrome: **28 June 2026, 11:14:42 PM**, later than the last non-success at **11:14:00 PM** on the same day. These are the dates displayed by the website, not a new September submission. The current-pass completion record rests on Kapil's explicit confirmation; the saved submission separately establishes an accepted implementation. No new submission was made. No question note was requested for this entry.

The HDLBits website is the authority for platform acceptance. Earlier checkpoints support entries 1-98; Kapil's explicit current-pass completion reports support entries 99-122, with matching Chrome tabs and saved-success records used as evidence. Entries 124-127 and 129-130 are supported by their current Chrome simulation result panels inspected on 5 September 2026; entries 123, 128, 131, 132, 134-140, and 142-144 by their current success panels inspected on 6 September 2026; entries 133, 146-150, 152-164 by their current success panels inspected on 7 September 2026; entries 168 and 172 by their current success panels rechecked on 8 September 2026; and entries 141, 145, 151, 165, 170, 175 and 177 by their current success panels inspected on 9 September 2026. Local simulation is a separate check and was run only where source or a reusable testbench is preserved in this directory; it is not claimed as a local rerun of all accepted submissions. Testbench2's final evidence is recorded above. Historical first-attempt successes alone do not establish second-attempt completion.
