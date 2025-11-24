import streamlit as st
import pandas as pd
import os
from utils.emotion_model import get_emotion
from utils.topic_model import extract_topics
from utils.suggestions import generate_suggestions
from wordcloud import WordCloud
import plotly.express as px

DATA_PATH = "data/journal_entries.csv"

# Create CSV if not exists
if not os.path.exists(DATA_PATH):
    df = pd.DataFrame(columns=["date", "text", "emotion", "confidence", "topics"])
    df.to_csv(DATA_PATH, index=False)


def save_entry(text, emotion, confidence, topics):
    df = pd.read_csv(DATA_PATH)
    new_row = {
        "date": pd.Timestamp.now().strftime("%Y-%m-%d"),
        "text": text,
        "emotion": emotion,
        "confidence": round(confidence, 2),
        "topics": ", ".join(topics)
    }
    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    df.to_csv(DATA_PATH, index=False)



st.title("🧠 AI Emotional Support Journal")


tab1, tab2 = st.tabs(["📘 Write Journal", "📊 Emotional Dashboard"])

# --------------- TAB 1 (JOURNAL ENTRY) ---------------
with tab1:
    st.header("Write Your Journal Entry")
    text = st.text_area("How are you feeling today? Write freely...", height=200)

    if st.button("Analyze Mood"):
        if text.strip() == "":
            st.warning("Please write something first.")
        else:
            emotion, confidence, secondary, reasoning = get_emotion(text)
            topics = extract_topics(text)
            suggestions = generate_suggestions(emotion, topics)

            save_entry(text, emotion, confidence, topics)

            st.subheader(f"Primary Emotion: {emotion} ({confidence:.2f})")
            st.write(f"Secondary Emotion: {secondary}")
            st.write("Reasoning:")
            st.write(reasoning)

            st.write("**Topics detected:**", topics)
            st.write("### Suggested Advice:")
            for s in suggestions:
                st.markdown(f"- {s}")


# -------------- TAB 2 (DASHBOARD) ---------------
with tab2:
    st.header("Emotional Journey Dashboard")

    df = pd.read_csv(DATA_PATH)

    if len(df) == 0:
        st.info("No entries yet. Start writing your journal!")
    else:
        # Emotion Over Time
        fig = px.line(df, x="date", y="emotion", title="Emotion Over Time")
        st.plotly_chart(fig)

        # Emotion distribution
        fig2 = px.pie(df, names="emotion", title="Emotion Breakdown")
        st.plotly_chart(fig2)

        # Word Cloud
        words = " ".join(df["text"].tolist())
        wc = WordCloud(width=600, height=400, background_color="white").generate(words)
        st.image(wc.to_array(), caption="Your Word Cloud")

