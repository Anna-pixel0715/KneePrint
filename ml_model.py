import os
import joblib
import pandas as pd


class KneeMLModel:

    def __init__(self, model_file=None):

        if model_file is None:
            model_file = os.path.join(
                os.path.dirname(__file__),
                "kneeprint_random_forest.pkl"
            )

        self.model_file = model_file
        self.model = None

        self.feature_columns = [
            "Patient_Length",
            "Patient_Width",
            "Patient_Thickness",

            "Donor_Length",
            "Donor_Width",
            "Donor_Thickness",

            "Length_Difference",
            "Width_Difference",
            "Thickness_Difference",

            "Length_Relative_Difference",
            "Width_Relative_Difference",
            "Thickness_Relative_Difference"
        ]

    def load_model(self):
        """Load the trained Random Forest model."""

        if not os.path.exists(self.model_file):
            raise FileNotFoundError(
                "Trained ML model was not found. "
                "Run train_model.py first."
            )

        self.model = joblib.load(self.model_file)

        return self.model

    def prepare_features(
        self,
        patient_length,
        patient_width,
        patient_thickness,
        donor_length,
        donor_width,
        donor_thickness
    ):
        """Create the same features used during training."""

        patient_length = float(patient_length)
        patient_width = float(patient_width)
        patient_thickness = float(patient_thickness)

        donor_length = float(donor_length)
        donor_width = float(donor_width)
        donor_thickness = float(donor_thickness)

        length_difference = abs(
            patient_length - donor_length
        )

        width_difference = abs(
            patient_width - donor_width
        )

        thickness_difference = abs(
            patient_thickness - donor_thickness
        )

        length_relative_difference = (
            length_difference / patient_length
        )

        width_relative_difference = (
            width_difference / patient_width
        )

        thickness_relative_difference = (
            thickness_difference / patient_thickness
        )

        features = {
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
                thickness_relative_difference
        }

        return pd.DataFrame(
            [features],
            columns=self.feature_columns
        )

    def predict_compatibility(
        self,
        patient_length,
        patient_width,
        patient_thickness,
        donor_length,
        donor_width,
        donor_thickness
    ):
        """Predict compatibility for one patient-donor pair."""

        if self.model is None:
            self.load_model()

        features = self.prepare_features(
            patient_length,
            patient_width,
            patient_thickness,
            donor_length,
            donor_width,
            donor_thickness
        )

        prediction = self.model.predict(features)[0]

        probabilities = self.model.predict_proba(features)[0]

        class_names = self.model.classes_

        probability_dict = {
            class_name: float(probability)
            for class_name, probability
            in zip(class_names, probabilities)
        }

        confidence = max(probability_dict.values())

        return {
            "Compatibility": prediction,
            "Confidence": confidence,
            "Probabilities": probability_dict
        }


if __name__ == "__main__":

    print("========================================")
    print("       KNEEPRINT ML MODEL TEST")
    print("========================================")

    model = KneeMLModel()

    # Example patient measurements
    patient_length = 42
    patient_width = 28
    patient_thickness = 8

    # Example donor measurements
    donor_length = 42.5
    donor_width = 28.4
    donor_thickness = 7.8

    result = model.predict_compatibility(
        patient_length,
        patient_width,
        patient_thickness,
        donor_length,
        donor_width,
        donor_thickness
    )

    print("\nPatient measurements:")
    print(f"Length: {patient_length} mm")
    print(f"Width: {patient_width} mm")
    print(f"Thickness: {patient_thickness} mm")

    print("\nDonor measurements:")
    print(f"Length: {donor_length} mm")
    print(f"Width: {donor_width} mm")
    print(f"Thickness: {donor_thickness} mm")

    print("\n----------------------------------------")
    print("ML PREDICTION")
    print("----------------------------------------")

    print(
        f"Compatibility: "
        f"{result['Compatibility']}"
    )

    print(
        f"Confidence: "
        f"{result['Confidence'] * 100:.2f}%"
    )

    print("\nClass probabilities:")

    for class_name, probability in result[
        "Probabilities"
    ].items():

        print(
            f"{class_name}: "
            f"{probability * 100:.2f}%"
        )

    print("\n========================================")
    print("          TEST COMPLETED")
    print("========================================")