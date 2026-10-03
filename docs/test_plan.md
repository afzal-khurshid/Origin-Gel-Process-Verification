Test Plan

1. Purpose

This test plan describes how the Origin Gel Process Verification prototype is verified.

The aim is to confirm that the software correctly:

Processes simulated RPM measurements.
Processes simulated temperature measurements.
Calculates the maximum measurement deviation.
Classifies process conditions as PASS, WARNING or FAIL.
Combines the RPM and temperature results into one overall process status.
Detects the predefined abnormal simulation scenarios.
Shows correct results on the PyQt6 dashboard.


2. Scope

The test scope covers:

RPM data analysis.
Temperature data analysis.
RPM verification.
Temperature verification.
Combined process verification.
Scenario-based fault testing.
Automated unit testing.
Dashboard verification.

Physical hardware and clinical validation are outside the current scope.


3. Test Environment

Software:
Python 3
PyQt6
Matplotlib
Python unittest
Windows operating system

Project:
Origin_Gel_Process_Verification


4. Test Parameters

RPM
Target: 1600 RPM

Limits defined for this project:
PASS: maximum deviation of 5 RPM or less
WARNING: maximum deviation above 5 RPM and up to 10 RPM
FAIL: maximum deviation above 10 RPM

Temperature
Target: 37.0 degrees Celsius

Limits defined for this project:
PASS: maximum deviation of 0.2 degrees Celsius or less
WARNING: maximum deviation above 0.2 and up to 0.5 degrees Celsius
FAIL: maximum deviation above 0.5 degrees Celsius

These limits are test thresholds I defined specifically for this prototype.


5. RPM Test Cases

TC-RPM-01, Normal RPM
Input: normal_rpm.csv
Expected: PASS
Observed: PASS

TC-RPM-02, RPM Drift
Input: rpm_drift_rpm.csv
Expected: FAIL
Observed: FAIL

TC-RPM-03, High RPM Deviation
Input: high_deviation_rpm.csv
Expected: FAIL
Observed: FAIL

TC-RPM-04, Low RPM Deviation
Input: low_deviation_rpm.csv
Expected: FAIL
Observed: FAIL

TC-RPM-05, Noisy RPM Sensor
Input: noisy_sensor_rpm.csv
Expected: FAIL
Observed: FAIL


6. Temperature Test Cases

TC-TEMP-01, Normal Temperature
Input: normal_temperature.csv
Expected: PASS
Observed: PASS

TC-TEMP-02, Temperature Drift
Input: temperature_drift_temperature.csv
Expected: FAIL
Observed: FAIL

TC-TEMP-03, High Temperature
Input: high_temperature_temperature.csv
Expected: FAIL
Observed: FAIL

TC-TEMP-04, Low Temperature
Input: low_temperature_temperature.csv
Expected: FAIL
Observed: FAIL

TC-TEMP-05, Noisy Temperature Sensor
Input: noisy_sensor_temperature.csv
Expected: FAIL
Observed: FAIL


7. Combined Verification Tests

The combined logic works like this:
If either parameter is FAIL, the overall status is FAIL.
If there is no FAIL but at least one WARNING, the overall status is WARNING.
If both parameters are PASS, the overall status is PASS.

Combined test cases (RPM status, Temperature status, Expected overall):

PASS, PASS, PASS
FAIL, PASS, FAIL
PASS, FAIL, FAIL
FAIL, FAIL, FAIL
WARNING, PASS, WARNING
PASS, WARNING, WARNING
WARNING, FAIL, FAIL
WARNING, WARNING, WARNING

All eight combined verification unit tests passed.


8. Automated Test Results

Combined verification tests
Command:
python -m unittest discover -s tests -p "test_combined_verification.py" -v
Result: 8 tests passed

Threshold tests
Command:
python -m unittest discover -s tests -p "test_thresholds.py" -v
Result: 10 tests passed

Total automated tests: 18


9. Dashboard Tests

Dashboard Test 01, Normal Scenario
Scenario: NORMAL
Expected: RPM PASS, Temperature PASS, Overall PASS
Observed: RPM PASS, Temperature PASS, Overall PASS
Result: PASS

Dashboard Test 02, RPM Fault
Scenario: RPM DRIFT
Expected: RPM FAIL, Temperature PASS, Overall FAIL
Observed: RPM FAIL, Temperature PASS, Overall FAIL
Result: PASS

Dashboard Test 03, Temperature Fault
Scenario: TEMPERATURE DRIFT
Expected: RPM PASS, Temperature FAIL, Overall FAIL
Observed: RPM PASS, Temperature FAIL, Overall FAIL
Result: PASS


10. Baseline Measurement Verification

RPM baseline
Target: 1600.00 RPM
Average: 1600.15 RPM
Minimum: 1595.51 RPM
Maximum: 1603.93 RPM
Standard deviation: 1.91 RPM
Maximum deviation: 4.49 RPM
Status: PASS

Temperature baseline
Target: 37.000 degrees Celsius
Average: 37.004 degrees Celsius
Minimum: 36.880 degrees Celsius
Maximum: 37.105 degrees Celsius
Standard deviation: 0.051 degrees Celsius
Maximum deviation: 0.120 degrees Celsius
Status: PASS


11. Acceptance Criteria

The prototype is considered functionally successful when:

1. Normal RPM data produces PASS.
2. Abnormal RPM scenarios are detected.
3. Normal temperature data produces PASS.
4. Abnormal temperature scenarios are detected.
5. The combined status logic gives the expected result.
6. The automated unit tests pass.
7. Dashboard results match the underlying verification logic.
8. Missing input files produce an appropriate error.
9. The project runs from the defined project structure.

The current prototype meets the functional acceptance criteria that have been implemented.


12. Limitations

The test results are based on simulated data.

The testing does not establish:
Clinical performance.
Medical device compliance.
Compliance with manufacturer specifications.
Physical sensor accuracy.
Real motor control performance.
Real heater control performance.
Long-duration hardware reliability.

Testing with calibrated sensors and real hardware would be needed to cover these.


13. Future Test Expansion

Future hardware-based testing can include:

RPM sensor calibration.
Temperature sensor calibration.
Motor speed response testing.
Heater response testing.
Sensor disconnection detection.
Sensor noise characterization.
Long-duration stability testing.
Communication fault testing.
Power interruption testing.
Hardware-in-the-loop testing.
Data logging integrity testing.
