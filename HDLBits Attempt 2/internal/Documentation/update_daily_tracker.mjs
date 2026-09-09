// Artifact Tool authors the friendly discussion labels. A narrow native-link
// pass applies these authored values to the original package, preserving every
// unrelated part and all original styling.
import fs from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { FileBlob, SpreadsheetFile } from '@oai/artifact-tool';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'../..');
const work=path.join(root,'internal/tmp/daily_collection');
const book=path.join(root,'HDLBits_Attempt_2_Tracker_Simple.xlsx');
const mode=process.argv[2] ?? '--preview';
const wb=await SpreadsheetFile.importXlsx(await FileBlob.load(book));
const sheet=wb.worksheets.getItem('Tracker');
if (mode==='--edit') {
  const changes=JSON.parse(await fs.readFile(path.join(work,'tracker_changes.json'),'utf8'));
  for (const [ref,item] of Object.entries(changes)) sheet.getRange(ref).values=[[item.label]];
  const out=await SpreadsheetFile.exportXlsx(wb);
  await out.save(path.join(work,'tracker_authored.xlsx'));
  console.log(`Authored ${Object.keys(changes).length} discussion labels.`);
} else {
  console.log((await wb.inspect({kind:'table',range:'Tracker!A1:E8',include:'values,formulas',tableMaxRows:8,tableMaxCols:5,maxChars:2200})).ndjson);
  console.log((await wb.inspect({kind:'match',searchTerm:'#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A|#NUM!|#NULL!|#SPILL!|#CALC!|HYPERLINK is not implemented',options:{useRegex:true,maxResults:20},summary:'Saved workbook error scan'})).ndjson);
  const ranges=mode==='--verify' ? [['beginning','A1:E13'],['middle','A81:E94'],['end','A165:E183']] : [['before','A1:E13']];
  for (const [name,range] of ranges) {
    const image=await wb.render({sheetName:'Tracker',range,scale:1.3,format:'png'});
    await fs.writeFile(path.join(work,`tracker_${name}.png`),new Uint8Array(await image.arrayBuffer()));
  }
}
