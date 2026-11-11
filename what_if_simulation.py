import os
import sys
import matplotlib.pyplot as plt

PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))

if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)

from ML_Model.ml_model import KneeMLModel
class WhatIfSimulator:

    def __init__(self, patient_meniscus, donor):

        self.patient_meniscus = patient_meniscus
        self.donor = donor

        self.model = KneeMLModel()

    def predict(
        self,
        donor_length,
        donor_width,
        donor_thickness
    ):

        result = self.model.predict_compatibility(
            self.patient_meniscus["Meniscus Length"],
            self.patient_meniscus["Meniscus Width"],
            self.patient_meniscus["Meniscus Thickness"],
            donor_length,
            donor_width,
            donor_thickness
        )

        return result

    def run_simulation(
        self,
        new_length=None,
        new_width=None,
        new_thickness=None
    ):

        original_length = float(
            self.donor["Length_mm"]
        )

        original_width = float(
            self.donor["Width_mm"]
        )

        original_thickness = float(
            self.donor["Thickness_mm"]
        )

        if new_length is None:
            new_length = original_length

        if new_width is None:
            new_width = original_width

        if new_thickness is None:
            new_thickness = original_thickness

        original_result = self.predict(
            original_length,
            original_width,
            original_thickness
        )

        new_result = self.predict(
            new_length,
            new_width,
            new_thickness
        )

        return {
            "Original": {
                "Length": original_length,
                "Width": original_width,
                "Thickness": original_thickness,
                "Prediction":
                    original_result["Compatibility"],
                "Confidence":
                    original_result["Confidence"]
            },

            "Modified": {
                "Length": new_length,
                "Width": new_width,
                "Thickness": new_thickness,
                "Prediction":
                    new_result["Compatibility"],
                "Confidence":
                    new_result["Confidence"]
            }
        }

    def display_simulation(
        self,
        new_length=None,
        new_width=None,
        new_thickness=None
    ):

        result = self.run_simulation(
            new_length,
            new_width,
            new_thickness
        )

        original = result["Original"]
        modified = result["Modified"]

        print("\n========================================")
        print("       KNEEPRINT WHAT-IF SIMULATION")
        print("========================================")

        print(
            f"\nDonor ID: "
            f"{self.donor['Donor_ID']}"
        )

        print("\n----------------------------------------")
        print("ORIGINAL DONOR")
        print("----------------------------------------")

        print(
            f"Length: "
            f"{original['Length']} mm"
        )

        print(
            f"Width: "
            f"{original['Width']} mm"
        )

        print(
            f"Thickness: "
            f"{original['Thickness']} mm"
        )

        print(
            f"Prediction: "
            f"{original['Prediction']}"
        )

        print(
            f"Confidence: "
            f"{original['Confidence'] * 100:.2f}%"
        )

        print("\n----------------------------------------")
        print("MODIFIED DONOR")
        print("----------------------------------------")

        print(
            f"Length: "
            f"{modified['Length']} mm"
        )

        print(
            f"Width: "
            f"{modified['Width']} mm"
        )

        print(
            f"Thickness: "
            f"{modified['Thickness']} mm"
        )

        print(
            f"Prediction: "
            f"{modified['Prediction']}"
        )

        print(
            f"Confidence: "
            f"{modified['Confidence'] * 100:.2f}%"
        )

        print("\n----------------------------------------")
        print("RESULT")
        print("----------------------------------------")

        if (
            original["Prediction"]
            != modified["Prediction"]
        ):
            print(
                "The ML compatibility "
                "prediction changed after "
                "the donor measurements "
                "were modified."
            )
        else:
            print(
                "The ML compatibility "
                "prediction remained the same."
            )

        self.create_visualization(
            original,
            modified
        )

    def create_visualization(
        self,
        original,
        modified
    ):

        measurements = [
            "Length",
            "Width",
            "Thickness"
        ]

        original_values = [
            original["Length"],
            original["Width"],
            original["Thickness"]
        ]

        modified_values = [
            modified["Length"],
            modified["Width"],
            modified["Thickness"]
        ]

        positions = range(len(measurements))

        plt.figure(figsize=(8, 5))

        plt.plot(
            positions,
            original_values,
            marker="o",
            label="Original"
        )

        plt.plot(
            positions,
            modified_values,
            marker="o",
            label="Modified"
        )

        plt.xticks(
            list(positions),
            measurements
        )

        plt.xlabel("Measurement")
        plt.ylabel("Value (mm)")

        plt.title(
            "KneePrint What-If Simulation"
        )

        plt.legend()

        plt.tight_layout()

        plt.show()


if __name__ == "__main__":

    patient = {
        "Meniscus Length": 42,
        "Meniscus Width": 28,
        "Meniscus Thickness": 8
    }

    donor = {
        "Donor_ID": "D024",
        "Length_mm": 41.6,
        "Width_mm": 29.0,
        "Thickness_mm": 8.0
    }

    simulator = WhatIfSimulator(
        patient,
        donor
    )

    simulator.display_simulation(
        new_length=42.5,
        new_width=28.5,
        new_thickness=8.2
    )