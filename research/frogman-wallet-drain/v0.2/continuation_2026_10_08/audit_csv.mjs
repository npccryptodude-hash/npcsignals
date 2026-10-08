// Read-only CSV audit. Preserve source strings and precision; do not export a workbook.
import fs from 'node:fs/promises';
import { Workbook } from '@oai/artifact-tool';
const root=process.argv[2];
for(const [name,count] of [['transaction_ledger_F0207_F0208.csv',2],['hyperliquid_ledger_F0209_F0220.csv',12],['spot_fills_F0221_F0425.csv',205]]){
  const text=await fs.readFile(`${root}/${name}`,'utf8');
  const wb=await Workbook.fromCSV(text,{sheetName:'Ledger'});
  const sheet=wb.worksheets.getItemAt(0);
  const ids=sheet.getRange(`A2:A${count+1}`).values.flat();
  if(ids.length!==count || new Set(ids).size!==count || ids.some(x=>!/^F\d{4}$/.test(x)))throw new Error(`Invalid IDs in ${name}`);
  console.log(JSON.stringify({file:name,rows:count,firstID:ids[0],lastID:ids.at(-1),unique:true}));
  const check=await wb.inspect({kind:'table',range:'Ledger!A1:H3',include:'values',tableMaxRows:3,tableMaxCols:8,maxChars:1200});
  console.log(check.ndjson);
}
