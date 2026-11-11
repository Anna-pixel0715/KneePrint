class KneePrint:

    def __init__(self, patient, left_knee, right_knee):
        self.patient = patient
        self.left_knee = left_knee
        self.right_knee = right_knee

    def generate_profile(self):
        return {
            "Patient": self.patient.get_patient_details(),
            "Left Knee": self.left_knee.get_measurements(),
            "Right Knee": self.right_knee.get_measurements()
        }

    def display_profile(self):

        profile = self.generate_profile()

        print("\n===================================")
        print("          KNEEPRINT PROFILE")
        print("===================================")

        print("\nPATIENT")
        print("-----------------------------------")

        for key, value in profile["Patient"].items():
            print(f"{key}: {value}")

        print("\nLEFT KNEE")
        print("-----------------------------------")

        for key, value in profile["Left Knee"].items():
            print(f"{key}: {value} mm")

        print("\nRIGHT KNEE")
        print("-----------------------------------")

        for key, value in profile["Right Knee"].items():
            print(f"{key}: {value} mm")