Research Dossier



Closed Loop Process Control for Gel Card Processing



Centrifugation Speed Integrity and Incubation Thermal Uniformity



Author: Afzal Khurshid

Program: Electrical Engineering

Institution: University of Engineering and Technology (UET), Lahore

Project type: Self-directed engineering research and software prototype





1\. Executive Summary



This project looks at a software-based way of verifying two important parameters in gel card processing:



1\. Centrifugation speed.

2\. Incubation temperature.



The goal is to show how measured process values can be checked continuously against defined engineering thresholds and turned into a clear process status.



I built a simulation environment that generates normal and abnormal RPM and temperature measurements. The simulated data is analyzed statistically, then each parameter is verified on its own, and finally the two results are combined into an overall process status.



A PyQt6 dashboard lets the user select a scenario and see the RPM status, temperature status and overall status.



The current implementation is a software proof of concept. It is meant as a base for future hardware integration.





2\. Engineering Problem



Gel card processing needs controlled conditions during centrifugation and incubation.



The two important parameters are:



Rotational speed during centrifugation.

Temperature during incubation.



A process can run into:



Speed drift.

Excessive speed deviation.

Temperature drift.

Temperature overshoot.

Temperature undershoot.

Sensor noise.



A simple timer-based controller can tell you that a programmed run has finished, but it does not necessarily tell you whether the actual conditions stayed within the desired range.



This project therefore explores an architecture built around verification, where process measurements are analyzed and classified continuously.





3\. Proposed Concept



The concept has five stages:



Measurement, then data processing, then deviation analysis, then parameter verification, then combined process status.



In the current prototype, the measurement stage is simulated using generated CSV datasets.



In a future hardware version, the simulated source could be replaced by real sensors and a microcontroller-based data acquisition system.





4\. RPM Verification Concept



The centrifugation target speed is 1600 RPM.



For each simulated measurement, the RPM deviation is the measured RPM minus the target RPM.



The absolute deviation is used to find the largest departure from the target.



The prototype uses these thresholds:



PASS: maximum absolute deviation of 5 RPM or less.

WARNING: maximum absolute deviation above 5 RPM and up to 10 RPM.

FAIL: maximum absolute deviation above 10 RPM.



These limits are engineering test thresholds that I defined for this project. They are not manufacturer specifications.





5\. Temperature Verification Concept



The incubation target temperature is 37.0 degrees Celsius.



For each measurement, the temperature deviation is the measured temperature minus the target temperature.



The maximum absolute deviation is then evaluated.



The prototype uses these thresholds:



PASS: maximum absolute deviation of 0.2 degrees Celsius or less.

WARNING: maximum absolute deviation above 0.2 and up to 0.5 degrees Celsius.

FAIL: maximum absolute deviation above 0.5 degrees Celsius.



These are also project-defined test thresholds. They are not clinical or manufacturer limits.





6\. Simulation Methodology



The simulation environment produces datasets that represent different process conditions.



RPM scenarios



Normal: measurements stay close to the 1600 RPM target.

RPM drift: the simulated speed slowly moves away from the target.

High RPM deviation: measurements are above the target.

Low RPM deviation: measurements are below the target.

Noisy RPM sensor: measurements vary much more, to represent a noisy signal.





7\. Temperature Scenarios



Normal: measurements stay close to 37.0 degrees Celsius.

Temperature drift: the simulated temperature slowly moves away from the target.

High temperature: measurements are above the target.

Low temperature: measurements are below the target.

Noisy temperature sensor: measurements show more variation.





8\. Statistical Analysis



The simulated measurements are analyzed using these indicators:



Average value.

Minimum value.

Maximum value.

Standard deviation.

Maximum absolute deviation.

Mean absolute deviation.

Percentage of measurements within a defined tolerance.



Together these show both the central behavior and the stability of the simulated process.





9\. Baseline RPM Results



For the normal simulated RPM dataset:



Target: 1600.00 RPM

Average: 1600.15 RPM

Minimum: 1595.51 RPM

Maximum: 1603.93 RPM

Standard deviation: 1.91 RPM

Maximum deviation: 4.49 RPM

Mean absolute deviation: 1.41 RPM



The maximum deviation stayed within the PASS threshold, so the RPM verification result is PASS.





10\. Baseline Temperature Results



For the normal simulated temperature dataset:



Target: 37.000 degrees Celsius

Average: 37.004 degrees Celsius

Minimum: 36.880 degrees Celsius

Maximum: 37.105 degrees Celsius

Standard deviation: 0.051 degrees Celsius

Maximum deviation: 0.120 degrees Celsius

Mean absolute deviation: 0.038 degrees Celsius



The maximum deviation stayed within the PASS threshold, so the temperature verification result is PASS.





11\. Combined Verification Architecture



The two verification channels work independently. The RPM measurements go through RPM verification, and the temperature measurements go through temperature verification. Both results then feed into the combined logic.



The combined logic is:



If any parameter is FAIL, the overall status is FAIL.

Otherwise, if any parameter is WARNING, the overall status is WARNING.

Otherwise, the overall status is PASS.



This lets the dashboard separate normal operation from abnormal process conditions.





12\. Scenario Verification Results



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



These results show how the verification logic behaves under the simulated scenarios.





13\. Software Architecture



The project is divided into functional modules.



Simulator (folder: simulator)

Generates the synthetic measurement datasets.



Analysis (folder: analysis)

Calculates statistics and deviations.



Verification (files: analysis/rpm\_verification.py, analysis/temperature\_verification.py, analysis/combined\_verification.py)

Classifies measurements using the project-defined thresholds.



Testing (folder: tests)

Provides automated checks of the software behavior.



Dashboard (folder: dashboard)

Shows the verification results graphically.



Results (folder: results)

Stores the generated CSV data and plots.





14\. Testing Strategy



The software uses automated unit tests. Two test groups are implemented.



Combined verification tests

Eight tests check the combined status decision logic. The combinations tested are:

PASS and PASS

FAIL and PASS

PASS and FAIL

FAIL and FAIL

WARNING and PASS

PASS and WARNING

WARNING and FAIL

WARNING and WARNING

All eight tests passed.



Threshold tests

Ten tests check the RPM and temperature scenario classification. All ten tests passed.



Total automated tests: 18





15\. Dashboard Concept



The PyQt6 dashboard gives a readable interface to the verification system.



The user selects a simulated scenario and runs the verification.



The dashboard displays:

RPM integrity status.

Temperature integrity status.

Overall process status.

Maximum RPM deviation.

Maximum temperature deviation.

Target RPM.

Target temperature.

Verification thresholds.



In this way the dashboard works as a visualization layer on top of the verification engine.





16\. Potential Hardware Architecture



The current project uses simulated CSV measurements.



A future hardware version could be structured like this:



RPM path: an RPM sensor feeds a microcontroller. The microcontroller handles RPM processing, data logging and communication. The data is then sent to the verification software, which feeds the dashboard.



Temperature path: a temperature sensor feeds a microcontroller. The microcontroller handles temperature processing and heater control.



The microcontroller platform can be chosen based on the sensor interfaces, motor control needs, communication needs and other system constraints.





17\. Closed Loop Extension



The current implementation only performs verification.



A future version could extend this into closed loop control. For example, in the RPM loop, an RPM setpoint goes to a controller, the controller drives a motor driver, the motor driver runs the centrifuge motor, and an RPM sensor feeds the measured speed back to the controller.



(The original document ended at this point, so this section is incomplete.)



