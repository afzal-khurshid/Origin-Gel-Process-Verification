import sys
from pathlib import Path

sys.path.insert(
    0,
    str(Path(__file__).resolve().parents[1])
)

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import (
    QApplication,
    QComboBox,
    QGridLayout,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget
)

from analysis.combined_verification import ProcessVerifier


class StatusCard(QGroupBox):

    def __init__(self, title):
        super().__init__()

        self.setTitle(title)

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.status_label = QLabel("NOT TESTED")
        self.status_label.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        self.status_label.setFont(
            QFont("Arial", 22, QFont.Weight.Bold)
        )

        self.value_label = QLabel("--")
        self.value_label.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        self.value_label.setFont(
            QFont("Arial", 11)
        )

        layout.addWidget(
            self.status_label
        )

        layout.addWidget(
            self.value_label
        )

        self.set_status("NOT TESTED")

    def set_status(self, status):

        self.status_label.setText(
            status
        )

        if status == "PASS":
            self.status_label.setStyleSheet(
                """
                QLabel {
                    color: green;
                    font-weight: bold;
                    padding: 15px;
                }
                """
            )

        elif status == "WARNING":
            self.status_label.setStyleSheet(
                """
                QLabel {
                    color: orange;
                    font-weight: bold;
                    padding: 15px;
                }
                """
            )

        elif status == "FAIL":
            self.status_label.setStyleSheet(
                """
                QLabel {
                    color: red;
                    font-weight: bold;
                    padding: 15px;
                }
                """
            )

        else:
            self.status_label.setStyleSheet(
                """
                QLabel {
                    color: gray;
                    font-weight: bold;
                    padding: 15px;
                }
                """
            )


class ProcessDashboard(QMainWindow):

    def __init__(self):

        super().__init__()

        self.setWindowTitle(
            "Origin Gel Process Verification Dashboard"
        )

        self.setMinimumSize(
            900,
            600
        )

        self.results_folder = (
            Path(__file__).resolve().parents[1]
            / "results"
        )

        self.verifier = ProcessVerifier()

        self.scenarios = {
            "NORMAL": (
                "normal_rpm.csv",
                "normal_temperature.csv"
            ),
            "RPM DRIFT": (
                "rpm_drift_rpm.csv",
                "normal_temperature.csv"
            ),
            "HIGH RPM DEVIATION": (
                "high_deviation_rpm.csv",
                "normal_temperature.csv"
            ),
            "LOW RPM DEVIATION": (
                "low_deviation_rpm.csv",
                "normal_temperature.csv"
            ),
            "NOISY RPM SENSOR": (
                "noisy_sensor_rpm.csv",
                "normal_temperature.csv"
            ),
            "TEMPERATURE DRIFT": (
                "normal_rpm.csv",
                "temperature_drift_temperature.csv"
            ),
            "HIGH TEMPERATURE": (
                "normal_rpm.csv",
                "high_temperature_temperature.csv"
            ),
            "LOW TEMPERATURE": (
                "normal_rpm.csv",
                "low_temperature_temperature.csv"
            ),
            "NOISY TEMPERATURE SENSOR": (
                "normal_rpm.csv",
                "noisy_sensor_temperature.csv"
            )
        }

        self.create_ui()

    def create_ui(self):

        central_widget = QWidget()

        self.setCentralWidget(
            central_widget
        )

        main_layout = QVBoxLayout()

        central_widget.setLayout(
            main_layout
        )

        title = QLabel(
            "ORIGIN GEL PROCESS VERIFICATION"
        )

        title.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        title.setFont(
            QFont("Arial", 24, QFont.Weight.Bold)
        )

        main_layout.addWidget(
            title
        )

        subtitle = QLabel(
            "Closed-Loop RPM & Temperature Integrity Prototype"
        )

        subtitle.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        subtitle.setFont(
            QFont("Arial", 12)
        )

        main_layout.addWidget(
            subtitle
        )

        scenario_group = QGroupBox(
            "Test Scenario"
        )

        scenario_layout = QHBoxLayout()

        scenario_group.setLayout(
            scenario_layout
        )

        scenario_label = QLabel(
            "Select Scenario:"
        )

        self.scenario_box = QComboBox()

        self.scenario_box.addItems(
            self.scenarios.keys()
        )

        self.run_button = QPushButton(
            "RUN VERIFICATION"
        )

        self.run_button.setMinimumHeight(
            40
        )

        self.run_button.clicked.connect(
            self.run_verification
        )

        scenario_layout.addWidget(
            scenario_label
        )

        scenario_layout.addWidget(
            self.scenario_box
        )

        scenario_layout.addWidget(
            self.run_button
        )

        main_layout.addWidget(
            scenario_group
        )

        cards_layout = QGridLayout()

        self.rpm_card = StatusCard(
            "RPM INTEGRITY"
        )

        self.temperature_card = StatusCard(
            "TEMPERATURE INTEGRITY"
        )

        self.overall_card = StatusCard(
            "OVERALL PROCESS STATUS"
        )

        cards_layout.addWidget(
            self.rpm_card,
            0,
            0
        )

        cards_layout.addWidget(
            self.temperature_card,
            0,
            1
        )

        cards_layout.addWidget(
            self.overall_card,
            0,
            2
        )

        main_layout.addLayout(
            cards_layout
        )

        measurements_group = QGroupBox(
            "Verification Measurements"
        )

        measurements_layout = QGridLayout()

        measurements_group.setLayout(
            measurements_layout
        )

        measurements_layout.addWidget(
            QLabel("RPM Target:"),
            0,
            0
        )

        measurements_layout.addWidget(
            QLabel("1600 RPM"),
            0,
            1
        )

        measurements_layout.addWidget(
            QLabel("Maximum RPM Deviation:"),
            1,
            0
        )

        self.rpm_deviation = QLabel(
            "--"
        )

        measurements_layout.addWidget(
            self.rpm_deviation,
            1,
            1
        )

        measurements_layout.addWidget(
            QLabel("Temperature Target:"),
            0,
            2
        )

        measurements_layout.addWidget(
            QLabel("37.0 °C"),
            0,
            3
        )

        measurements_layout.addWidget(
            QLabel("Maximum Temperature Deviation:"),
            1,
            2
        )

        self.temperature_deviation = QLabel(
            "--"
        )

        measurements_layout.addWidget(
            self.temperature_deviation,
            1,
            3
        )

        main_layout.addWidget(
            measurements_group
        )

        thresholds_group = QGroupBox(
            "Project-Defined Verification Thresholds"
        )

        thresholds_layout = QGridLayout()

        thresholds_group.setLayout(
            thresholds_layout
        )

        thresholds_layout.addWidget(
            QLabel("RPM PASS:"),
            0,
            0
        )

        thresholds_layout.addWidget(
            QLabel("≤ 5 RPM"),
            0,
            1
        )

        thresholds_layout.addWidget(
            QLabel("RPM WARNING:"),
            0,
            2
        )

        thresholds_layout.addWidget(
            QLabel("≤ 10 RPM"),
            0,
            3
        )

        thresholds_layout.addWidget(
            QLabel("Temperature PASS:"),
            1,
            0
        )

        thresholds_layout.addWidget(
            QLabel("≤ 0.2 °C"),
            1,
            1
        )

        thresholds_layout.addWidget(
            QLabel("Temperature WARNING:"),
            1,
            2
        )

        thresholds_layout.addWidget(
            QLabel("≤ 0.5 °C"),
            1,
            3
        )

        main_layout.addWidget(
            thresholds_group
        )

        self.scenario_label = QLabel(
            "Scenario: NOT TESTED"
        )

        self.scenario_label.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        self.scenario_label.setFont(
            QFont("Arial", 11)
        )

        main_layout.addWidget(
            self.scenario_label
        )

        disclaimer = QLabel(
            "Simulation/prototype verification only. "
            "Thresholds are project-defined engineering "
            "test thresholds and are not manufacturer or "
            "clinical specifications."
        )

        disclaimer.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        disclaimer.setWordWrap(
            True
        )

        main_layout.addWidget(
            disclaimer
        )

    def run_verification(self):

        scenario = (
            self.scenario_box.currentText()
        )

        rpm_file, temperature_file = (
            self.scenarios[scenario]
        )

        rpm_path = (
            self.results_folder
            / rpm_file
        )

        temperature_path = (
            self.results_folder
            / temperature_file
        )

        rpm_result = (
            self.verifier.verify_rpm(
                rpm_path
            )
        )

        temperature_result = (
            self.verifier.verify_temperature(
                temperature_path
            )
        )

        overall_status = (
            self.verifier.combine_statuses(
                rpm_result["status"],
                temperature_result["status"]
            )
        )

        self.rpm_card.set_status(
            rpm_result["status"]
        )

        self.temperature_card.set_status(
            temperature_result["status"]
        )

        self.overall_card.set_status(
            overall_status
        )

        self.rpm_card.value_label.setText(
            f"Maximum deviation: "
            f"{rpm_result['maximum_deviation']:.2f} RPM"
        )

        self.temperature_card.value_label.setText(
            f"Maximum deviation: "
            f"{temperature_result['maximum_deviation']:.3f} °C"
        )

        self.rpm_deviation.setText(
            f"{rpm_result['maximum_deviation']:.2f} RPM"
        )

        self.temperature_deviation.setText(
            f"{temperature_result['maximum_deviation']:.3f} °C"
        )

        self.scenario_label.setText(
            f"Scenario: {scenario}"
        )


if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = ProcessDashboard()

    window.show()

    sys.exit(
        app.exec()
    )