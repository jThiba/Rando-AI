import json

# Charger les randonnées structurées
with open("randonnées_auvergne_structurées.json", "r", encoding="utf-8") as f:
    randonnées = json.load(f)

def rechercher_randonnées(query, min_distance=0, max_distance=float("inf")):
    """Recherche des randonnées correspondant à un mot-clé et une distance"""
    résultats = []
    query = query.lower()
    
    for rando in randonnées:
        nom = rando["nom"].lower()
        distance = rando["distance_km"] or 0  # Gérer le cas où la distance est None

        if query in nom and min_distance <= distance <= max_distance:
            résultats.append(rando)

    return résultats

# Exemple d'utilisation
query = input("🔍 Entrez un mot-clé pour la randonnée : ")
min_dist = float(input("📏 Distance min (km) : ") or 0)
max_dist = float(input("📏 Distance max (km) : ") or float("inf"))

résultats = rechercher_randonnées(query, min_dist, max_dist)

# Affichage des résultats
if résultats:
    print(f"\n🏞️ {len(résultats)} randonnées trouvées :\n")
    for rando in résultats:
        print(f"- {rando['nom']} ({rando['distance_km']} km)")
else:
    print("❌ Aucune randonnée trouvée.")
