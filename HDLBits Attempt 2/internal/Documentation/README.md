# Maintain the Attempt 2 day-wise collection

The primary reading set is **10 day-wise PDFs** under `output/pdf/`, built by [build_daily_collection.py](build_daily_collection.py). [daily_questions.py](daily_questions.py) maps each preserved technical page to a specific reader question. The generated [manifest](daily_collection_manifest.json) records every source page, final page, contents target, entry mapping and intentional prose-reference edit. All later series and the new LFSR reference are in Day 10.

## Current workflow

```bash
python "HDLBits Attempt 2/internal/Documentation/build_daily_collection.py"
python "HDLBits Attempt 2/internal/Documentation/check_daily_collection.py"
python "HDLBits Attempt 2/internal/Documentation/render_daily_collection.py"
```

Inspect every rendered page for a full rebuild. The current set is 166 pages: 148 original body pages, 3 new LFSR reference pages and 15 cover/index pages. Larger volumes have a detailed question index. The checker compares source text, image bytes and geometry, allowing only documented reference changes and running-header/footer replacement. It also verifies question bookmarks, contents links, page counts, embedded fonts, local index targets, all 58 entry mappings and the LFSR examples.

The original 16 PDFs remain unchanged at their existing paths to preserve historical links. They supply vector source pages for consolidation. The older source indexer below now requires `--source-only` when a day-wise manifest exists, preventing an accidental overwrite of the primary index.

To refresh the tracker's 58 discussion labels and native links after pagination changes, use `daily_tracker_links.py prepare`, `update_daily_tracker.mjs --edit`, and `daily_tracker_links.py apply`, in that order. Run the JavaScript with the bundled Node runtime and a local ignored `node_modules` junction to the bundled packages. Artifact Tool authors the friendly labels. The native-link pass changes only those payloads and existing hyperlink relationship targets in the original workbook package. Every other ZIP part and all unrelated cells, styles, day labels, validation, panes and dimensions must remain unchanged. Use `update_daily_tracker.mjs --preview` before editing and `--verify` afterward to inspect the saved file and representative beginning/middle/end ranges.

Before another update, deliberately select a new before snapshot if the ignored `internal/tmp/daily_collection/tracker_before.xlsx` belongs to a different change set; do not silently overwrite its baseline. Temporary work and review renders are kept under ignored `internal/tmp/daily_collection/`. The primary workbook stays in the Attempt 2 directory so its relative PDF links resolve.

## Retained source-note workflow

[index_study_pdfs.py](index_study_pdfs.py) maintains covers/navigation for the retained 16 source PDFs. It is not the day-wise index writer. The following older workflow and its baseline remain useful for reproducing the pre-consolidation presentation audit.

## Rebuild

Use Python with PyMuPDF, ReportLab, pypdf and openpyxl available. Ghostscript (`gs` or `gswin64c`) is optional: when it is absent, the builder accepts output only after confirming that every font is already embedded. On Kapil's Codex setup, the scripts automatically add the bundled Python package directory, so the commands below also work from the normal system Python. The tracker is read only in this builder.

```bash
python "HDLBits Attempt 2/internal/Documentation/index_study_pdfs.py" --source-only
```

The PDF metadata marker identifies an already indexed file. A repeat build replaces its cover and recreates its navigation; it does not add another contents page. Intermediate output goes under the ignored `internal/tmp/portfolio_index/` directory. The PDFs themselves remain the source for their preserved body pages; Git history retains earlier versions.

When Ghostscript is available, the final pass re-embeds fonts to prevent substitution and spacing differences between viewers. It uses no image-downsampling preset and verifies text, bookmarks and link destinations before accepting the result. Without Ghostscript, the generated Arial/Consolas cover and footer fonts and the preserved body fonts must already be embedded or the build stops. See the [Ghostscript PDF output documentation](https://ghostscript.readthedocs.io/en/latest/VectorDevices.html) for embedding and preservation controls.

## When a document changes

The indexer calls [standardize_pdf_palette.py](standardize_pdf_palette.py) after font embedding. It changes only inventoried authored colors and decorative full-bleed top rules, preserves meaningful diagram colors, and compares text, image bytes, geometry and navigation before accepting the result. [audit_pdf_palette.py](audit_pdf_palette.py) inventories text and vector-fill colors without changing a PDF.

`verify_pdf_preservation.py bc5bc09` compares the full collection with the completion commit before the presentation audit. It requires unchanged text, image bytes, page geometry, bookmarks and link destinations, allowing only the documented Day 9 page-reference correction. Use that baseline for this audit; a later content revision needs its own explicitly reviewed change set.

For a full visual review, run `python "HDLBits Attempt 2/internal/Documentation/render_collection_review.py"`. This uses Poppler and Pillow to render every page and assemble numbered four-page review sheets plus a manifest under ignored `internal/tmp/collection_review_20260909/`. Inspect all pages; re-render any page changed during review. Rendered images are QA intermediates, not substitutes for the vector/searchable reader PDFs.

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
