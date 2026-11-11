import os
import sys

# Allow this file to access the existing project modules
PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))

if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)

from Donor_Database.donor_database import DonorDatabase
from ML_Model.ml_model import KneeMLModel


class MLDonorMatcher:

    def __init__(self, patient_meniscus, donor_records=None):

        self.patient_meniscus = patient_meniscus

        if donor_records is None:
            database = DonorDatabase()
            database.load_donors()
            donor_records = database.get_donors()

        self.donor_records = donor_records

        self.ml_model = KneeMLModel()

    def match_donors(self):

        results = []

        patient_length = float(
            self.patient_meniscus["Meniscus Length"]
        )

        patient_width = float(
            self.patient_meniscus["Meniscus Width"]
        )

        patient_thickness = float(
            self.patient_meniscus["Meniscus Thickness"]
        )

        for donor in self.donor_records:

            donor_length = float(
                donor["Length_mm"]
            )

            donor_width = float(
                donor["Width_mm"]
            )

            donor_thickness = float(
                donor["Thickness_mm"]
            )

            prediction = self.ml_model.predict_compatibility(
                patient_length,
                patient_width,
                patient_thickness,
                donor_length,
                donor_width,
                donor_thickness
            )

            results.append({
                "Donor_ID": donor["Donor_ID"],
                "Side": donor["Side"],
                "Meniscus_Type": donor["Meniscus_Type"],
                "Length_mm": donor_length,
                "Width_mm": donor_width,
                "Thickness_mm": donor_thickness,
                "Compatibility": prediction["Compatibility"],
                "Confidence": prediction["Confidence"],
                "Probabilities": prediction["Probabilities"]
            })

        # Rank the compatibility classes
        compatibility_order = {
            "High": 1,
            "Medium": 2,
            "Low": 3
        }

        results.sort(
            key=lambda result: (
                compatibility_order.get(
                    result["Compatibility"], 4
                ),
                -result["Confidence"]
            )
        )

        return results

    def get_top_matches(self, number_of_matches=5):

        results = self.match_donors()

        return results[:number_of_matches]

    def display_matches(self, number_of_matches=5):

        matches = self.get_top_matches(
            number_of_matches
        )

        print("\n========================================")
        print("       KNEEPRINT ML DONOR MATCHING")
        print("========================================")

        print(
            f"\nPatient KneePrint:"
            f"\nLength: "
            f"{self.patient_meniscus['Meniscus Length']} mm"
            f"\nWidth: "
            f"{self.patient_meniscus['Meniscus Width']} mm"
            f"\nThickness: "
            f"{self.patient_meniscus['Meniscus Thickness']} mm"
        )

        print("\n----------------------------------------")
        print("TOP ML MATCHES")
        print("----------------------------------------")

        for rank, donor in enumerate(
            matches,
            start=1
        ):

            print(
                f"\nRank {rank}"
            )

            print(
                f"Donor ID      : "
                f"{donor['Donor_ID']}"
            )

            print(
                f"Side          : "
                f"{donor['Side']}"
            )

            print(
                f"Meniscus Type : "
                f"{donor['Meniscus_Type']}"
            )

            print(
                f"Compatibility : "
                f"{donor['Compatibility']}"
            )

            print(
                f"Confidence    : "
                f"{donor['Confidence'] * 100:.2f}%"
            )

            print(
                f"Dimensions    : "
                f"{donor['Length_mm']} × "
                f"{donor['Width_mm']} × "
                f"{donor['Thickness_mm']} mm"
            )


if __name__ == "__main__":

    # Example patient KneePrint
    patient = {
        "Meniscus Length": 42,
        "Meniscus Width": 28,
        "Meniscus Thickness": 8
    }

    matcher = MLDonorMatcher(patient)

    matcher.display_matches(5)