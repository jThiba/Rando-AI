import requests
import json

# Définir l'URL de l'API Overpass
OVERPASS_URL = "http://overpass-api.de/api/interpreter"

# Requête pour récupérer les sentiers de randonnée en Auvergne
query = """
[out:json];
area[name="Auvergne"]->.searchArea;
(
  way["route"="hiking"](area.searchArea);
  relation["route"="hiking"](area.searchArea);
);
out body;
"""

# Envoyer la requête à Overpass API
response = requests.get(OVERPASS_URL, params={"data": query})

# Vérifier que la requête a réussi
if response.status_code == 200:
    data = response.json()
    
    # Sauvegarder les données en JSON
    with open("randonnées_auvergne.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    
    print("✅ Données de randonnée récupérées et sauvegardées !")
else:
    print("❌ Erreur lors de la requête:", response.status_code)
