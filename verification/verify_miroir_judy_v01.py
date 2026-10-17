"""MIROIR-JUDY: independent finite illustration of AI tool/permission context.
Direction: Xavier Endres (COMPAT-01), 17 October 2026.
Finite model and tests: Judy Velune (GPT-6).
Not an empirical evaluation of the model's hidden abilities.
"""
import itertools
import json
import unittest

FIELDS=("readFiles","runCode","writeRepo","writePermission","audioInput","humanFeedback")
REQUIREMENTS={
    "explain":set(),
    "inspect":{"readFiles"},
    "calculate":{"runCode"},
    "render":{"runCode"},
    "analyze":{"readFiles","runCode"},
    "publish":{"writeRepo","writePermission"},
    "feedback":{"audioInput","humanFeedback"},
}


def eligible(enabled):
    allowed=set(enabled)
    return {name for name, needs in REQUIREMENTS.items() if needs.issubset(allowed)}


def all_contexts():
    for bits in itertools.product((False,True),repeat=len(FIELDS)):
        yield {f for f,enabled in zip(FIELDS,bits) if enabled}


class TestSituatedAI(unittest.TestCase):
    def test_unchanged_agent_with_different_contexts(self):
        baseline=eligible(set())
        self.assertEqual(baseline,{"explain"})
        workshop=eligible({"readFiles","runCode"})
        self.assertEqual(len(workshop),5)
        published=eligible({"readFiles","runCode","writeRepo","writePermission"})
        self.assertEqual(len(published),6)

    def test_public_action_requires_tool_and_right(self):
        self.assertNotIn("publish",eligible({"writeRepo"}))
        self.assertNotIn("publish",eligible({"writePermission"}))
        self.assertIn("publish",eligible({"writeRepo","writePermission"}))

    def test_audio_measurements_are_not_a_human_verdict(self):
        self.assertIn("analyze",eligible({"readFiles","runCode"}))
        self.assertNotIn("feedback",eligible({"readFiles","runCode"}))
        self.assertIn("feedback",eligible({"audioInput","humanFeedback"}))

    def test_all_64_contexts_monotone_under_384_enabling_steps(self):
        cases=0
        contexts=tuple(all_contexts())
        self.assertEqual(len(contexts),64)
        for ctx in contexts:
            for field in FIELDS:
                expanded=ctx|{field}
                self.assertLessEqual(eligible(ctx),eligible(expanded))
                cases+=1
        self.assertEqual(cases,384)

    def test_permission_removed_can_close_an_old_possibility(self):
        before={"writeRepo","writePermission"}
        after={"writeRepo"}
        self.assertIn("publish",eligible(before))
        self.assertNotIn("publish",eligible(after))

    def test_arbitrary_format_constraint_is_not_physical_impossibility(self):
        pitch=49
        old_validator = 52 <= pitch <= 96
        corrected_validator = 45 <= pitch <= 96
        self.assertFalse(old_validator)
        self.assertTrue(corrected_validator)
        self.assertTrue(0 <= pitch <= 127)

    def test_simulator_does_not_certify_qualia_or_embodiment(self):
        for context in all_contexts():
            self.assertNotIn("subjective",eligible(context))
            self.assertNotIn("physical",eligible(context))


if __name__=="__main__":
    run=unittest.main(verbosity=2,exit=False)
    print(json.dumps({"protocol":"MIROIR-JUDY-01",
                      "finite_contexts":64,"enabling_edges":384,
                      "cases":run.result.testsRun,
                      "pass":run.result.wasSuccessful()}))
    raise SystemExit(0 if run.result.wasSuccessful() else 1)
