
import unittest

from analysis.combined_verification import ProcessVerifier


class TestCombinedVerification(unittest.TestCase):

    def setUp(self):
        self.verifier = ProcessVerifier()

    def test_both_pass(self):
        self.assertEqual(
            self.verifier.combine_statuses("PASS", "PASS"),
            "PASS"
        )

    def test_rpm_fail(self):
        self.assertEqual(
            self.verifier.combine_statuses("FAIL", "PASS"),
            "FAIL"
        )

    def test_temperature_fail(self):
        self.assertEqual(
            self.verifier.combine_statuses("PASS", "FAIL"),
            "FAIL"
        )

    def test_both_fail(self):
        self.assertEqual(
            self.verifier.combine_statuses("FAIL", "FAIL"),
            "FAIL"
        )

    def test_rpm_warning(self):
        self.assertEqual(
            self.verifier.combine_statuses("WARNING", "PASS"),
            "WARNING"
        )

    def test_temperature_warning(self):
        self.assertEqual(
            self.verifier.combine_statuses("PASS", "WARNING"),
            "WARNING"
        )

    def test_warning_and_fail(self):
        self.assertEqual(
            self.verifier.combine_statuses("WARNING", "FAIL"),
            "FAIL"
        )

    def test_both_warning(self):
        self.assertEqual(
            self.verifier.combine_statuses("WARNING", "WARNING"),
            "WARNING"
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)