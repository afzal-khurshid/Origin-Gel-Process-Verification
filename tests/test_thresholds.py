import unittest
from pathlib import Path

from analysis.combined_verification import ProcessVerifier


class TestThresholds(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.verifier = ProcessVerifier()
        cls.results_folder = (
            Path(__file__).resolve().parents[1] / "results"
        )

    def test_normal_rpm_passes(self):
        result = self.verifier.verify_rpm(
            self.results_folder / "normal_rpm.csv"
        )
        self.assertEqual(result["status"], "PASS")

    def test_rpm_drift_fails(self):
        result = self.verifier.verify_rpm(
            self.results_folder / "rpm_drift_rpm.csv"
        )
        self.assertEqual(result["status"], "FAIL")

    def test_high_rpm_deviation_fails(self):
        result = self.verifier.verify_rpm(
            self.results_folder / "high_deviation_rpm.csv"
        )
        self.assertEqual(result["status"], "FAIL")

    def test_low_rpm_deviation_fails(self):
        result = self.verifier.verify_rpm(
            self.results_folder / "low_deviation_rpm.csv"
        )
        self.assertEqual(result["status"], "FAIL")

    def test_noisy_rpm_fails(self):
        result = self.verifier.verify_rpm(
            self.results_folder / "noisy_sensor_rpm.csv"
        )
        self.assertEqual(result["status"], "FAIL")

    def test_normal_temperature_passes(self):
        result = self.verifier.verify_temperature(
            self.results_folder / "normal_temperature.csv"
        )
        self.assertEqual(result["status"], "PASS")

    def test_temperature_drift_fails(self):
        result = self.verifier.verify_temperature(
            self.results_folder / "temperature_drift_temperature.csv"
        )
        self.assertEqual(result["status"], "FAIL")

    def test_high_temperature_fails(self):
        result = self.verifier.verify_temperature(
            self.results_folder / "high_temperature_temperature.csv"
        )
        self.assertEqual(result["status"], "FAIL")

    def test_low_temperature_fails(self):
        result = self.verifier.verify_temperature(
            self.results_folder / "low_temperature_temperature.csv"
        )
        self.assertEqual(result["status"], "FAIL")

    def test_noisy_temperature_fails(self):
        result = self.verifier.verify_temperature(
            self.results_folder / "noisy_sensor_temperature.csv"
        )
        self.assertEqual(result["status"], "FAIL")


if __name__ == "__main__":
    unittest.main(verbosity=2)