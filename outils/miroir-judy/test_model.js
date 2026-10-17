/* Reproducible test for the MIROIR-JUDY *illustrative* capabilities model.
 * No network, external data, credentials or actual ChatGPT permission changes.
 */
"use strict";
const assert=require("node:assert/strict");
const fs=require("node:fs");
const vm=require("node:vm");
const path=require("node:path");
const m=require("./model.js");
const names=m.switches;
const STATES=1<<names.length;

function stateAt(mask) {
  const state={};
  names.forEach(function (key,i) {state[key]=Boolean(mask & (1<<i));});
  return state;
}
function check(label,func) {func(); console.log("PASS "+label);}

check("texte seul et scénarios complets",function(){
  assert.deepEqual(m.evaluate(m.preset("text")).possible,["explain"]);
  assert.equal(m.evaluate(m.preset("documents")).possible.length,2);
  assert.equal(m.evaluate(m.preset("lab")).possible.length,5);
  assert.equal(m.evaluate(m.preset("publication")).possible.length,6);
  assert.equal(m.evaluate(m.preset("audition")).possible.length,7);
});

check("permission de publier indépendante de l'outil",function(){
  assert.ok(!m.evaluate({writeRepo:true,writePermission:false}).possible.includes("publish"));
  assert.ok(!m.evaluate({writeRepo:false,writePermission:true}).possible.includes("publish"));
  assert.ok(m.evaluate({writeRepo:true,writePermission:true}).possible.includes("publish"));
});

check("code et fichier nécessaires pour un diagnostic acoustique",function(){
  assert.ok(!m.evaluate({runCode:true}).possible.includes("analyze"));
  assert.ok(!m.evaluate({readFiles:true}).possible.includes("analyze"));
  assert.ok(m.evaluate({readFiles:true,runCode:true}).possible.includes("analyze"));
  assert.ok(m.evaluate({runCode:true}).possible.includes("render"));
  assert.ok(!m.evaluate({readFiles:true}).possible.includes("render"));
});

check("qualité subjective et action physique non induites par des outils",function(){
  for (let mask=0;mask<STATES;mask++) {
    const out=m.evaluate(stateAt(mask));
    assert.deepEqual(out.outside,["physical"]);
    assert.deepEqual(out.unverified,["subjective"]);
    assert.ok(!out.possible.includes("physical"));
    assert.ok(!out.possible.includes("subjective"));
    assert.ok(out.possible.includes("explain"));
  }
});

let checked=0;
check("extension authentique monotone pour 64 états finis",function(){
  for(let mask=0;mask<STATES;mask++) {
    const source=stateAt(mask);
    for(let i=0;i<names.length;i++) {
      const expanded={...source,[names[i]]:true};
      const comp=m.compare(source,expanded);
      assert.equal(comp.extension,true);
      assert.deepEqual(comp.lost,[]);
      checked++;
    }
  }
  assert.equal(checked,STATES*names.length);
});

check("retirer une permission peut rétrécir l'ensemble",function(){
  const a=m.preset("publication");
  const b={...a,writePermission:false};
  const compare=m.compare(a,b);
  assert.equal(compare.extension,false);
  assert.ok(compare.lost.includes("publish"));
});

check("schéma strict de la simulation et refus des valeurs incohérentes",function(){
  assert.throws(()=>m.evaluate({readFiles:"oui"}),TypeError);
  assert.throws(()=>m.preset("real_live_permissions"),RangeError);
  assert.equal(m.tasks.length,9);
  assert.deepEqual(new Set(m.tasks.map(t=>t.id)).size,m.tasks.length);
});

check("HTML autonome, contrôles reliés, aucun stockage ou appel serveur",function(){
  const html=fs.readFileSync(path.join(__dirname,"demo.html"),"utf8");
  for (const name of [...names,"preset","reset","taskGrid","summary","delta"]) {
    assert.ok(html.includes('id="'+name+'"'),"élément manquant : "+name);
  }
  assert.ok(html.includes('<script src="./model.js"></script>'));
  const inline=[...html.matchAll(/<script(?:\s[^>]*)?>([\s\S]*?)<\/script>/g)]
      .map(x=>x[1]).filter(Boolean);
  assert.equal(inline.length,1);
  new vm.Script(inline[0],{filename:"MIROIR-JUDY-demo"});
  assert.ok(!/fetch\s*\(|XMLHttpRequest|WebSocket|sendBeacon|localStorage|mediaDevices/.test(html));
});

console.log(JSON.stringify({schema:"MIROIR-JUDY-v01",pass:true,states:STATES,
                            checked_extensions:checked,unit_scenarios:8},null,2));
