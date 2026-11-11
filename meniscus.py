class MeniscusAnalysis:

    def __init__(self, affected_knee, left_knee, right_knee):
        self.affected_knee = affected_knee
        self.left_knee = left_knee
        self.right_knee = right_knee

    def get_affected_measurement(self):

        if self.affected_knee.lower() == "left":
            return self.left_knee

        elif self.affected_knee.lower() == "right":
            return self.right_knee

        else:
            return None

    def analyze(self):

        knee = self.get_affected_measurement()

        if knee is None:
            return None

        return {
            "Meniscus Length": knee.meniscus_length,
            "Meniscus Width": knee.meniscus_width,
            "Meniscus Thickness": knee.meniscus_thickness
        }

    def display_analysis(self):

        results = self.analyze()

        print("\n===================================")
        print("          MENISCUS ANALYSIS")
        print("===================================")

        if results is None:
            print("Invalid affected knee.")
            return

        print(f"Affected Knee: {self.affected_knee}")

        print("-----------------------------------")

        for key, value in results.items():
            print(f"{key}: {value} mm")