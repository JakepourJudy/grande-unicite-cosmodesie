/* Independent implementation of the finite game for the interactive display. */
(function (root) {
  'use strict';
  const allActions = ['feed', 'repair_c', 'repair_b', 'explore'];
  const key = s => s.join(',');
  const defaults = () => ({lifetime_c:4,lifetime_b:4,capacity:4,gains:[2,3],actions:[...allActions],strict_deadline:false});
  function states(c) {
    const out=[];
    for(let i=1;i<=c.lifetime_c;i++) for(let j=1;j<=c.lifetime_b;j++)
      for(let r=1;r<=c.capacity;r++) out.push([i,j,r]);
    return out;
  }
  function step(s,a,w,c) {
    if (!c.actions.includes(a) || !c.gains.includes(w)) throw Error('Action or gain outside declared model');
    if (!s || s[0]<1 || s[1]<1 || s[2]<1 || s[0]>c.lifetime_c || s[1]>c.lifetime_b || s[2]>c.capacity) return null;
    const [x,b,r]=s;
    if(c.strict_deadline && ((a==='repair_c' && x===1)||(a==='repair_b' && b===1)))return null;
    const n=[a==='repair_c'?c.lifetime_c:x-1,a==='repair_b'?c.lifetime_b:b-1,a==='feed'?Math.min(c.capacity,r+w):r-1];
    return n.every(v=>v>=1)?n:null;
  }
  function solve(c) {
    const all=states(c),ranks={};let K=new Set(all.map(key));const sizes=[K.size];let rank=0;
    while(true){
      rank++;
      const next=new Set();
      for(const s of all){
        if(!K.has(key(s)))continue;
        const ok=c.actions.some(a=>c.gains.every(w=>{const n=step(s,a,w,c);return n&&K.has(key(n));}));
        if(ok)next.add(key(s));else ranks[key(s)]=rank;
      }
      sizes.push(next.size);
      if(next.size===K.size)break;
      K=next;
    }
    const safe={};
    for(const s of all)if(K.has(key(s)))safe[key(s)]=c.actions.filter(a=>c.gains.every(w=>{const n=step(s,a,w,c);return n&&K.has(key(n));}));
    return {K,ranks,safe,sizes};
  }
  const api={allActions,key,defaults,states,step,solve};
  if(typeof module!=='undefined'&&module.exports)module.exports=api;
  root.Renewal=api;
})(typeof globalThis!=='undefined'?globalThis:this);
