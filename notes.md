# HDLBits Workspace Notes

## Excel hyperlink rule

Apply this rule to every current and future HDLBits workbook:

- Keep each link as a real Excel `HYPERLINK(url, friendly_name)` formula so it remains clickable.
- Preserve the short friendly label shown in the cell (for example, `Note`, `Image`, `Code`, `HDLBits`, or the problem name). Never replace it with the URL or an exporter diagnostic.
- After exporting an `.xlsx`, verify every hyperlink cell has a normal string cache containing the friendly label. It must not be stored as an error cell.
- The text `HYPERLINK is not implemented` must never appear anywhere in a final workbook. It is an export-tool cache error, not valid workbook content.
- Preserve the workbook's existing link-blue font, fills, status colors, formulas, tables, notes, and layout when repairing links.
- Final verification must include: all hyperlink formulas counted, zero cached-label mismatches, zero error cells, zero diagnostic strings, and a clickability check in desktop Excel using **Ctrl+click** or **Open Hyperlink** from the context menu.

This rule prevents the broken-link display that previously appeared in the HDLBits trackers.

## Attempt 2 output layout

- Keep exactly one Excel workbook in the `HDLBits Attempt 2` directory: `HDLBits_Attempt_2_Tracker_Simple.xlsx`.
- Update that workbook in place. Do not leave duplicate, backup, repaired, final, copy, or versioned `.xlsx` files beside it.
- Keep every user-facing Attempt 2 PDF in the outermost `HDLBits Attempt 2` directory.
- Temporary builders, renders, and validation files may be used under `internal` while working, but remove task-specific scratch output after final verification.
