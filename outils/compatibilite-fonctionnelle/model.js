/* COMPAT-01: finite illustration of situated feasibility, not a human assessment.
 * Xavier Endres: conceptual direction. Judy Velune (GPT-6): toy model and code.
 * Shared unchanged between browser and Node tests; no API, no tracking.
 */
(function (root, factory) {
  "use strict";
  var model = factory();
  if (typeof module !== "undefined" && module.exports) module.exports = model;
  if (root) root.CompatModel = model;
})(typeof window !== "undefined" ? window : null, function () {
  "use strict";
  var DEFAULTS = Object.freeze({
    height: 175, shoe: 50, shelf: 205, door: 180,
    lowerShelf: false, raiseDoor: false, extendStock: false
  });
  var STANDARD = Object.freeze([39, 40, 41, 42, 43, 44, 45]);
  var EXTENDED = Object.freeze([36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52]);
  function integer(value, min, max, key) {
    if (!Number.isInteger(value) || value < min || value > max)
      throw new RangeError(key + " doit être un entier entre " + min + " et " + max);
    return value;
  }
  function bool(value, key) {
    if (typeof value !== "boolean") throw new TypeError(key + " doit être booléen");
    return value;
  }
  function normalize(input) {
    var s = Object.assign({}, DEFAULTS, input || {});
    return {
      height: integer(s.height, 140, 210, "height"),
      shoe: integer(s.shoe, 36, 52, "shoe"),
      shelf: integer(s.shelf, 160, 240, "shelf"),
      door: integer(s.door, 150, 235, "door"),
      lowerShelf: bool(s.lowerShelf, "lowerShelf"),
      raiseDoor: bool(s.raiseDoor, "raiseDoor"),
      extendStock: bool(s.extendStock, "extendStock")
    };
  }
  function coverage(demands, offered, tolerance) {
    if (!Array.isArray(demands) || !Array.isArray(offered) || !(tolerance >= 0))
      throw new TypeError("Entrées de couverture invalides");
    return demands.filter(function (need) {
      return offered.some(function (size) { return Math.abs(size - need) <= tolerance; });
    }).length;
  }
  function calculate(input) {
    var s = normalize(input);
    var reach = s.height + 20;       // purely illustrative reach proxy
    var shelf = s.lowerShelf ? Math.min(s.shelf, 160) : s.shelf;
    var clearance = s.raiseDoor ? Math.max(s.door, 225) : s.door;
    var offered = s.extendStock ? EXTENDED : STANDARD;
    var shelfOK = reach >= shelf;
    var doorOK = s.height <= clearance;
    var shoesOK = offered.includes(s.shoe);
    var tasks = [
      { id: "shelf", title: "Atteindre un objet", feasible: shelfOK,
        detail: "Portée fictive " + reach + " cm ; objet à " + shelf + " cm.",
        intervention: "Abaisser l'étagère", key: "lowerShelf" },
      { id: "door", title: "Passer sans se courber", feasible: doorOK,
        detail: "Hauteur fictive " + s.height + " cm ; passage à " + clearance + " cm.",
        intervention: "Rehausser le passage", key: "raiseDoor" },
      { id: "shoes", title: "Trouver la taille demandée", feasible: shoesOK,
        detail: "Taille demandée " + s.shoe + " ; références disponibles " +
                (s.extendStock ? "36–52" : "39–45") + " (modèle fictif).",
        intervention: "Élargir les références", key: "extendStock" }
    ];
    return {
      state: s,
      tasks: tasks,
      feasibleCount: tasks.filter(function (t) { return t.feasible; }).length,
      availableStock: offered.slice(),
      possibleTasks: tasks.filter(function (t) { return t.feasible; }).map(function (t) { return t.id; }),
      barriers: tasks.filter(function (t) { return !t.feasible; }).map(function (t) {
        return { id: t.id, proposedEnvironmentalAdaptation: t.intervention, key: t.key };
      })
    };
  }
  function withAdaptations(state) {
    var s = normalize(state);
    return Object.assign({}, s, {lowerShelf: true, raiseDoor: true, extendStock: true});
  }
  return Object.freeze({
    defaults: DEFAULTS, standardStock: STANDARD, extendedStock: EXTENDED,
    normalize: normalize, calculate: calculate,
    coverage: coverage, withAdaptations: withAdaptations
  });
});
