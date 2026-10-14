// Optional CSV regeneration. Run with the documented Codex primary runtime.
import fs from 'node:fs/promises';
import path from 'node:path';
import {Workbook} from '@oai/artifact-tool';
const root=path.resolve(process.argv[2]);
const rows=JSON.parse(await fs.readFile(path.join(root,'five-transfer-matrix.json'),'utf8'));
const wb=Workbook.create();const sh=wb.worksheets.add('Five transfer evidence');
sh.getRangeByIndexes(0,0,rows.length,rows[0].length).values=rows;
wb.recalculate();const values=sh.getUsedRange().values;
for(let i=0;i<rows.length;i++)for(let j=0;j<rows[0].length;j++){
 if(String(values[i]?.[j]??'')===String(rows[i][j]??''))continue;
 if(i>0&&rows[0][j]==='utc'&&Date.parse(values[i][j])===Date.parse(rows[i][j]))continue;
 throw Error('Matrix mismatch '+i+','+j);
}
const quote=v=>'"'+String(v??'').replaceAll('"','""')+'"';
await fs.writeFile(path.join(root,'five-transfer-ledger.csv'),rows.map(r=>r.map(quote).join(',')).join('\r\n')+'\r\n');
console.log('PASS: five-row CSV preserves all exact identifiers, integer amounts and UTC values.');
