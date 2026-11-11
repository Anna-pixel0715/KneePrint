class MeniscusMatcher:

    def __init__(self, patient_meniscus, donor_records):
        self.patient_meniscus = patient_meniscus
        self.donor_records = donor_records

    def calculate_score(self, donor):

        length_difference = abs(
            float(self.patient_meniscus["Meniscus Length"])
            - float(donor["Length_mm"])
        )

        width_difference = abs(
            float(self.patient_meniscus["Meniscus Width"])
            - float(donor["Width_mm"])
        )

        thickness_difference = abs(
            float(self.patient_meniscus["Meniscus Thickness"])
            - float(donor["Thickness_mm"])
        )

        score = (
            length_difference
            + width_difference
            + thickness_difference
        )

        return score

    def find_matches(self):

        matches = []

        for donor in self.donor_records:

            score = self.calculate_score(donor)

            matches.append({
                "Donor ID": donor["Donor_ID"],
                "Score": score
            })

        matches.sort(key=lambda x: x["Score"])

        return matches[:3]
