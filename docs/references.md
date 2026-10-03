References



1\. Project Scope



This project is a self-directed engineering and software prototype built to demonstrate process verification concepts for gel card processing equipment.



It is not an Origin-authorized project, not a medical device, not a clinical validation study, and not a manufacturer-certified verification system.



The RPM and temperature thresholds used here are test thresholds that I defined for this project. They must not be treated as manufacturer specifications or clinical acceptance limits.





2\. Gel Card Processing Context



Gel card immunohematology systems commonly use controlled centrifugation and incubation before the test results are interpreted.



This project focuses on two process variables:



Centrifugation speed integrity

Incubation temperature uniformity



The purpose is to show how measured process data can be analyzed automatically and turned into a PASS, WARNING or FAIL status.





3\. Bio-Rad Gel Card System Documentation



Bio-Rad provides gel card immunohematology systems that include dedicated centrifugation and incubation equipment.



Relevant product families include:



ID-Centrifuge and IH-Centrifuge systems

ID-Incubator and IH-Incubator systems

ID-System and IH-System gel card platforms



These products give the engineering context for studying controlled centrifugation and incubation processes.



Reference:

Bio-Rad Laboratories

https://www.bio-rad.com/





4\. Centrifugation Verification Concept



The prototype uses rotational speed measurements to evaluate centrifugation stability.



For each measurement:

deviation = measured\_RPM minus target\_RPM



The maximum absolute deviation is then calculated:

maximum\_deviation = max(abs(deviation))



The RPM thresholds defined for this project are:



PASS: maximum deviation of 5 RPM or less

WARNING: maximum deviation above 5 RPM and up to 10 RPM

FAIL: maximum deviation above 10 RPM



These thresholds are engineering assumptions for this software prototype. They are not manufacturer acceptance criteria.





5\. Temperature Verification Concept



The prototype evaluates incubation temperature stability around a target of 37.0 degrees Celsius.



For each measurement:

deviation = measured\_temperature minus target\_temperature



The maximum absolute deviation is calculated:

maximum\_deviation = max(abs(deviation))



The temperature thresholds defined for this project are:



PASS: maximum deviation of 0.2 degrees Celsius or less

WARNING: maximum deviation above 0.2 and up to 0.5 degrees Celsius

FAIL: maximum deviation above 0.5 degrees Celsius



These thresholds are engineering assumptions for simulation and software verification only.





6\. Statistical Analysis



The project uses basic statistical indicators to describe process stability:



Mean

Minimum

Maximum

Standard deviation

Maximum absolute deviation

Mean absolute deviation

Percentage of readings within the defined tolerance



These give a simple way to spot process drift, excessive variation and abnormal sensor behavior.





7\. Software Engineering References



The prototype is written in Python.



Main technologies:



Python

NumPy

Matplotlib

PyQt6

unittest

CSV-based data processing



Python documentation:

https://docs.python.org/3/



NumPy documentation:

https://numpy.org/doc/



Matplotlib documentation:

https://matplotlib.org/stable/



PyQt documentation:

https://doc.qt.io/qtforpython/





8\. Automated Testing



Python's built-in unittest framework is used to automatically verify the project's analysis and decision logic.



Python unittest documentation:

https://docs.python.org/3/library/unittest.html



The project currently has automated tests for:



Combined RPM and temperature verification

Normal operating scenarios

RPM fault scenarios

Temperature fault scenarios

Threshold classification





9\. Engineering Standards and Future Validation



A production implementation would need the right engineering standards, equipment specifications, calibration procedures, risk analysis, electrical safety requirements, software verification and any applicable regulatory requirements.



This project does not claim compliance with any specific medical device standard.



Future work would include reviewing the applicable standards and requirements before building a real hardware system.





10\. Important Limitations



The project uses simulated data.



It does not include:



Physical RPM sensor measurements

Physical temperature sensor measurements

Real centrifuge hardware

Real incubator hardware

Calibration-certified instruments

Clinical samples

Clinical validation

Manufacturer acceptance testing

Regulatory approval



The results therefore show a software verification method, not validated medical device performance.





11\. Project Status



The current implementation includes:



RPM simulation

Temperature simulation

RPM statistical analysis

Temperature statistical analysis

RPM fault scenarios

Temperature fault scenarios

Combined process verification

Automated unit tests

PyQt6 verification dashboard

Test plan

Research dossier

Project README



The project is currently a software and simulation proof of concept.





12\. Reference Usage Note



External references are used only to give the engineering and application context of the project.



The numerical thresholds and simulation scenarios were developed specifically for this prototype and are identified as project-defined values.



No project-defined threshold should be treated as an official specification unless it is independently validated against the equipment manufacturer's documentation or the relevant engineering and medical device requirements.



