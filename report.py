class AnalysisReport:

    def __init__(self, patient, comparison, meniscus, matches):
        self.patient = patient
        self.comparison = comparison
        self.meniscus = meniscus
        self.matches = matches

    def display_report(self):

        patient_details = self.patient.get_patient_details()
        comparison_results = self.comparison.compare()
        meniscus_results = self.meniscus.analyze()

        print("\n")
        print("=" * 50)
        print("             KNEEPRINT")
        print("        FINAL ANALYSIS REPORT")
        print("=" * 50)

        # Patient Information
        print("\nPATIENT INFORMATION")
        print("-" * 50)

        for key, value in patient_details.items():
            print(f"{key}: {value}")

        # Knee Comparison
        print("\nBILATERAL KNEE COMPARISON")
        print("-" * 50)

        for key, value in comparison_results.items():
            print(f"{key}: {value} mm")

        # Meniscus Analysis
        print("\nMENISCUS PROFILE")
        print("-" * 50)

        for key, value in meniscus_results.items():
            print(f"{key}: {value} mm")

        # Donor Matches
        print("\nCLOSEST DIMENSIONAL DONOR MATCHES")
        print("-" * 50)

        for index, match in enumerate(self.matches, start=1):
            print(
                f"{index}. {match['Donor ID']}"
                f"  |  Difference Score: {match['Score']:.2f}"
            )

        print("\n" + "-" * 50)
        print("Analysis completed successfully.")
        print("-" * 50)

        print("\nNOTE:")
        print("This is an educational software prototype.")
        print("The matching result is based only on the")
        print("dimensions included in the sample dataset.")
        print("It does not determine clinical transplant suitability.")

        print("=" * 50)