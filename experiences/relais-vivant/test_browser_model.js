'use strict';
const fs=require('node:fs'),assert=require('node:assert/strict');
const R=require('./kernel.js'), results=JSON.parse(fs.readFileSync(__dirname+'/results.json','utf8'));
let compared=0;
for(const scenario of Object.values(results.scenarios)){
  const result=R.solve(scenario.config);
  assert.deepEqual([...result.K].sort(),scenario.kernel.map(R.key).sort());
  assert.deepEqual(result.ranks,scenario.losing_ranks);
  assert.deepEqual(result.safe,scenario.safe_actions);
  assert.deepEqual(result.sizes,scenario.iterations);
  compared+=scenario.states;
}
for(const row of results.sweep){
  const cfg={...R.defaults(),lifetime_c:row.lifetime,lifetime_b:row.lifetime,gains:[row.minimum_gain,row.minimum_gain+1]};
  assert.equal(R.solve(cfg).K.size,row.viable);compared+=row.total;
}
console.log(JSON.stringify({status:'PASS',python_javascript_state_parameter_pairs:compared,scenarios:28}));
