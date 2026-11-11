import csv
import os


class DonorDatabase:

    def __init__(self, filename=None):

        if filename is None:
            filename = os.path.join(
                os.path.dirname(__file__),
                "donor_database.csv"
            )

        self.filename = filename
        self.donors = []

    def load_donors(self):

        self.donors = []

        with open(self.filename, "r", newline="") as file:

            reader = csv.DictReader(file)

            for row in reader:
                self.donors.append(row)

        return self.donors

    def get_donors(self):

        return self.donors