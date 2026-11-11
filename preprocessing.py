import os
import random
import pandas as pd


class KneeDataPreprocessor:

    def __init__(self, donor_file=None):
        if donor_file is None:
            donor_file = os.path.join(
                os.path.dirname(os.path.dirname(__file__)),
                "Donor_Database",
                "donor_database.csv"
            )

        self.donor_file = donor_file

    def load_donor_data(self):
        """Load donor measurements from the existing donor database."""

        return pd.read_csv(self.donor_file)

    def generate_training_data(self, number_of_samples=2000):
        """
        Generate synthetic patient-donor pairs for ML training.

        This dataset is for educational simulation only.
        """

        donors = self.load_donor_data()

        training_records = []

        for _ in range(number_of_samples):

            donor = donors.sample(
                n=1,
                random_state=random.randint(0, 100000)
            ).iloc[0]

            # Generate a synthetic patient measurement
            patient_length = round(
                random.uniform(38.0, 46.0), 1
            )

            patient_width = round(
                random.uniform(25.0, 32.0), 1
            )

            patient_thickness = round(
                random.uniform(7.0, 9.5), 1
            )

            donor_length = float(donor["Length_mm"])
            donor_width = float(donor["Width_mm"])
            donor_thickness = float(donor["Thickness_mm"])

            # Calculate dimensional differences
            length_difference = abs(
                patient_length - donor_length
            )

            width_difference = abs(
                patient_width - donor_width
            )

            thickness_difference = abs(
                patient_thickness - donor_thickness
            )

            # Relative differences
            length_relative_difference = (
                length_difference / patient_length
            )

            width_relative_difference = (
                width_difference / patient_width
            )

            thickness_relative_difference = (
                thickness_difference / patient_thickness
            )

            # Combined compatibility measure
            compatibility_measure = (
                (length_relative_difference * 0.40)
                + (width_relative_difference * 0.35)
                + (thickness_relative_difference * 0.25)
            )

            # Create compatibility labels
            if compatibility_measure <= 0.035:
                compatibility = "High"

            elif compatibility_measure <= 0.075:
                compatibility = "Medium"

            else:
                compatibility = "Low"

            training_records.append({
                "Patient_Length": patient_length,
                "Patient_Width": patient_width,
                "Patient_Thickness": patient_thickness,

                "Donor_Length": donor_length,
                "Donor_Width": donor_width,
                "Donor_Thickness": donor_thickness,

                "Length_Difference": length_difference,
                "Width_Difference": width_difference,
                "Thickness_Difference": thickness_difference,

                "Length_Relative_Difference":
                    length_relative_difference,

                "Width_Relative_Difference":
                    width_relative_difference,

                "Thickness_Relative_Difference":
                    thickness_relative_difference,

                "Compatibility": compatibility
            })

        return pd.DataFrame(training_records)

    def save_training_data(self, output_file=None):
        """Generate and save the ML training dataset."""

        if output_file is None:
            output_file = os.path.join(
                os.path.dirname(__file__),
                "knee_ml_dataset.csv"
            )

        dataset = self.generate_training_data()

        dataset.to_csv(
            output_file,
            index=False
        )

        return dataset
    
if __name__ == "__main__":

    preprocessor = KneeDataPreprocessor()

    dataset = preprocessor.save_training_data()

    print("ML dataset generated successfully.")
    print(f"Number of records: {len(dataset)}")
    print("\nCompatibility distribution:")
    print(dataset["Compatibility"].value_counts())

    print("\nFirst 5 records:")
    print(dataset.head())