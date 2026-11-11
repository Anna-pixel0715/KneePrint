import os
import joblib


class ExplainableAnalyzer:

    def __init__(self, model_file=None):

        if model_file is None:
            model_file = os.path.join(
                os.path.dirname(__file__),
                "kneeprint_random_forest.pkl"
            )

        self.model_file = model_file
        self.model = joblib.load(self.model_file)

        self.feature_names = [
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

    def get_feature_importance(self):

        importances = self.model.feature_importances_

        feature_importance = []

        for feature, importance in zip(
            self.feature_names,
            importances
        ):
            feature_importance.append({
                "Feature": feature,
                "Importance": float(importance)
            })

        feature_importance.sort(
            key=lambda x: x["Importance"],
            reverse=True
        )

        return feature_importance

    def get_top_features(self, number_of_features=5):

        features = self.get_feature_importance()

        return features[:number_of_features]

    def display_explanation(self):

        top_features = self.get_top_features(5)

        print("\n========================================")
        print("       KNEEPRINT EXPLAINABLE ANALYSIS")
        print("========================================")

        print("\nTop factors learned by the model:")
        print("----------------------------------------")

        for rank, feature in enumerate(
            top_features,
            start=1
        ):

            print(
                f"{rank}. "
                f"{feature['Feature']}"
                f" → "
                f"{feature['Importance'] * 100:.2f}%"
            )

        print("\n----------------------------------------")
        print("INTERPRETATION")
        print("----------------------------------------")

        print(
            "\nThe Random Forest model considers "
            "multiple knee and donor measurements "
            "when predicting compatibility."
        )

        print(
            "\nFeature importance indicates which "
            "features contributed most to the "
            "model's learned decision patterns."
        )

        print(
            "\nThese values represent model behavior "
            "and should not be interpreted as "
            "clinical importance."
        )


if __name__ == "__main__":

    analyzer = ExplainableAnalyzer()

    analyzer.display_explanation()