🌟 MoodAI – AI-Powered Emotional Journal & Mood Analyzer

MoodAI is an intelligent emotional journaling application built using advanced NLP.
It understands your feelings, detects topics from your journal entries, provides personalized suggestions, and visualizes your emotional journey over time.

Powered by the GoEmotions transformer model, KeyBERT topic extraction, and a custom suggestion engine, MoodAI helps users reflect, process emotions, and gain self-insight.

🚀 Features
🧠 28-Emotion Detection (GoEmotions Model)

Uses SamLowe/roberta-base-go_emotions

Identifies 28 human emotions like: admiration, amusement, anger, fear, joy, sadness, nervousness, realization, optimism, frustration, etc.

More accurate and expressive than basic sentiment analysis.

🔍 Topic Extraction

Extracts key topics using KeyBERT

Helps understand what the journal entry is about

Used to generate topic-specific suggestions

💡 Personalized Suggestions

Custom rule-based engine combines emotion + topic

Gives meaningful guidance based on your feelings and writing context

Example:

Emotion: nervousness + Topic: exam → study tips

Emotion: fear + Topic: dog → grounding techniques

📊 Emotional Dashboard

Line chart: Mood over time

Pie chart: Emotion distribution

WordCloud: Most common themes

Helps track emotional patterns and personal growth

📁 Local Storage

Journal entries stored in data/journal_entries.csv

Works offline, no database needed

Perfect for local use or cloning the repo

🎨 Streamlit UI

Clean, modern, user-friendly interface

Two main tabs:

Write Journal

Emotional Dashboard

🧰 Tech Stack

| Component          | Technology                       |
| ------------------ | -------------------------------- |
| UI                 | Streamlit                        |
| Emotion Model      | RoBERTa GoEmotions Transformer   |
| Topic Extraction   | KeyBERT (MiniLM/BERT embeddings) |
| Suggestions Engine | Custom Python Rule-Based System  |
| Visualizations     | Plotly, WordCloud                |
| Storage            | CSV + Pandas                     |
| Environment        | Python 3.9+                      |

📦 Installation
1️⃣ Clone the repository
git clone https://github.com/your-username/MoodAI.git
cd MoodAI
2️⃣ Install Dependencies
pip install -r requirements.txt
3️⃣ Run the App
streamlit run app.py

📁 Project Structure

MoodAI/
│
├── app.py                         # Streamlit main app
├── requirements.txt               # Dependencies
│
├── data/
│   └── journal_entries.csv        # Local storage of entries
│
├── utils/
│   ├── emotion_model.py           # 28-emotion GoEmotions model
│   ├── topic_model.py             # Keyword/topic extraction
│   └── suggestions.py             # Emotion + Topic suggestion engine
│
└── README.md                      # Project documentation


🧠 How It Works (Conceptual Flow)

User writes a journal entry

Emotion Detection (GoEmotions)

Model predicts one of 28 emotions

Topic Extraction (KeyBERT)

Finds meaningful keywords

Suggestion Engine

Combines emotion + topic

Generates personalized advice

Save Entry

Stores date, text, emotion, topics, and confidence

Dashboard

Tracks emotional patterns over time

📊 Visual Insights

MoodAI provides:

✔ Emotional Timeline

See how your mood changes across days.

✔ Emotion Distribution

Understand how often you feel certain emotions.

✔ Word Cloud

Visualize the most common words from your journal.

🤝 Contributing
Pull requests and feature suggestions are welcome!

💬 Author
Emmadi Leelavardhan Raj
AI & Software Engineer | NLP Projects | Machine Learning Enthusiast
