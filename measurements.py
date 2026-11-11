class KneeMeasurement:

    def __init__(
        self,
        knee_width,
        knee_depth,
        meniscus_length,
        meniscus_width,
        meniscus_thickness
    ):
        self.knee_width = knee_width
        self.knee_depth = knee_depth
        self.meniscus_length = meniscus_length
        self.meniscus_width = meniscus_width
        self.meniscus_thickness = meniscus_thickness

    def get_measurements(self):
        return {
            "Knee Width": self.knee_width,
            "Knee Depth": self.knee_depth,
            "Meniscus Length": self.meniscus_length,
            "Meniscus Width": self.meniscus_width,
            "Meniscus Thickness": self.meniscus_thickness
        }