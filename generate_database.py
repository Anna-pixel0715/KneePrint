import csv
import random


with open("donor_database.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow([
        "Donor_ID",
        "Side",
        "Meniscus_Type",
        "Length_mm",
        "Width_mm",
        "Thickness_mm"
    ])

    for i in range(1, 101):

        donor_id = f"D{i:03d}"

        side = random.choice(["Left", "Right"])

        meniscus_type = random.choice([
            "Medial",
            "Lateral"
        ])

        length = round(random.uniform(39.0, 44.5), 1)
        width = round(random.uniform(26.0, 30.5), 1)
        thickness = round(random.uniform(7.3, 8.6), 1)

        writer.writerow([
            donor_id,
            side,
            meniscus_type,
            length,
            width,
            thickness
        ])

print("100 donor records created successfully!")
