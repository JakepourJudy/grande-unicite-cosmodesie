/* Public finite checks for the same compatibility model used by GitHub Pages.
 * No library, browser session, people records, microphone or network.
 */
"use strict";
const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const vm = require("node:vm");
const model = require("./model.js");
let cases = 0;
function test(label, fn) {
  fn();
  process.stdout.write("PASS " + label + "\n");
}
test("moyenne inadaptée à la couverture", () => {
  assert.equal(model.coverage([40,48],[44],1),0);
  assert.equal(model.coverage([40,48],[40],1),1);
  assert.equal(model.coverage([40,48],[40,48],1),2);
});
test("inversion des possibilités selon la tâche", () => {
  const common = {shelf:190,door:170,shoe:43};
  const short = model.calculate({...common,height:150});
  const tall = model.calculate({...common,height:200});
  assert.equal(short.tasks[0].feasible,false);
  assert.equal(tall.tasks[0].feasible,true);
  assert.equal(short.tasks[1].feasible,true);
  assert.equal(tall.tasks[1].feasible,false);
});
test("faisabilité contextuelle, sans diagnostic", () => {
  const base=model.calculate(model.defaults);
  assert.equal(base.feasibleCount,1);
  assert.deepEqual(base.possibleTasks,["door"]);
  const adapted=model.calculate(model.withAdaptations(model.defaults));
  assert.equal(adapted.feasibleCount,3);
});
test("extension véritable : aucun témoin ancien perdu sur la grille finie", () => {
  for (let height=140;height<=210;height+=5) {
    for (let shoe=36;shoe<=52;shoe++) {
      for (const shelf of [160,185,205,235]) {
        for (const door of [150,170,190,230]) {
          const s={height,shoe,shelf,door};
          const before=model.calculate(s);
          const after=model.calculate(model.withAdaptations(s));
          for (const id of before.possibleTasks)
            assert.ok(after.possibleTasks.includes(id),"action perdue : "+id);
          assert.ok(after.feasibleCount>=before.feasibleCount);
          cases++;
        }
      }
    }
  }
  assert.equal(cases,15*17*4*4);
});
test("une extension partielle conserve les succès précédents", () => {
  const s={height:175,shoe:48,shelf:205,door:180};
  let prev=model.calculate(s);
  for(const key of ["lowerShelf","raiseDoor","extendStock"]){
    s[key]=true;
    const after=model.calculate(s);
    assert.ok(after.feasibleCount>=prev.feasibleCount);
    prev=after;
  }
});
test("données invalides refusées", () => {
  assert.throws(()=>model.calculate({height:182.3}),RangeError);
  assert.throws(()=>model.calculate({shoe:55}),RangeError);
  assert.throws(()=>model.calculate({lowerShelf:1}),TypeError);
});
test("page publique : syntaxe et branchements utilisateur", () => {
  const html=fs.readFileSync(path.join(__dirname,"demo.html"),"utf8");
  for(const id of ["height","shoe","shelf","door","lowerShelf","raiseDoor","extendStock",
                   "summary","adapt","reset","shelfStatus","doorStatus","shoesStatus"]){
    assert.ok(html.includes('id="'+id+'"'),"ID manquant "+id);
  }
  assert.ok(html.includes('<script src="./model.js"></script>'));
  const inline=[...html.matchAll(/<script(?:\s[^>]*)?>([\s\S]*?)<\/script>/g)].map(x=>x[1]).filter(Boolean);
  assert.equal(inline.length,1);
  new vm.Script(inline[0],{filename:"COMPAT-01-browser"});
  assert.ok(!/fetch\s*\(|XMLHttpRequest|sendBeacon|localStorage|mediaDevices/.test(html));
});
console.log(JSON.stringify({ok:true,finite_cases:cases,standalone_html:true}));
