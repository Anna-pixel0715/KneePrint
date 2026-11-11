import os
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report
)

import joblib


class KneeMLTrainer:

    def __init__(self, dataset_file=None):

        if dataset_file is None:
            dataset_file = os.path.join(
                os.path.dirname(__file__),
                "knee_ml_dataset.csv"
            )

        self.dataset_file = dataset_file
        self.model = None

    def load_dataset(self):
        """Load the generated ML dataset."""

        return pd.read_csv(self.dataset_file)

    def prepare_data(self):

        dataset = self.load_dataset()

        feature_columns = [
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

        X = dataset[feature_columns]
        y = dataset["Compatibility"]

        return X, y

    def train_model(self):

        X, y = self.prepare_data()

        X_train, X_test, y_train, y_test = train_test_split(
            X,
            y,
            test_size=0.20,
            random_state=42,
            stratify=y
        )

        self.model = RandomForestClassifier(
            n_estimators=150,
            max_depth=10,
            random_state=42
        )

        self.model.fit(X_train, y_train)

        predictions = self.model.predict(X_test)

        accuracy = accuracy_score(
            y_test,
            predictions
        )

        precision = precision_score(
            y_test,
            predictions,
            average="weighted",
            zero_division=0
        )

        recall = recall_score(
            y_test,
            predictions,
            average="weighted",
            zero_division=0
        )

        f1 = f1_score(
            y_test,
            predictions,
            average="weighted",
            zero_division=0
        )

        matrix = confusion_matrix(
            y_test,
            predictions
        )

        print("\n========================================")
        print("       KNEEPRINT ML MODEL TRAINING")
        print("========================================")

        print(f"\nTotal dataset records : {len(X)}")
        print(f"Training records      : {len(X_train)}")
        print(f"Testing records       : {len(X_test)}")

        print("\nAlgorithm:")
        print("Random Forest Classifier")

        print("\n----------------------------------------")
        print("MODEL PERFORMANCE")
        print("----------------------------------------")

        print(f"Accuracy  : {accuracy:.4f}")
        print(f"Precision : {precision:.4f}")
        print(f"Recall    : {recall:.4f}")
        print(f"F1 Score  : {f1:.4f}")

        print("\n----------------------------------------")
        print("CONFUSION MATRIX")
        print("----------------------------------------")

        print(matrix)

        print("\n----------------------------------------")
        print("CLASSIFICATION REPORT")
        print("----------------------------------------")

        print(
            classification_report(
                y_test,
                predictions,
                zero_division=0
            )
        )

        self.display_feature_importance(
            X.columns
        )

        return self.model

    def display_feature_importance(self, feature_names):

        print("\n----------------------------------------")
        print("FEATURE IMPORTANCE")
        print("----------------------------------------")

        importance_data = []

        for feature, importance in zip(
            feature_names,
            self.model.feature_importances_
        ):
            importance_data.append(
                (feature, importance)
            )

        importance_data.sort(
            key=lambda x: x[1],
            reverse=True
        )

        for feature, importance in importance_data:
            print(
                f"{feature:<35} "
                f"{importance:.4f}"
            )

    def save_model(self, output_file=None):

        if self.model is None:
            raise ValueError(
                "Model has not been trained yet."
            )

        if output_file is None:
            output_file = os.path.join(
                os.path.dirname(__file__),
                "kneeprint_random_forest.pkl"
            )

        joblib.dump(
            self.model,
            output_file
        )

        print(
            f"\nModel saved successfully:"
            f"\n{output_file}"
        )


if __name__ == "__main__":

    trainer = KneeMLTrainer()

    trainer.train_model()

    trainer.save_model()

    print("\n========================================")
    print("       TRAINING COMPLETED")
    print("========================================")