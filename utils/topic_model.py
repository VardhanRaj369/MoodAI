from keybert import KeyBERT
import re
import nltk
from nltk.stem import PorterStemmer

kw_model = KeyBERT()
ps = PorterStemmer()

def extract_topics(text, n=3):
    """
    Extract clean, root-word topics to ensure accurate matching.
    Converts all words to their stem form (study → studi, exams → exam).
    """

    # Step 1: Get raw keyword phrases from KeyBERT
    raw_keywords = kw_model.extract_keywords(text, top_n=n)
    cleaned_topics = []

    for word, score in raw_keywords:

        # Step 2: Remove punctuation, numbers, symbols
        cleaned = re.sub(r"[^a-zA-Z\s]", " ", word)

        # Step 3: Lowercase
        cleaned = cleaned.lower()

        # Step 4: Handle multi-word topics ("exam fear" → ["exam", "fear"])
        parts = cleaned.split()

        for p in parts:

            # Step 5: Remove very short words like "to", "on"
            if len(p) < 3:
                continue

            # Step 6: Convert to root word (stemming)
            root = ps.stem(p)

            cleaned_topics.append(root)

    # Step 7: Keep unique topics and return only top 5
    cleaned_topics = list(set(cleaned_topics))

    return cleaned_topics[:5]
