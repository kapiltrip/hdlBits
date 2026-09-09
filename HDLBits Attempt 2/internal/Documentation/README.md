# Maintain the Attempt 2 document index

The current reading collection is built by [index_study_pdfs.py](index_study_pdfs.py). It updates all 16 PDF covers, PDF bookmarks, page counters and footer links, then regenerates [DOCUMENT_INDEX.md](../../DOCUMENT_INDEX.md) from the document manifest and the tracker. Original technical pages stay at their native quality.

## Rebuild

Use Python with PyMuPDF, ReportLab and openpyxl available. Ghostscript (`gs` or `gswin64c`) is optional: when it is absent, the builder accepts output only after confirming that every font is already embedded. On Kapil's Codex setup, the scripts automatically add the bundled Python package directory, so the commands below also work from the normal system Python. The tracker is read only in this builder.

```bash
python "HDLBits Attempt 2/internal/Documentation/index_study_pdfs.py"
python "HDLBits Attempt 2/internal/Documentation/check_study_index.py"
```

The PDF metadata marker identifies an already indexed file. A repeat build replaces its cover and recreates its navigation; it does not add another contents page. Intermediate output goes under the ignored `internal/tmp/portfolio_index/` directory. The PDFs themselves remain the source for their preserved body pages; Git history retains earlier versions.

When Ghostscript is available, the final pass re-embeds fonts to prevent substitution and spacing differences between viewers. It uses no image-downsampling preset and verifies text, bookmarks and link destinations before accepting the result. Without Ghostscript, the generated Arial/Consolas cover and footer fonts and the preserved body fonts must already be embedded or the build stops. See the [Ghostscript PDF output documentation](https://ghostscript.readthedocs.io/en/latest/VectorDevices.html) for embedding and preservation controls.

## When a document changes

1. Edit or regenerate the relevant technical note, keeping source references and historical evidence attached.
2. Update its `DOCS` manifest entry: filename, title, summary, takeaway, contents groups, body-page labels and tracker-entry answer pages. The manifest's ranges use the original page numbers, before the added cover in notes marked `prepend=True`.
3. Rebuild. The builder stops if the file set, body-page count or linked tracker-entry coverage differs from the manifest.
4. Update corresponding page references in the Attempt 2 README, document review, Day 5 Markdown companion, posting plan and any tracker hyperlink labels that display pages.
5. Run the checker, render changed pages and inspect them before committing. Check code, tables, diagrams, links and page counters at readable size.

The Day 5 submission review, Day 8 wire/reg note, Day 9 latch/FSM note, combined Day 10 note, Review 2015 timer-series note, LFSR-series note and Conway note receive a new front page. Their physical pages are body page + 1. The other nine PDFs replace an existing cover, keeping their physical page numbers.

## Earlier scripts

`build_day12_conway.py` generates six technical pages for entry 177, using the complete RTL in `conway_reference.v`; the indexer adds the cover for a seven-page note. `conway_reference_tb.sv` checks the RTL against an independent flat-index model, including 512 local configurations, 100 random five-generation runs, boundary patterns and load timing. The tracker reader supports both original HYPERLINK formulas and native workbook hyperlinks, so preserving friendly link text does not break the generated entry index.

The older `review_documents.py`, `write_review_index.py` and `check_document_layout.py` record the previous review workflow. They depend on checkpoint data or paths under `internal/tmp/document_review_20260907`; they are not a fresh-checkout rebuild command. In particular, the old index writer assumes 151 Done / 27 Pending and must not be used to overwrite the current progress summary.

`build_day9_questions.py` generates the original five-page Day 9 technical note. `build_day10_combined.py` generates the eight technical pages for entries 161, 164, 168 and 172; the indexer then adds the standard collection cover and navigation to make the nine-page reader document. `build_day11_review2015_timer.py` generates fourteen technical pages for entries 144, 149, 155, 160, 165 and 170; the indexed reader document is fifteen pages. `build_day12_lfsr_series.py` generates eleven technical pages for entries 141, 145 and 151; the indexed reader document is twelve pages. The existing RTL verification scripts remain separate from document-layout validation.
