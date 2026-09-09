# HDLBits Attempt 2

**The questions behind the code - study notes by Kapil Tripathi.**

Start with the **[question-led index](DOCUMENT_INDEX.md)**: choose the question you want answered, open one of the **10 day-wise PDFs**, or look up an entry. Related short notes are combined. Each PDF has a reading cover, clickable question contents, section and entry bookmarks, and continuous page numbering.

Use the [tracker](HDLBits_Attempt_2_Tracker_Simple.xlsx) for problem order and progress. At the final 9 September 2026 completion checkpoint, it records **178 Done and 0 Pending out of 178 entries**. The [review record](DOCUMENT_REVIEW.md) documents the evidence, earlier technical corrections and presentation checks.

The [LinkedIn posting plan](../LinkedIn_Attempt_2_Posting_Plan_and_Ideas.md) contains the proposed 10-day series, draft captions, document choices and review checklist.

## Study PDFs

These are the primary reading files: **one PDF per day**. Reading days follow the review sequence, including later revisits; the tracker's original day labels and submission dates remain unchanged. All the later series are together on Day 10.

| Day | Read this | Pages |
|---|---|---:|
| 01 | [Serial reception and HDLC timing](output/pdf/HDLBits_Day_01.pdf) | 27 |
| 02 | [Loops, muxes and Verilog operators](output/pdf/HDLBits_Day_02.pdf) | 11 |
| 03 | [Latch storage and state history](output/pdf/HDLBits_Day_03.pdf) | 3 |
| 04 | [Vectors, flip-flops and PS/2 packets](output/pdf/HDLBits_Day_04.pdf) | 6 |
| 05 | [Sampled edges, serial complement and RTL questions](output/pdf/HDLBits_Day_05.pdf) | 24 |
| 06 | [Dual-edge sampling and three-sample FSMs](output/pdf/HDLBits_Day_06.pdf) | 31 |
| 07 | [FSM widths and counter connections](output/pdf/HDLBits_Day_07.pdf) | 7 |
| 08 | [Wire, reg and reset behavior](output/pdf/HDLBits_Day_08.pdf) | 6 |
| 09 | [Missing assignments and the 1101 FSM](output/pdf/HDLBits_Day_09.pdf) | 6 |
| 10 | [Boolean forms, timers, LFSRs and Conway](output/pdf/HDLBits_Day_10.pdf) | 45 |

The [Day 5 Markdown review](HDLBits_Day5_Original_Submissions_Review.md) remains an alternative companion. All 58 tracker discussion links now open the corresponding day-wise PDF at its answer page. The original 16 PDFs remain unchanged at their existing paths so historical links and evidence continue to work; they are source notes, not a second primary reading list.

## Reading and sharing

Open a PDF's question contents or bookmarks to jump to an explanation. Every footer links back to **Contents** and **All days**. The [question and entry index](DOCUMENT_INDEX.md) provides exact answer pages and original HDLBits problem links. In a preview that ignores links, use the printed page numbers or download the PDF.

Day 10's [clocked state/next_state decision guide](output/pdf/HDLBits_Day_10.pdf#page=21) is on page 21. Its final [LFSR definitions and revision reference](output/pdf/HDLBits_Day_10.pdf#page=43), pages 43-45, explains the acronym, state, seed, taps, feedback forms, maximum period, zero lockup, applications and limitations. Earlier code, traces and complete solutions remain in the preceding chapters.

For a LinkedIn document attachment, use the title on the PDF cover. These are full study notes; the posting plan suggests focused pages for each post. Source references, original questions and dated submission records remain with their explanations.

## Verification

The [document review](DOCUMENT_REVIEW.md) separates earlier local RTL simulations from checks of PDF content, links, page references and layout. The day-wise set preserves all **148 original technical pages**, adds **3 LFSR reference pages**, and replaces the old front matter with **15 cover/index pages**: **166 pages total**. Source images remain byte-identical; text is preserved apart from the recorded navigation-reference edits. Original note numbers in the historical records below refer to the retained source PDFs, not the ten new reading-day files.

## Completion records

On 8 September, entries **167, 169, 173, 174, and 178** were marked Done after Kapil identified these exact second-attempt completions and their latest saved submissions were verified as successful on 7 September. Later, entries **171 and 176** were marked Done after Kapil's explicit completion report: Always_casez had a saved success dated 7 September, and Always_nolatches showed a current `Status: Success!` result panel. Entries **168 (Rule 90)** and **172 (Rule 110)** were then marked Done after their current compile-and-simulate panels were rechecked and showed `Status: Success!`.

On 9 September, the current result panels for entries **165 (the complete controller), 170 (the complete timer), and 175 (one-hot logic equations)** showed `Status: Success!`, so those three entries were marked Done. Entry 175 is intentionally recorded as `No questions asked` and is not included in Note 14; the note stops with the six non-basic series entries through the complete timer. At that checkpoint, entries **141, 145, 151, 166, and 177** remained Pending.

Later on 9 September, entries **141 (5-bit LFSR), 145 (3-bit LFSR), and 151 (32-bit LFSR)** were marked Done after their current Chrome result panels showed `Status: Success!`. Note 15 explains their common Galois update method, one-based tap numbering, schematic-to-equation translation, nonblocking old-value timing, exact 5-bit and 3-bit cycles, and the 32-bit tap check. Entries **166 and 177** remain Pending at this checkpoint.

At the final 9 September check, entry **177 (Conwaylife)** also showed `Status: Success!` in its current Chrome result panel and was marked Done. The editor's row/column-index question and request to discuss the solution are covered in Note 16. Local Icarus simulation separately passed 1,638 full-grid edge checks. The tracker now uses native clickable hyperlinks with readable labels, including all existing problem and discussion links.

Finally, Kapil explicitly confirmed entry **166 (Testbench2)** and the whole second attempt complete. Its latest stored successful submission was loaded and inspected in Chrome: **28 June 2026, 11:14:42 PM**, later than the last non-success at **11:14:00 PM** on the same day. These are the dates displayed by the website, not a new September submission. The current-pass completion record rests on Kapil's explicit confirmation; the saved submission separately establishes an accepted implementation. No new submission was made. No question note was requested for this entry.

The HDLBits website is the authority for platform acceptance. Earlier checkpoints support entries 1-98; Kapil's explicit current-pass completion reports support entries 99-122, with matching Chrome tabs and saved-success records used as evidence. Entries 124-127 and 129-130 are supported by their current Chrome simulation result panels inspected on 5 September 2026; entries 123, 128, 131, 132, 134-140, and 142-144 by their current success panels inspected on 6 September 2026; entries 133, 146-150, 152-164 by their current success panels inspected on 7 September 2026; entries 168 and 172 by their current success panels rechecked on 8 September 2026; and entries 141, 145, 151, 165, 170, 175 and 177 by their current success panels inspected on 9 September 2026. Local simulation is a separate check and was run only where source or a reusable testbench is preserved in this directory; it is not claimed as a local rerun of all accepted submissions. Testbench2's final evidence is recorded above. Historical first-attempt successes alone do not establish second-attempt completion.
