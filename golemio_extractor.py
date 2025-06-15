import json
import csv

# 1. Načítanie falošných dát zo súboru
with open("fake_golemio_data.json", encoding="utf-8") as f:
    data = json.load(f)

libraries = data.get("data", [])

# 2. Zápis do CSV
with open("golemio_libraries.csv", mode="w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([
        "id", "name", "street", "zip", "city",
        "region", "country", "latitude", "longitude", "opening_hours"
    ])

    for lib in libraries:
        writer.writerow([
            lib.get("id"),
            lib.get("name"),
            lib.get("address", {}).get("street"),
            lib.get("address", {}).get("zipCode"),
            lib.get("address", {}).get("city"),
            lib.get("address", {}).get("region"),
            lib.get("address", {}).get("country"),
            lib.get("location", {}).get("lat"),
            lib.get("location", {}).get("lon"),
            lib.get("opening_hours", {}).get("cs")
        ])

print(f"✅ Hotovo: {len(libraries)} knižníc uložených do golemio_libraries.csv")
