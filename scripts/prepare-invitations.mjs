import {randomInt,randomBytes,createCipheriv} from 'node:crypto';
import {existsSync,writeFileSync,mkdirSync} from 'node:fs';
const members=['Huen','Tiffany','Ashley','Ronnie','Sara','Gu'];
if(existsSync('draw.json')||existsSync('.private/invitations.json'))throw Error('Draw already exists; refusing to reroll or overwrite invitations.');
let order;do{order=[0,1,2,3,4,5];for(let i=5;i>0;i--){const j=randomInt(i+1);[order[i],order[j]]=[order[j],order[i]]}}while(order.some((n,i)=>n===i));
const entries={},invitations=[];
for(let i=0;i<6;i++){const id=randomBytes(16).toString('hex'),key=randomBytes(32),iv=randomBytes(12);const cipher=createCipheriv('aes-256-gcm',key,iv);cipher.setAAD(Buffer.from(id));const encrypted=Buffer.concat([cipher.update(JSON.stringify({giver:members[i],recipient:members[order[i]]}).padEnd(256,' ')),cipher.final(),cipher.getAuthTag()]);entries[id]={iv:iv.toString('base64url'),cipher:encrypted.toString('base64url')};invitations.push({name:members[i],email:null,url:'https://saratcfung.github.io/starsc-secret-santa/#id='+id+'&key='+key.toString('base64url')})}
mkdirSync('.private',{recursive:true,mode:0o700});writeFileSync('.private/invitations.json',JSON.stringify(invitations,null,2),{mode:0o600});writeFileSync('draw.json',JSON.stringify({version:1,entries},null,2));console.log('Prepared six fixed encrypted invitations. Private links saved locally; no results printed.');
