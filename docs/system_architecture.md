System Architecture



1\. Overview



The Origin Gel Process Verification prototype is built as a modular software system for monitoring and verifying two process variables:



1\. Centrifugation speed

2\. Incubation temperature



The system takes simulated measurement data, calculates deviations from the target values, classifies the process condition, and shows the verification result on a graphical dashboard.



The architecture is designed so that the simulated sensors can later be replaced by real hardware sensors without changing the overall verification concept.





2\. High-Level Architecture



The processing flow is:



Simulated process data goes to the data generation layer, then the data analysis layer, then the verification layer, then the combined process decision, and finally the dashboard.



There are two main measurement paths. The RPM data goes through RPM analysis and then RPM verification. The temperature data goes through temperature analysis and then temperature verification. Both verification results then feed into the combined verification stage.





3\. Major Software Components



3.1 Simulator Layer



Location: simulator



The simulator layer generates synthetic measurement data for different operating conditions.



RPM simulator: simulator/rpm\_simulator.py

RPM scenarios: simulator/run\_scenarios.py

Temperature simulator: simulator/temperature\_simulator.py

Temperature scenarios: simulator/temperature\_scenarios.py



The simulator allows controlled testing of normal operation, process drift, excessive deviation and noisy sensor conditions.





4\. RPM Analysis Layer



Location: analysis/rpm\_analysis.py



The RPM analysis module reads the RPM measurement data and calculates:



Average RPM

Minimum RPM

Maximum RPM

Standard deviation

Maximum absolute deviation

Mean absolute deviation

Percentage within tolerance



The target RPM in the current prototype is 1600 RPM.





5\. Temperature Analysis Layer



Location: analysis/temperature\_analysis.py



The temperature analysis module processes the temperature measurements and calculates:



Average temperature

Minimum temperature

Maximum temperature

Standard deviation

Maximum absolute deviation

Mean absolute deviation

Percentage within tolerance



The target temperature in the current prototype is 37.0 degrees Celsius.





6\. Verification Layer



The verification layer converts the numerical measurements into status categories.



The categories are PASS, WARNING and FAIL.



RPM verification

Thresholds defined for this project:

Maximum deviation of 5 RPM or less: PASS

Above 5 RPM and up to 10 RPM: WARNING

Above 10 RPM: FAIL



Temperature verification

Thresholds defined for this project:

Maximum deviation of 0.2 degrees Celsius or less: PASS

Above 0.2 and up to 0.5 degrees Celsius: WARNING

Above 0.5 degrees Celsius: FAIL



These thresholds are prototype engineering values. They are not manufacturer or clinical acceptance limits.





7\. Combined Verification



Location: analysis/combined\_verification.py



The ProcessVerifier class combines the RPM and temperature verification results.



The decision logic is:



If RPM is FAIL or Temperature is FAIL, the overall status is FAIL.

Otherwise, if RPM is WARNING or Temperature is WARNING, the overall status is WARNING.

Otherwise, the overall status is PASS.



This makes sure that a serious fault in either variable causes the whole process verification to fail.





8\. Dashboard Layer



Location: dashboard/main.py



The dashboard is a graphical interface for running the verification.



It displays:



Selected scenario

RPM status

Temperature status

Overall process status

RPM target

Temperature target

Maximum RPM deviation

Maximum temperature deviation

Project-defined thresholds



The interface uses PyQt6.



The dashboard is a prototype monitoring interface, not a production control system.





9\. Data Flow



The complete data flow is as follows.



Step 1, Generate data

The simulator generates measurement samples.

Example: target RPM is 1600, and sample measurements are 1598.9, 1600.7, 1601.2, 1599.6 and so on.



Step 2, Calculate deviation

For RPM: deviation = measured\_RPM minus target\_RPM

For temperature: deviation = measured\_temperature minus target\_temperature



Step 3, Calculate statistics

The analysis modules calculate the average, minimum, maximum, standard deviation, maximum deviation and mean absolute deviation.



Step 4, Verify limits

The verification layer compares the maximum deviation with the project-defined limits.

Example: the RPM maximum deviation is 4.49 RPM, which is within 5 RPM, so the result is PASS.



Step 5, Combine results

The RPM and temperature statuses are combined into one process status.

Example: RPM is PASS and temperature is PASS, so the overall result is PASS.



Step 6, Display result

The dashboard shows the verification result to the user.





10\. Fault Detection Architecture



The architecture supports simulated fault conditions.



RPM faults:

RPM drift

High RPM deviation

Low RPM deviation

Noisy RPM sensor



Temperature faults:

Temperature drift

High temperature

Low temperature

Noisy temperature sensor



The same verification mechanism is used for both normal and abnormal conditions.





11\. Testing Architecture



Location: tests



Automated testing uses Python's unittest framework.



Current test modules:

tests/test\_combined\_verification.py

tests/test\_thresholds.py



The tests verify:



Normal operation

RPM fault detection

Temperature fault detection

Combined status logic

Threshold classification



Current automated test count: 18 tests

Current result: all 18 tests pass





12\. Future Hardware Architecture



The simulator can later be replaced by physical sensors.



A possible future structure is: an RPM sensor feeds a microcontroller, which does the RPM processing and passes the result to a process controller. A temperature sensor feeds temperature processing, which also goes to the same process controller.



The microcontroller could send the measurement data to a computer or an embedded dashboard.



Possible communication methods:

USB serial

UART

RS-485

Ethernet

Wi-Fi



The right interface would depend on the final hardware design and system requirements.





13\. Closed Loop Extension



A future hardware version could extend the verification architecture into a closed loop control system.



General concept: a sensor gives a measurement, the measurement goes to a controller, the controller drives an actuator, the actuator acts on the process, and the sensor measures the process again.



For centrifugation: the RPM sensor feeds the controller, the controller drives the motor driver, the motor driver runs the centrifuge motor, and the RPM sensor measures the speed again.



For incubation: the temperature sensor feeds the controller, the controller drives the heater control, the heater control heats the incubation chamber, and the temperature sensor measures the temperature again.



This would let the system keep measuring the process and adjust the actuator output.





14\. Future Monitoring Features



Possible future extensions:



Real-time sensor monitoring

Data logging

Alarm generation

Sensor fault detection

Calibration reminders

Historical trend analysis

Process deviation tracking

Predictive maintenance indicators

Remote monitoring

Hardware-in-the-loop testing



These are future development directions and are not part of the current validated functionality.





15\. Engineering Boundaries



The current architecture is a software and simulation proof of concept.



It does not control real laboratory equipment.

It does not perform clinical interpretation.

It does not provide medical diagnosis.

It does not replace equipment calibration.

It does not demonstrate regulatory compliance.



Any future hardware version would need the proper electrical, mechanical, software, safety, calibration and regulatory engineering work.





16\. Architecture Summary



The architecture separates the project into independent layers: simulation, analysis, verification, combined decision and dashboard.



Because of this modular structure, the simulated measurements can be replaced with real sensor data while the core analysis and verification logic stays the same.



The architecture therefore gives a base for future development toward a hardware-integrated process monitoring and closed loop control prototype.



