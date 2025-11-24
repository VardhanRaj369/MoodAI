from keybert import KeyBERT

kw_model = KeyBERT()

def extract_topics(text, n=3):
    """Extract top n keywords (topics) from journal entry."""
    keywords = kw_model.extract_keywords(text, top_n=n)
    return [word for word, score in keywords]
