class BilateralComparison:

    def __init__(self, left_knee, right_knee):
        self.left_knee = left_knee
        self.right_knee = right_knee

    def compare(self):

        results = {
            "Knee Width Difference":
                abs(self.left_knee.knee_width -
                    self.right_knee.knee_width),

            "Knee Depth Difference":
                abs(self.left_knee.knee_depth -
                    self.right_knee.knee_depth),

            "Meniscus Length Difference":
                abs(self.left_knee.meniscus_length -
                    self.right_knee.meniscus_length),

            "Meniscus Width Difference":
                abs(self.left_knee.meniscus_width -
                    self.right_knee.meniscus_width),

            "Meniscus Thickness Difference":
                abs(self.left_knee.meniscus_thickness -
                    self.right_knee.meniscus_thickness)
        }

        return results

    def display_comparison(self):

        results = self.compare()

        print("\n===================================")
        print("      BILATERAL KNEE COMPARISON")
        print("===================================")

        for key, value in results.items():
            print(f"{key}: {value} mm")