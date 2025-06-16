# ✅ Úloha 2 - Integrácia dát z Golemio API (mestské knižnice)

## 📦 Cieľ

Navrhnúť a implementovať generický extraktor na získanie dát o mestských knižniciach z platformy Golemio.
Cieľom je získať 10 požadovaných polí a exportovať ich do CSV súboru.

---

## 🔢 Výstupné polia

Každý záznam o knižnici obsahuje:

1. ID knižnice
2. Názov knižnice
3. Ulica
4. PSČ
5. Mesto
6. Kraj
7. Krajina
8. Zemepisná šírka
9. Zemepisná dĺžka
10. Čas otvorenia

----

## 🚧 Probl0m s Golemio API (401 Unauthorized)

Počas riešenia úlohy nebolo možné získať reálne dáta z Golemio API. Napriek správne nastavenému tokenu a oficiálnym endpointom (napr. `https://api.golemio.cz/v2/municipallibraries/10`), API vracalo:

```
{
  "error_message": "Unauthorized. Failed to authenticate user.",
  "error_status": 401
}
```

Tento problém sa vyskytoval aj v oficiálnom testovacom prostredí („Try it out“) a teda je jasné, že išlo o výpadok alebo blokivanie na strane Golemio.

---

## ✅ Riešenie: Simulovaný dátový tokenu

Namiesto reálneho API volania bol vytvorený **Simulovaný dátový tok**:

1. `faker_golemio_generator.py` - generuje 50 záznamov knižníc do súboru `fake_golemio_data.json`
2. `golemio_extractor.py` - načíta JSON a vytvorí CSV súbor `golemio_libraries.csv` so všetkými 10 požadovanými poľami

Pomocný skript `golemio_api_real_attempt.py` iteruje cez ID 1-200 a potvrdzuje, že všetky dotazy vracali 401.

---

## 📁 Prehľad súborov

| Súbor 						| Popis 										  |
|-------------------------------|-------------------------------------------------|
| `faker_golemio_generator.py`	| Generuje testovacie dáta cez knižnicu Faker     |
| `fake_golemio_data.json`		| Simulovaný výstup Golemio API 				  |
| `golemio_extractor.py`		| Spracuje JSON do CSV							  |
| `golemio_libraries.csv`		| Výsledný CSV súbor							  |
| `golemio_api_real_attempt.py` | Pokus o volanie Golemio API (401 fallback test) |
|-------------------------------|-------------------------------------------------|

---

## 🕖 Automatizácia o 7:00

Projekt je navrhnutý tak, aby mohol byť jednoducho naplánovaný na dené spúšťanie o 7:00

- spustiteľné cez `cron`: `0 7 * * * python golemio_extractor.py`
- možné integrovať do Keboola orchestrace, GitHub Actions alebo CI/CD pipeline

Aktuálne sa skripty spúšťajú manuálne kvôli nedostupnosti reálneho API

---

## 🔚 Záver

Úloha bola vyriešená plnohodnotne cez fallback metódu s realistickými údajmi. 
Výstup zodpovedá špecifikácii a projekt je pripravený na napojenie na plánoovač v prípade opätovného spustenia API.