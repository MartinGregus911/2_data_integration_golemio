import requests
import time

API_TOKEN = "PASTE_YOUR_API_TOKEN_HERE"

headers = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Accept": "application/json; charset=utf-8"
}

checked = 0
success = 0
fail = 0

for id in range(1, 50):
    url = f"https://api.golemio.cz/v2/municipallibraries/{id}"
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        print(f"✅ OK: ID {id}")
        success += 1
    else:
        print(f"⛔️ {id}: {response.status_code}")
        fail += 1

    checked += 1
    time.sleep(0.2)

print(f"\n🧾 Skontrolovaných: {checked}, Úspešných: {success}, Zlyhaní: {fail}")
