# 🦅 Rando-AI: Your Custom Hiking Assistant

**Rando-AI** is a lightweight demo of a Retrieval-Augmented Generation (RAG) system powered by OpenAI.

You can ask personalized hiking questions like:

> _“What’s a good summer hike in Auvergne with great views and moderate difficulty?”_

And get smart recommendations from a custom assistant powered by a manifest file.

---

## 🚀 Features

- 🔍 Retrieval-Augmented Generation (RAG) using your own `randos.json` dataset  
- 💬 Customizable assistant personalities via `manifest.json`  
- 🧠 Uses OpenAI GPT model (e.g., `gpt-3.5-turbo`)  
- ⚙️ Command-line interface for easy testing  

---

## 🗂️ Project Structure

```plaintext
.
├── data/
│   └── randos.json              # Hiking data used as knowledge base
├── manifests/
│   ├── coach_expert.json        # Expert coach personality
│   └── ...                      # Add more assistants here
├── retriever.py                 # Retrieves top hiking matches
├── main.py                      # Entry point
└── README.md

```
## 🧪 How to Use

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

## 2. 🧭 Choose Your Assistant

When you launch the app, you'll be prompted to choose one of the assistant profiles defined in the `manifests/` folder.

Each assistant is described in its own `manifest.json` file and can have a different personality, tone, and behavior depending on your use case.

For example, you could define:
- A **friendly coach** assistant (`coach_friendly.json`)
- A **serious expert** assistant (`coach_expert.json`)
- A **fun hiking buddy** (`buddy_chill.json`)

### 🛠️ How to launch

To start the assistant selection process and begin chatting:

```bash
python main.py
```

## 3. ➕ Add a New Assistant

You can create custom assistants with unique personalities, tones, and specialties by simply adding new manifest files in the `manifests/` folder.

Each assistant is defined in a separate `.json` file, following a standardized structure.

### 🧩 File location

All assistant configurations should be placed inside the `manifests/` directory:

```plaintext
.
├── manifests/
│   └── coach_expert.json
│   └── guide_zen.json
│   └── pote_aventure.json
```

### 📝 Sample `manifest.json` structure

Here’s a basic example of what a manifest file might look like:

```json
{
  "name": "Coach Friendly",
  "description": "A friendly and motivating assistant who encourages you during your hikes.",
  "personality": "warm, enthusiastic, supportive",
  "tone": "casual",
  "prompt_prefix": "You're a supportive and energetic hiking coach. Always cheer up the user, encourage physical activity, and provide helpful hiking tips.",
  "example_phrases": [
    "You're doing amazing!",
    "Keep it up, champ!",
    "Let me find a great hike for you today!"
  ]
}
```

## 🧠 How it works

When `main.py` is launched, all files inside the `manifests/` directory with a `.json` extension are automatically loaded and listed.

You can choose the assistant you want to use by selecting it from the prompt at runtime.

Each assistant’s settings (`name`, `tone`, `prompt style`, etc.) will shape how it responds to your questions.

---

## ⚙️ Technical Overview

### `main.py`

- Entry point of the application.
- Loads assistant configurations from the `manifests/` folder.
- Prompts the user to select an assistant to use.
- Uses the assistant's settings and invokes the retriever to get relevant context.
- Sends both the user question and retrieved context to OpenAI’s GPT API.
- Displays the generated response.

### `retriever.py`

- Implements the **retrieval** component of the RAG pipeline.
- Searches the `randos.json` dataset for hiking entries matching the user’s query.
- Uses simple keyword and attribute-based matching (region, difficulty, tags, etc.).
- Returns the best matching entries as a string that will be used as **context** in the GPT prompt.

---

## 🔍 Retrieval-Augmented Generation (RAG)

This project uses a lightweight **RAG approach**:

1. **Retrieval**:
   - When the user asks a question, `retriever.py` searches the local `randos.json` file for the most relevant hiking data.
   - The search returns a set of hike descriptions that are relevant to the query.

2. **Augmented Generation**:
   - The retrieved hike data is prepended to the GPT prompt as **context**.
   - This allows the assistant to answer questions more accurately by grounding responses in real, structured data.
   - The context acts as a knowledge base for GPT, without needing fine-tuning for every new dataset.

>💡 This approach makes it easy to update or expand the dataset (`randos.json`) without retraining the model.

---

## ✅ Tips for Creating Effective Assistants

- Be specific with the `system_prompt`. It defines the assistant’s behavior and expertise.
- Use natural tone descriptions like `"casual"`, `"professional"`, `"playful"`, or `"serious"`.
- Add several `"example_phrases"` to enrich the assistant’s responses and make them feel more alive.
- Give each assistant a distinct name and personality to help users quickly understand what to expect.

>💡 You can test new assistants instantly — no need to restart the app. Just save your `.json` file in `manifests/`, then run `python main.py` again.

---

### 💬 Example Query

```text
You: I'm looking for an easy summer hike in Auvergne with scenic views. What do you suggest?
The assistant will search relevant hikes and generate a helpful response using your randos.json.
```

### 📚 Credits

Built by Justin Thibault as part of an AI prototyping demo using fine-tuning of a language model.

This project uses OpenAI’s GPT API combined with a custom retriever engine to provide relevant, natural-language answers based on structured hiking data.
