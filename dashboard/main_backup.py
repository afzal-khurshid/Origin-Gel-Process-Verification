import sys
from pathlib import Path
sys.path.insert(
    0,
    str(Path(__file__).resolve().parents[1])
)

from PyQt6.QtWidgets import (
    QApplication,
    QComboBox,
    QGridLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget
)

from analysis.combined_verification import ProcessVerifier


class ProcessDashboard(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle(
            "Origin Gel Process Verification Dashboard"
        )

        self.setMinimumSize(700, 450)

        self.results_folder = (
            Path(__file__).resolve().parents[1] / "results"
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
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)

        title = QLabel(
            "ORIGIN GEL PROCESS VERIFICATION"
        )

        title.setStyleSheet(
            "font-size: 24px; font-weight: bold;"
        )

        main_layout.addWidget(title)

        subtitle = QLabel(
            "RPM + Temperature Verification"
        )

        subtitle.setStyleSheet(
            "font-size: 16px;"
        )

        main_layout.addWidget(subtitle)

        self.scenario_box = QComboBox()

        self.scenario_box.addItems(
            self.scenarios.keys()
        )

        main_layout.addWidget(
            QLabel("Select Test Scenario:")
        )

        main_layout.addWidget(
            self.scenario_box
        )

        self.run_button = QPushButton(
            "RUN VERIFICATION"
        )

        self.run_button.clicked.connect(
            self.run_verification
        )

        main_layout.addWidget(
            self.run_button
        )

        grid = QGridLayout()

        grid.addWidget(
            QLabel("RPM Status"),
            0,
            0
        )

        grid.addWidget(
            QLabel("Temperature Status"),
            0,
            1
        )

        grid.addWidget(
            QLabel("Overall Status"),
            0,
            2
        )

        self.rpm_status = QLabel("NOT TESTED")
        self.temperature_status = QLabel("NOT TESTED")
        self.overall_status = QLabel("NOT TESTED")

        self.rpm_status.setStyleSheet(
            "font-size: 20px; font-weight: bold;"
        )

        self.temperature_status.setStyleSheet(
            "font-size: 20px; font-weight: bold;"
        )

        self.overall_status.setStyleSheet(
            "font-size: 20px; font-weight: bold;"
        )

        grid.addWidget(
            self.rpm_status,
            1,
            0
        )

        grid.addWidget(
            self.temperature_status,
            1,
            1
        )

        grid.addWidget(
            self.overall_status,
            1,
            2
        )

        main_layout.addLayout(grid)

        self.rpm_deviation = QLabel(
            "Maximum RPM deviation: --"
        )

        self.temperature_deviation = QLabel(
            "Maximum temperature deviation: --"
        )

        main_layout.addWidget(
            self.rpm_deviation
        )

        main_layout.addWidget(
            self.temperature_deviation
        )

        self.info_label = QLabel(
            "Select a scenario and press RUN VERIFICATION."
        )

        main_layout.addWidget(
            self.info_label
        )

    def run_verification(self):

        scenario = self.scenario_box.currentText()

        rpm_file, temperature_file = (
            self.scenarios[scenario]
        )

        rpm_path = (
            self.results_folder / rpm_file
        )

        temperature_path = (
            self.results_folder / temperature_file
        )

        rpm_result = self.verifier.verify_rpm(
            rpm_path
        )

        temperature_result = (
            self.verifier.verify_temperature(
                temperature_path
            )
        )

        overall = (
            self.verifier.combine_statuses(
                rpm_result["status"],
                temperature_result["status"]
            )
        )

        self.rpm_status.setText(
            rpm_result["status"]
        )

        self.temperature_status.setText(
            temperature_result["status"]
        )

        self.overall_status.setText(
            overall
        )

        self.rpm_deviation.setText(
            f"Maximum RPM deviation: "
            f"{rpm_result['maximum_deviation']:.2f} RPM"
        )

        self.temperature_deviation.setText(
            f"Maximum temperature deviation: "
            f"{temperature_result['maximum_deviation']:.3f} °C"
        )

        self.info_label.setText(
            f"Scenario: {scenario}"
        )


if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = ProcessDashboard()

    window.show()

    sys.exit(
        app.exec()
    )