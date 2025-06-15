from faker import Faker
import json
import random

faker = Faker(["cs_CZ", "sk_SK"])

regions = [
    "Bratislavský", "Trnavský", "Nitriansky", "Žilinský", "Banskobystrický",
    "Prešovský", "Košický", "Praha", "Středočeský", "Jihomoravský",
    "Moravskoslezský", "Plzeňský", "Olomoucký", "Královéhradecký"
]

opening_hours_templates = [
    "Po-Pi 9:00-17:00", "Po-Št 8:00-18:00", "Po-Pá 10:00-16:00", "Po, St, Pi 9:00-15:00"
]

libraries = []

for i in range(1, 51):
    lib = {
        "id": i,
        "name": f"Knižnica {faker.city()}",
        "address": {
            "street": faker.street_address(),
            "zipCode": faker.postcode(),
            "city": faker.city(),
            "region": random.choice(regions),
            "country": faker.current_country()
        },
        "location": {
            "lat": float(faker.latitude()),
            "lon": float(faker.longitude())
        },
        "opening_hours": {
            "cs": random.choice(opening_hours_templates)
        }
    }
    libraries.append(lib)

# Zapíš do JSON
with open("fake_golemio_data.json", "w", encoding="utf-8") as f:
    json.dump({"data": libraries}, f, indent=2, ensure_ascii=False)

print("✅ JSON dátový súbor vytvorený → fake_golemio_data.json")
