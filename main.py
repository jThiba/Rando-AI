import os
import json
import openai
from retriever import Retriever

from openai import OpenAI

client = OpenAI()

def list_manifests(manifests_dir="manifests"):
    files = [f for f in os.listdir(manifests_dir) if f.endswith(".json")]
    return [os.path.splitext(f)[0] for f in files]

def load_manifest(name, manifests_dir="manifests"):
    path = os.path.join(manifests_dir, f"{name}.json")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def select_assistant():
    assistants = list_manifests()
    print("Quel assistant veux-tu utiliser ?\n")
    for i, name in enumerate(assistants):
        print(f"{i + 1}. {name}")
    choice = int(input("\nEntre le numéro de l'assistant : ")) - 1
    return assistants[choice]

def main():
    assistant_name = select_assistant()
    manifest = load_manifest(assistant_name)
    print(f"\n✅ Assistant activé : {manifest['name']}")
    print("Tape 'exit' pour quitter\n")

    retriever = None
    if "retriever" in manifest:
        retriever_config = manifest["retriever"]
        if retriever_config["type"] == "json":
            retriever = Retriever(retriever_config["data_path"])

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break

        context = ""
        if retriever:
            context = retriever.retrieve_context(user_input)

        messages = [
            {"role": "system", "content": manifest["system_prompt"]},
        ]
        if context:
            messages.append({"role": "system", "content": f"Contexte pour la réponse :\n{context}"})
        messages.append({"role": "user", "content": user_input})

        response = client.chat.completions.create(
            model=manifest["model"],
            messages=messages
        )
        print(f"\nAssistant: {response.choices[0].message.content}\n")

if __name__ == "__main__":
    main()
