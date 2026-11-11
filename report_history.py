import os
import json
from datetime import datetime


class KneePrintReportHistory:

    def __init__(self):

        self.module_folder = os.path.dirname(__file__)

        self.history_file = os.path.join(
            self.module_folder,
            "analysis_history.json"
        )

        self.report_folder = os.path.join(
            os.path.dirname(self.module_folder),
            "Analysis_Report"
        )

        os.makedirs(
            self.report_folder,
            exist_ok=True
        )

    def load_history(self):

        if not os.path.exists(self.history_file):
            return []

        try:
            with open(
                self.history_file,
                "r",
                encoding="utf-8"
            ) as file:

                return json.load(file)

        except json.JSONDecodeError:
            return []

    def save_analysis(
        self,
        patient_id,
        patient_meniscus,
        donor_result
    ):

        history = self.load_history()

        analysis = {
            "Analysis_ID": len(history) + 1,

            "Date_Time":
                datetime.now().strftime(
                    "%Y-%m-%d %H:%M:%S"
                ),

            "Patient_ID": patient_id,

            "Patient_KneePrint": {
                "Meniscus_Length":
                    float(
                        patient_meniscus[
                            "Meniscus Length"
                        ]
                    ),

                "Meniscus_Width":
                    float(
                        patient_meniscus[
                            "Meniscus Width"
                        ]
                    ),

                "Meniscus_Thickness":
                    float(
                        patient_meniscus[
                            "Meniscus Thickness"
                        ]
                    )
            },

            "Donor_Result": {
                "Donor_ID":
                    donor_result["Donor_ID"],

                "Compatibility":
                    donor_result["Compatibility"],

                "Confidence":
                    donor_result["Confidence"],

                "Length_mm":
                    donor_result["Length_mm"],

                "Width_mm":
                    donor_result["Width_mm"],

                "Thickness_mm":
                    donor_result["Thickness_mm"]
            }
        }

        history.append(analysis)

        with open(
            self.history_file,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                history,
                file,
                indent=4
            )

        return analysis

    def generate_report(
        self,
        patient_id,
        patient_meniscus,
        donor_result
    ):

        timestamp = datetime.now()

        filename = (
            f"KneePrint_Report_"
            f"{patient_id}_"
            f"{timestamp.strftime('%Y%m%d_%H%M%S')}"
            f".txt"
        )

        report_path = os.path.join(
            self.report_folder,
            filename
        )

        report = f"""
============================================================
                    KNEEPRINT
          ML-ASSISTED MENISCUS ANALYSIS
============================================================

PATIENT INFORMATION
------------------------------------------------------------
Patient ID       : {patient_id}
Analysis Date    : {timestamp.strftime('%Y-%m-%d')}
Analysis Time    : {timestamp.strftime('%H:%M:%S')}


PATIENT KNEEPRINT
------------------------------------------------------------
Meniscus Length    : {patient_meniscus['Meniscus Length']} mm
Meniscus Width     : {patient_meniscus['Meniscus Width']} mm
Meniscus Thickness : {patient_meniscus['Meniscus Thickness']} mm


ML DONOR ANALYSIS
------------------------------------------------------------
Donor ID           : {donor_result['Donor_ID']}
Compatibility      : {donor_result['Compatibility']}
ML Confidence      : {donor_result['Confidence'] * 100:.2f}%

Donor Dimensions
Length             : {donor_result['Length_mm']} mm
Width              : {donor_result['Width_mm']} mm
Thickness          : {donor_result['Thickness_mm']} mm


ANALYSIS SUMMARY
------------------------------------------------------------
The KneePrint system used a Random Forest machine-learning
model to classify the compatibility of the selected donor
with the entered KneePrint measurements.

The prediction represents the output of the trained
educational machine-learning model.


IMPORTANT DISCLAIMER
------------------------------------------------------------
This software is an educational prototype.

The donor data used by this project is synthetic/sample data.
The machine-learning model is intended to demonstrate an
ML-based compatibility analysis workflow.

The generated result does NOT determine clinical suitability,
medical compatibility, transplant eligibility, or treatment.

Clinical decisions must be made by qualified medical
professionals using validated clinical methods and data.


============================================================
                  END OF KNEEPRINT REPORT
============================================================
"""

        with open(
            report_path,
            "w",
            encoding="utf-8"
        ) as file:

            file.write(report)

        return report_path

    def display_history(self):

        history = self.load_history()

        print("\n========================================")
        print("          KNEEPRINT HISTORY")
        print("========================================")

        if not history:
            print("\nNo previous analyses found.")
            return

        for analysis in history:

            print(
                f"\nAnalysis ID : "
                f"{analysis['Analysis_ID']}"
            )

            print(
                f"Date        : "
                f"{analysis['Date_Time']}"
            )

            print(
                f"Patient ID  : "
                f"{analysis['Patient_ID']}"
            )

            print(
                f"Donor ID    : "
                f"{analysis['Donor_Result']['Donor_ID']}"
            )

            print(
                f"Compatibility : "
                f"{analysis['Donor_Result']['Compatibility']}"
            )

            print(
                f"Confidence    : "
                f"{analysis['Donor_Result']['Confidence'] * 100:.2f}%"
            )

            print("----------------------------------------")


if __name__ == "__main__":

    patient = {
        "Meniscus Length": 42,
        "Meniscus Width": 28,
        "Meniscus Thickness": 8
    }

    donor = {
        "Donor_ID": "D024",
        "Compatibility": "High",
        "Confidence": 0.95,
        "Length_mm": 41.6,
        "Width_mm": 29.0,
        "Thickness_mm": 8.0
    }

    manager = KneePrintReportHistory()

    saved_analysis = manager.save_analysis(
        patient_id="KP001",
        patient_meniscus=patient,
        donor_result=donor
    )

    report_path = manager.generate_report(
        patient_id="KP001",
        patient_meniscus=patient,
        donor_result=donor
    )

    print("\n========================================")
    print("       KNEEPRINT REPORT SYSTEM")
    print("========================================")

    print("\nAnalysis saved successfully.")

    print(
        f"\nReport created at:\n{report_path}"
    )

    manager.display_history()