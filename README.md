Origin Gel Process Verification



Closed Loop Process Control for Gel Card Processing



A self-directed engineering prototype that checks centrifuge speed and incubation temperature stability in gel card processing.



Author: Afzal Khurshid

Program: Electrical Engineering

Institution: University of Engineering and Technology (UET), Lahore

Project type: Self-directed engineering prototype



Note: This is a simulation and software verification prototype. It is not an Origin-authorized project, not a medical device, not a clinical validation system, and not a manufacturer-certified test system.





1\. Project Overview



Gel card processing depends on controlled centrifugation and incubation. If the rotational speed or the temperature changes, the process can become inconsistent.



In this project I built a software prototype that:



Simulates centrifuge RPM measurements.

Simulates incubation temperature measurements.

Calculates deviations and stability statistics.

Detects abnormal RPM behavior.

Detects abnormal temperature behavior.

Applies thresholds that I defined for this project.

Combines the RPM and temperature results into one overall process status.

Shows the results on a PyQt6 dashboard where a scenario can be selected.

Includes unit tests for the verification logic.



The main idea is to move from simple timed processing, where nothing is measured, to a process where integrity is actually verified from measurements.





2\. Objectives



1\. Check whether the simulated centrifuge speed stays close to the target RPM.

2\. Check whether the simulated incubation temperature stays close to the target temperature.

3\. Detect drift, large deviation and noisy sensor behavior.

4\. Combine both parameters into a single overall status.

5\. Build a software structure that can be reused later with real hardware.

6\. Show that the verification logic can be tested automatically.





3\. Target Process Parameters



RPM

Target: 1600 RPM



Thresholds defined for this project:

PASS: maximum deviation of 5 RPM or less

WARNING: maximum deviation of 10 RPM or less

FAIL: maximum deviation above 10 RPM



Temperature

Target: 37.0 degrees Celsius



Thresholds defined for this project:

PASS: maximum deviation of 0.2 degrees Celsius or less

WARNING: maximum deviation of 0.5 degrees Celsius or less

FAIL: maximum deviation above 0.5 degrees Celsius



These thresholds are test values I chose for this prototype. They are not manufacturer limits, regulatory limits or clinical specifications.





4\. System Architecture



The software is split into layers. The RPM path and the temperature path run side by side, and each one has three stages: simulation, analysis and verification. The two verification results then go into the combined verification stage. The combined result is shown on the PyQt6 dashboard as PASS, WARNING or FAIL.





5\. Project Structure



Origin\_Gel\_Process\_Verification



&#x20;   analysis

&#x20;       rpm\_analysis.py

&#x20;       rpm\_plot.py

&#x20;       rpm\_verification.py

&#x20;       temperature\_analysis.py

&#x20;       temperature\_plot.py

&#x20;       temperature\_verification.py

&#x20;       combined\_verification.py



&#x20;   dashboard

&#x20;       main.py



&#x20;   simulator

&#x20;       rpm\_simulator.py

&#x20;       run\_scenarios.py

&#x20;       temperature\_simulator.py

&#x20;       temperature\_scenarios.py



&#x20;   tests

&#x20;       test\_combined\_verification.py

&#x20;       test\_thresholds.py



&#x20;   results

&#x20;       simulated CSV files

&#x20;       verification plots







6\. Simulation Scenarios



The prototype has a normal case and several fault cases.



RPM scenarios:

Normal RPM

RPM drift

High RPM deviation

Low RPM deviation

Noisy RPM sensor



Temperature scenarios:

Normal temperature

Temperature drift

High temperature

Low temperature

Noisy temperature sensor



These are simulated test cases used to check the verification software.





7\. Verification Logic



Each parameter is evaluated on its own.



RPM verification

The maximum absolute deviation is calculated as the largest value of the absolute difference between measured RPM and target RPM. The result is then classified using the RPM thresholds.



Temperature verification

The maximum absolute deviation is calculated as the largest value of the absolute difference between measured temperature and target temperature. The result is then classified using the temperature thresholds.



Combined verification

If either parameter is FAIL, the overall status is FAIL.

If there is no FAIL but at least one WARNING, the overall status is WARNING.

If both parameters are PASS, the overall status is PASS.





8\. Baseline Results



Normal RPM (approximate values)

Target RPM: 1600.00

Average RPM: 1600.15

Minimum RPM: 1595.51

Maximum RPM: 1603.93

Standard deviation: 1.91 RPM

Maximum deviation: 4.49 RPM

Result: PASS



Normal temperature (approximate values)

Target temperature: 37.000 degrees Celsius

Average temperature: 37.004 degrees Celsius

Minimum temperature: 36.880 degrees Celsius

Maximum temperature: 37.105 degrees Celsius

Standard deviation: 0.051 degrees Celsius

Maximum deviation: 0.120 degrees Celsius

Result: PASS





9\. Fault Scenario Results



Scenario, RPM result, Temperature result, Overall result



Normal: PASS, PASS, PASS

RPM drift: FAIL, PASS, FAIL

High RPM deviation: FAIL, PASS, FAIL

Low RPM deviation: FAIL, PASS, FAIL

Noisy RPM sensor: FAIL, PASS, FAIL

Temperature drift: PASS, FAIL, FAIL

High temperature: PASS, FAIL, FAIL

Low temperature: PASS, FAIL, FAIL

Noisy temperature sensor: PASS, FAIL, FAIL



These results show that the combined logic can tell whether a simulated problem comes from the RPM path or the temperature path.





10\. Automated Testing



The tests use Python's unittest framework.



Combined verification tests (8 tests) cover these cases:

PASS and PASS

FAIL and PASS

PASS and FAIL

FAIL and FAIL

WARNING and PASS

PASS and WARNING

WARNING and FAIL

WARNING and WARNING



Threshold tests (10 tests) cover the RPM and temperature scenarios.



Both test suites pass.



To run the combined verification tests:

python -m unittest discover -s tests -p "test\_combined\_verification.py" -v



To run the threshold tests:

python -m unittest discover -s tests -p "test\_thresholds.py" -v





11\. Dashboard



The PyQt6 dashboard shows:

Scenario selection

RPM status

Temperature status

Overall process status

Maximum RPM deviation

Maximum temperature deviation

Target values

Verification thresholds



To launch it:

python dashboard\\main.py



Workflow: select a scenario, run the verification, the RPM and temperature checks are done, the two are combined, and the result is shown on the dashboard.





12\. Technologies Used



Python

PyQt6

CSV data processing

Python pathlib

Python unittest

Matplotlib

Numerical and statistical analysis

Scenario-based simulation





13\. Engineering Relevance



The project relates to:

Process control

Instrumentation

Sensor verification

Fault detection

Embedded system development

Data acquisition

Power electronics and control system integration

Software testing

Engineering data analysis

GUI-based monitoring



The software can later be extended to take real measurements from a microcontroller or data acquisition system instead of simulated CSV data.





14\. Future Development



1\. Real RPM sensor integration.

2\. Real temperature sensor integration.

3\. STM32-based data acquisition.

4\. Closed loop motor speed control.

5\. Closed loop heater temperature control.

6\. Real-time dashboard updates.

7\. Sensor fault detection.

8\. Data logging.

9\. Automatic verification reports.

10\. Predictive maintenance indicators.

11\. Communication over UART, USB, CAN or another suitable interface.

12\. Hardware-in-the-loop testing.





15\. Limitations



This is currently a software simulation and verification prototype.



It does not provide:

Clinical validation.

Regulatory certification.

Manufacturer-specific performance validation.

Real centrifuge control.

Real heater control.

Real sensor acquisition.

Medical device safety validation.



The thresholds and scenarios are meant for engineering demonstration and software verification only.





16\. Project Status



RPM simulation: complete

Temperature simulation: complete

RPM analysis: complete

Temperature analysis: complete

RPM verification: complete

Temperature verification: complete

Combined verification: complete

Automated unit tests: complete

PyQt6 dashboard: complete

Scenario testing: complete

Documentation: in progress





17\. Conclusion



This project is a software proof of concept for monitoring and verifying two important gel card processing parameters: centrifuge speed and incubation temperature.



It covers the full workflow from simulated sensor data through analysis, fault detection, combined verification, automated testing and a graphical dashboard.



The structure is modular, so the simulated data sources can later be replaced with real sensor and controller interfaces.





Project classification: Self-directed engineering prototype

Validation level: Simulation and software verification

Manufacturer certification: None

