# Maintain the Attempt 2 document index

The current reading collection is built by [index_study_pdfs.py](index_study_pdfs.py). It updates all 12 PDF covers, PDF bookmarks, page counters and footer links, then regenerates [DOCUMENT_INDEX.md](../../DOCUMENT_INDEX.md) from the document manifest and the tracker. Original technical pages stay at their native quality.

## Rebuild

Use Python with PyMuPDF, ReportLab and openpyxl installed, plus Ghostscript (`gs` or `gswin64c`) on the executable path. The tracker is read only in this builder.

```bash
python "HDLBits Attempt 2/internal/Documentation/index_study_pdfs.py"
python "HDLBits Attempt 2/internal/Documentation/check_study_index.py"
```

The PDF metadata marker identifies an already indexed file. A repeat build replaces its cover and recreates its navigation; it does not add another contents page. Intermediate output goes under the ignored `internal/tmp/portfolio_index/` directory. The PDFs themselves remain the source for their preserved body pages; Git history retains earlier versions.

The final pass embeds fonts to prevent substitution and spacing differences between viewers. It uses no image-downsampling preset and verifies text, bookmarks and link destinations before accepting the result. See the [Ghostscript PDF output documentation](https://ghostscript.readthedocs.io/en/latest/VectorDevices.html) for embedding and preservation controls.

## When a document changes

1. Edit or regenerate the relevant technical note, keeping source references and historical evidence attached.
2. Update its `DOCS` manifest entry: filename, title, summary, takeaway, contents groups, body-page labels and tracker-entry answer pages. The manifest's ranges use the original page numbers, before the added cover in the three notes marked `prepend=True`.
3. Rebuild. The builder stops if the file set, body-page count or linked tracker-entry coverage differs from the manifest.
4. Update corresponding page references in the Attempt 2 README, document review, Day 5 Markdown companion, posting plan and any tracker hyperlink labels that display pages.
5. Run the checker, render changed pages and inspect them before committing. Check code, tables, diagrams, links and page counters at readable size.

The Day 5 submission review, Day 8 wire/reg note and Day 9 latch/FSM note received a new front page. Their current physical pages are original page + 1. The other nine PDFs replaced an existing cover, keeping their physical page numbers.

## Earlier scripts

The older `review_documents.py`, `write_review_index.py` and `check_document_layout.py` record the previous review workflow. They depend on checkpoint data or paths under `internal/tmp/document_review_20260907`; they are not a fresh-checkout rebuild command. In particular, the old index writer assumes 151 Done / 27 Pending and must not be used to overwrite the current progress summary.

`build_day9_questions.py` generates the original five-page Day 9 technical note. Run the current indexing builder afterward to restore its reading cover and navigation. The existing RTL verification scripts remain separate from document-layout validation.
