🧠 AI Emotional General
An AI-powered emotional analysis app built with Streamlit

AI Emotional General is an interactive web application that analyzes user-submitted text to detect emotions, sentiment, context, entities, and then provides personalized well-being suggestions.

The system uses HuggingFace Transformers, TextBlob, and custom logic to understand feelings expressed in natural language. It includes a complete fallback mode, ensuring the app works even when deep-learning models fail to load.
(Full logic implemented in EmotionAnalyzer class → emotion_model)

🚀 Features
✅ Emotion Analysis

Primary emotion detection

Confidence score

Full emotion distribution

Emotional intensity score
(Implemented in analyze_emotion() → emotion_model)

🎯 Context Extraction

Topic extraction using TextBlob noun phrases

Sentiment classification (Transformer or fallback)

Entity extraction (names & places)
(Implemented in extract_context() → emotion_model)

💡 Personalized Suggestions

Tailored advice for each emotion

Intensity-based guidance

Sentiment-based recommendations
(Implemented in get_suggestions() → emotion_model)

📊 Beautiful Visualizations

Emotion bar charts (Plotly)

Sentiment gauge

Radar chart for emotional profile
(Generated in display_* functions → app)

🧱 Fallback Mode (Offline / Error-proof)

If transformer models fail to load (network, device errors):

Uses keyword-based emotion detection

Uses TextBlob sentiment

Simplifies emotion scoring
(Fallback implemented in analyze_emotion_fallback() → emotion_model)

🧰 Tech Stack
| Category                 | Technologies / Tools                                                                                                       |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------------- |
| **Frontend**             | Streamlit, Custom CSS, Plotly (Charts & Visualizations)                                                                    |
| **Backend / Core Logic** | Python 3, HuggingFace Transformers, PyTorch, TextBlob, Regex                                                               |
| **ML Models Used**       | `j-hartmann/emotion-english-distilroberta-base` (Emotion Model), HuggingFace Sentiment Pipeline, Rule-based Fallback Model |
| **NLP Processing**       | TextBlob Noun Phrase Extraction, Regex-based Entity Extraction                                                             |
| **Data Processing**      | NumPy, Pandas                                                                                                              |
| **Visualizations**       | Plotly Express, Plotly Graph Objects                                                                                       |
| **Deployment**           | Streamlit Cloud, GitHub                                                                                                    |
| **Environment**          | Requirements from `requirements.txt` (Streamlit, Transformers, Torch, Pandas, TextBlob, Plotly, Scikit-learn)              |

📁 Project Structure
/
├── app.py                # Streamlit UI & main app logic
├── emotion_model.py      # Core emotion + context analysis module
├── requirements.txt      # Python dependencies
└── README.md             # Documentation

🧠 How It Works (Technical Overview)
1. Model Loading

EmotionAnalyzer.load_models() attempts to load:

Emotion classification model
"j-hartmann/emotion-english-distilroberta-base"

HuggingFace sentiment-analysis pipeline

If loading fails → fallback mode activates.
(Logic in → emotion_model)

2. Emotion Detection

If models are loaded:

Transformer probabilities determine:

Primary emotion

Emotion distribution

Emotional intensity

Fallback method uses:

TextBlob polarity

Keyword matching
(Logic: analyze_emotion() & fallback → emotion_model)

3. Context Extraction

Extracts:

Noun-phrase topics

Sentiment (model/TextBlob)

Named entities (via regex)

(Logic: extract_context() → emotion_model)

4. Personalized Suggestions

Generated using:

Primary emotion

Emotion intensity

Sentiment polarity

(Logic: get_suggestions() → emotion_model)

🖥️ User Interface (Streamlit)

The UI includes:

✔️ Text input
✔️ Example prompts
✔️ Loading spinners
✔️ Custom CSS design
✔️ Four analysis tabs:

Emotional Analysis

Context

Suggestions

Visualization

(Complete UI in app.py → app)

🧪 Example Inputs

Try entering:

“I'm really anxious about my exam tomorrow.”

“I feel proud of myself today, everything went great!”

“I’m frustrated because nobody listens to me.”

The app will:

Detect your emotion

Show the confidence

Extract topics

Provide helpful, personalized suggestions

🛡️ Error Handling

The app features:

✔ Model load errors
✔ Fallback mode warning
✔ Input validation
✔ Try/except blocks around analysis
✔ UI notifications for users
(All implemented in app.py → app)

