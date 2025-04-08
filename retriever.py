import json
import difflib
import re

class Retriever:
    def __init__(self, json_path="data/randos.json"):
        with open(json_path, "r", encoding="utf-8") as f:
            self.rando_data = json.load(f)

    def preprocess(self, text):
        return re.sub(r"[^\w\s]", "", text.lower())

    def retrieve_context(self, query, max_results=3):
        query_clean = self.preprocess(query)

        scored = []
        for rando in self.rando_data:
            full_text = " ".join([
                str(rando.get("name", "")),
                str(rando.get("region", "")),
                str(rando.get("description", "")),
                str(rando.get("difficulty", "")),
                str(rando.get("distance", "")),
                str(rando.get("duration", "")),
                str(rando.get("start", "")),
                str(rando.get("end", ""))
            ])
            full_text_clean = self.preprocess(full_text)

            score = difflib.SequenceMatcher(None, query_clean, full_text_clean).ratio()
            scored.append((score, rando))

        scored.sort(reverse=True, key=lambda x: x[0])
        top_results = [r[1] for r in scored[:max_results]]

        context = "Voici quelques randonnées correspondant à ta demande :\n\n"
        for r in top_results:
            context += (
                f"🏞️ {r.get('name', 'Nom inconnu')} ({r.get('region', 'région inconnue')})\n"
                f"• Difficulté : {r.get('difficulty', 'non précisée')}\n"
                f"• Distance : {r.get('distance', '?')} km\n"
                f"• Durée : {r.get('duration', 'inconnue')}\n"
                f"• Dénivelé : {r.get('denivele_m', '?')} m\n"
                f"• Départ : {r.get('start', 'non précisé')}\n"
                f"• Arrivée : {r.get('end', 'non précisée')}\n"
                f"• Saison : {r.get('saison', 'non précisée')}\n"
                f"• Description : {r.get('description', 'Pas de description')}\n\n"
            )

        return context.strip()
