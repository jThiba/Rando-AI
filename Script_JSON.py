import json

# Charger les données récupérées
with open("randonnées_auvergne.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Extraire les randonnées utiles
randonnées_structurées = []

for element in data.get("elements", []):
    if "tags" in element:
        tags = element["tags"]
        
        # Récupérer le nom (on ignore si absent)
        nom = tags.get("name")
        if not nom:
            continue  # Passe à la randonnée suivante si pas de nom
        
        # Récupérer la distance (convertir en km si nécessaire)
        distance = tags.get("distance") or tags.get("length")
        if distance:
            try:
                distance = float(distance)
                if distance > 100:  # Si c'est en mètres, convertir en km
                    distance /= 1000
            except ValueError:
                distance = None  # Ignorer si ce n'est pas un nombre
        
        # Ajouter les informations extraites
        rando = {
            "nom": nom,
            "distance_km": distance,
            "difficulté": tags.get("difficulty", "Non spécifié"),
            "type_de_chemin": tags.get("highway", "Non spécifié"),
            "source": tags.get("source", "Non spécifié")
        }
        randonnées_structurées.append(rando)

# Sauvegarder les randonnées filtrées dans un fichier JSON propre
with open("randonnées_auvergne_structurées.json", "w", encoding="utf-8") as f:
    json.dump(randonnées_structurées, f, indent=4, ensure_ascii=False)

print("✅ Données filtrées et sauvegardées dans 'randonnées_auvergne_structurées.json' !")
