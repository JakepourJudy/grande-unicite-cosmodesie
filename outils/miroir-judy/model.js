/* MIROIR-JUDY v0.1 - finite capability/environment demo.
 * The UI toggles ASSUMPTIONS, not actual ChatGPT permissions or plugins.
 * Xavier Endres: COMPAT-01 conceptual direction.
 * Judy Velune (GPT-6): model, tests, public editorial implementation.
 */
(function (root, factory) {
  "use strict";
  const model = factory();
  if (typeof module !== "undefined" && module.exports) module.exports = model;
  if (root) root.MiroirJudy = model;
})(typeof window !== "undefined" ? window : null, function () {
  "use strict";
  const SWITCHES = Object.freeze([
    "readFiles", "runCode", "writeRepo", "writePermission", "audioInput", "humanFeedback"
  ]);
  const LABELS = Object.freeze({
    readFiles: "Lecture de fichiers autorisés",
    runCode: "Exécution de code / création de fichiers",
    writeRepo: "Connecteur GitHub avec écriture",
    writePermission: "Autorisation explicite pour publier",
    audioInput: "Perception du signal audio",
    humanFeedback: "Retour d'un auditeur volontaire"
  });
  const PRESETS = Object.freeze({
    text: Object.freeze({}),
    documents: Object.freeze({readFiles:true}),
    lab: Object.freeze({readFiles:true,runCode:true}),
    publication: Object.freeze({readFiles:true,runCode:true,writeRepo:true,writePermission:true}),
    audition: Object.freeze({readFiles:true,runCode:true,writeRepo:true,writePermission:true,
                              audioInput:true,humanFeedback:true})
  });
  const TASKS = Object.freeze([
    Object.freeze({id:"explain",label:"Expliquer et structurer une hypothèse",
      requires:Object.freeze([]),kind:"operation",
      limitation:"Une réponse claire n'est pas automatiquement un résultat vrai."}),
    Object.freeze({id:"inspect",label:"Examiner le contenu d'un fichier",
      requires:Object.freeze(["readFiles"]),kind:"operation",
      limitation:"L'outil ne donne accès qu'aux fichiers réellement autorisés."}),
    Object.freeze({id:"calculate",label:"Exécuter un test fini par code",
      requires:Object.freeze(["runCode"]),kind:"operation",
      limitation:"Un test n'est pas une preuve générale."}),
    Object.freeze({id:"render",label:"Produire un fichier sonore WAV",
      requires:Object.freeze(["runCode"]),kind:"operation",
      limitation:"Savoir produire un son ne garantit pas une appréciation musicale."}),
    Object.freeze({id:"analyze",label:"Mesurer les hauteurs d'un WAV accessible",
      requires:Object.freeze(["readFiles","runCode"]),kind:"operation",
      limitation:"La mesure de hauteur n'est pas l'interprétation esthétique."}),
    Object.freeze({id:"publish",label:"Publier une modification sur GitHub",
      requires:Object.freeze(["writeRepo","writePermission"]),kind:"operation",
      limitation:"Écrire un fichier ne prouve pas qu'un lecteur l'a compris."}),
    Object.freeze({id:"feedback",label:"Organiser une évaluation musicale avec retour",
      requires:Object.freeze(["audioInput","humanFeedback"]),kind:"protocol",
      limitation:"Cela rend un protocole envisageable, pas son résultat déjà validé."}),
    Object.freeze({id:"physical",label:"Déplacer un objet physique",
      requires:Object.freeze([]),kind:"outside",
      limitation:"Aucun actionneur physique n'est représenté dans ce scénario."}),
    Object.freeze({id:"subjective",label:"Prouver une expérience émotionnelle subjective",
      requires:Object.freeze([]),kind:"undetermined",
      limitation:"Un outil ou une déclaration textuelle n'établit pas cette propriété."})
  ]);
  function normalize(input) {
    input = input || {};
    const result = {};
    for (const key of SWITCHES) {
      const value = Object.prototype.hasOwnProperty.call(input,key) ? input[key] : false;
      if (typeof value !== "boolean") throw new TypeError(key + " doit être booléen");
      result[key] = value;
    }
    return result;
  }
  function evaluate(input) {
    const state = normalize(input);
    const rows = TASKS.map(function (task) {
      if (task.kind==="outside") return Object.assign({},task,{status:"non-represented",missing:[]});
      if (task.kind==="undetermined") return Object.assign({},task,{status:"unverified",missing:[]});
      const missing = task.requires.filter(function (cap) { return !state[cap]; });
      return Object.assign({},task,{status:missing.length===0 ? "possible-under-assumptions" : "blocked",
                                    missing:missing});
    });
    return {
      state:state,
      rows:rows,
      possible:rows.filter(function (r) {return r.status==="possible-under-assumptions";}).map(function (r) {return r.id;}),
      blocked:rows.filter(function (r) {return r.status==="blocked";}).map(function (r) {return r.id;}),
      unverified:rows.filter(function (r) {return r.status==="unverified";}).map(function (r) {return r.id;}),
      outside:rows.filter(function (r) {return r.status==="non-represented";}).map(function (r) {return r.id;})
    };
  }
  function preset(key) {
    if (!Object.prototype.hasOwnProperty.call(PRESETS,key)) throw new RangeError("Preset inconnu");
    return normalize(PRESETS[key]);
  }
  function compare(oldState,newState) {
    const from=evaluate(oldState),to=evaluate(newState);
    return {
      from:from,to:to,
      added:to.possible.filter(function (id) {return !from.possible.includes(id);}),
      lost:from.possible.filter(function (id) {return !to.possible.includes(id);}),
      extension:SWITCHES.every(function (cap) {return !from.state[cap] || to.state[cap];})
    };
  }
  return Object.freeze({switches:SWITCHES,labels:LABELS,tasks:TASKS,presets:PRESETS,
    normalize:normalize,evaluate:evaluate,preset:preset,compare:compare});
});
