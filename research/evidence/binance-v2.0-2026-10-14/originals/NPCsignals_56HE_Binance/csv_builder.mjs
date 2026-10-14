import fs from 'node:fs/promises';
import {Workbook} from '@oai/artifact-tool';
const root='/workspace/scratch/7dfc4f3398aa/exchange-56he-pass';
const rows=JSON.parse(await fs.readFile(root+'/csv-rows.json','utf8'));
const wb=Workbook.create();const sh=wb.worksheets.add('56HE USDT disposition');
sh.getRangeByIndexes(0,0,rows.length,rows[0].length).values=rows;wb.recalculate();
const values=sh.getUsedRange().values;
for(let i=0;i<rows.length;i++)for(let j=0;j<rows[0].length;j++){
 if(String(values[i]?.[j]??'')===String(rows[i][j]??''))continue;
 if(i>0&&j===2&&Date.parse(values[i][j])===Date.parse(rows[i][j]))continue;
 throw Error('CSV mismatch '+i+','+j);
}
const quote=v=>'"'+String(v??'').replaceAll('"','""')+'"';
await fs.writeFile(root+'/evidence-ledger.csv',rows.map(r=>r.map(quote).join(',')).join('\r\n')+'\r\n');
console.log('Exact workbook/CSV matrix check passed: '+(rows.length-1)+' rows.');
