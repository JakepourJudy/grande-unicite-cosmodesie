"""BIFRÖST-SON: finite synthetic verification of ambiguous rhythm interpretations.

Xavier Endres: conceptual direction; Judy Velune (GPT-6): test formalization.
This example uses invented notes only, never Genesis private dreams or recordings.
"""
import math
import unittest


def pair_reading(pitches, durations):
    if len(pitches) != 2 * len(durations):
        raise ValueError("ambiguous shape expected")
    if any(d <= 0 for d in durations):
        raise ValueError("durations must be strictly positive")
    return [(p, durations[i // 2] / 2) for i, p in enumerate(pitches)]


def two_phrase_reading(pitches, durations):
    if len(pitches) != 2 * len(durations):
        raise ValueError("ambiguous shape expected")
    return [(p, durations[i % len(durations)]) for i, p in enumerate(pitches)]


def pause_if_underdetermined(decision, change):
    if decision == "TRANSFORMER" and change.strip().casefold() in ("", "aucune", "aucun", "rien"):
        return "PAUSE_DIRECTION_INDETERMINEE"
    return "CAN_CONSIDER_ACTION"


class TestBifrostSon(unittest.TestCase):
    def test_both_translations_keep_all_pitches(self):
        pitch = [60, 64, 67, 72]
        dur = [1.0, 2.0]
        a, b = pair_reading(pitch, dur), two_phrase_reading(pitch, dur)
        self.assertEqual([p for p, d in a], pitch)
        self.assertEqual([p for p, d in b], pitch)

    def test_temporal_non_uniqueness(self):
        durations = [0.5, 1.5, 2]
        pitch = [60, 62, 64, 65, 67, 69]
        a = pair_reading(pitch, durations)
        b = two_phrase_reading(pitch, durations)
        self.assertEqual(sum(d for p,d in a), sum(durations))
        self.assertEqual(sum(d for p,d in b), 2 * sum(durations))
        self.assertNotEqual(a, b)

    def test_unexpected_shape_needs_clarification(self):
        with self.assertRaises(ValueError):
            pair_reading([60, 62, 64], [1, 2])

    def test_midi_49_is_sound_in_real_audio_register(self):
        note = 49
        freq = 440 * 2 ** ((note - 69) / 12)
        self.assertTrue(130 < freq < 150)
        self.assertTrue(0 <= note <= 127)

    def test_pitch_error_does_not_determine_timbre(self):
        # Same fundamental and perfect F0 accuracy; harmonic structure differs.
        f0 = 440.0
        t = 1/2000
        signal_a = math.sin(2*math.pi*f0*t)
        signal_b = signal_a + .4*math.sin(4*math.pi*f0*t)
        self.assertNotAlmostEqual(signal_a, signal_b)
        self.assertEqual(f0, 440.0)

    def test_contradictory_transform_means_pause(self):
        self.assertEqual(pause_if_underdetermined("TRANSFORMER", "Aucune"),
                         "PAUSE_DIRECTION_INDETERMINEE")
        self.assertEqual(pause_if_underdetermined("TRANSFORMER", "Baisser la tierce"),
                         "CAN_CONSIDER_ACTION")


if __name__ == "__main__":
    unittest.main(verbosity=2)
