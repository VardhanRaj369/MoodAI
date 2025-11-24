def generate_suggestions(emotion, topics):
    emotion = emotion.lower()
    topics = [t.lower() for t in topics] if topics else []

    # -------------------------
    # EMOTION-BASED ADVICE
    # -------------------------
    emotion_advice = {
        "admiration": ["Reflect on what inspired you and how you can grow from it."],
        "amusement": ["Laughter is healing. Enjoy the lightness of this moment!"],
        "approval": ["Notice what aligned well with your values today."],
        "caring": ["Your compassion is valuable. Remember to care for yourself too."],
        "desire": ["Think about the first small step to move toward what you want."],
        "excitement": ["Channel this positive energy into something meaningful."],
        "gratitude": ["Write down three things you're grateful for."],
        "joy": ["Enjoy this moment fully — happiness is worth celebrating!"],
        "love": ["Express your love or appreciation to someone close."],
        "optimism": ["Use this mindset to plan something productive."],
        "pride": ["Appreciate your effort — you earned this!"],
        "relief": ["Take a breath and recognize what eased your mind."],
        "anger": ["Pause, breathe, and respond calmly instead of reacting instantly."],
        "annoyance": ["A short break might help reset your mood."],
        "confusion": ["Break things down into smaller pieces. Clarity will come."],
        "disappointment": ["It’s okay to feel let down. Focus on what you learned."],
        "disapproval": ["Reflect on what didn’t align with your values today."],
        "disgust": ["Distance yourself from the source and regain emotional balance."],
        "embarrassment": ["Remember: everyone makes mistakes. Be kind to yourself."],
        "fear": ["A slow deep breath can help your mind feel safer and grounded."],
        "grief": ["Healing takes time. Reach out if you need comfort."],
        "nervousness": ["Steady breathing and preparation can reduce your anxiety."],
        "remorse": ["Acknowledge your feelings gently, and make amends where possible."],
        "sadness": ["Give yourself rest. Talking to someone can ease the weight."],
        "curiosity": ["Explore what sparked your interest — it may lead somewhere new."],
        "realization": ["Reflect on how this insight could help guide your next steps."],
        "surprise": ["Unexpected moments can bring growth. Reflect on why this surprised you."],
        "neutral": ["A calm state is a good time to reflect on your goals."]
    }

    # -------------------------
    # TOPIC-BASED ADVICE
    # -------------------------
    topic_advice = []

    if any(t in topics for t in ["exam", "study", "test"]):
        topic_advice.append("Break your study into small sessions — your mind absorbs better that way.")
        topic_advice.append("Practice past papers to build confidence.")

    if any(t in topics for t in ["work", "office", "job", "career"]):
        topic_advice.append("Prioritize your tasks — not everything needs to be done at once.")
        topic_advice.append("Take a short walk to refresh your mind if stress builds up.")

    if any(t in topics for t in ["relationship", "partner", "love"]):
        topic_advice.append("Honest communication can clear many misunderstandings.")
        topic_advice.append("Reflect on what you truly need emotionally right now.")

    if any(t in topics for t in ["friends", "friendship"]):
        topic_advice.append("Reach out to a friend — even a small conversation can help.")
        topic_advice.append("Think of someone who made your day better.")

    if any(t in topics for t in ["family", "parents", "home"]):
        topic_advice.append("Family relationships can be complex — patience helps.")
        topic_advice.append("Try to express your feelings gently and clearly.")

    if any(t in topics for t in ["health", "illness", "sick", "pain"]):
        topic_advice.append("Listen to your body — rest is not a weakness.")
        topic_advice.append("If symptoms persist, consider speaking with a professional.")

    if any(t in topics for t in ["money", "finance", "salary"]):
        topic_advice.append("List your expenses to regain a sense of control.")
        topic_advice.append("Financial stress is common — take one step at a time.")

    if any(t in topics for t in ["school", "college", "class"]):
        topic_advice.append("Stay consistent — progress compounds over time.")
        topic_advice.append("Ask for help when you need it. You don’t have to do everything alone.")

    if any(t in topics for t in ["fear", "danger", "threat"]):
        topic_advice.append("Ground yourself: look around and remind yourself you are safe now.")

    # -------------------------
    # FINAL RECOMMENDATION COMBINATION
    # -------------------------
    final_suggestions = emotion_advice.get(emotion, [])

    # add topic-based advice
    final_suggestions.extend(topic_advice)

    # fallback if everything empty
    if not final_suggestions:
        final_suggestions = ["Take a moment to reflect on your feelings today."]

    return final_suggestions
