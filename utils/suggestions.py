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
    # TOPIC-BASED ADVICE (advanced matching)
    # -------------------------
    topic_advice = []

    def topic_match(*keywords):
        """Match stemmed topics using partial string matching."""
        return any(any(key in t for key in keywords) for t in topics)

    # STUDY / EXAM
    if topic_match("exam", "exams", "studi", "study", "test"):
        topic_advice.append("It's normal to feel anxious before exams — many people experience the same.")
        topic_advice.append("Break your study into short, focused sessions with small breaks.")
        topic_advice.append("Practice past exam papers to reduce fear and build confidence.")
        topic_advice.append("Progress matters more than pressure — take it step by step.")

    # WORK / CAREER
    if topic_match("work", "job", "office", "career"):
        topic_advice.append("Organize your tasks — small progress reduces stress.")
        topic_advice.append("Take a short break if you're overwhelmed.")

    # RELATIONSHIPS
    if topic_match("relationship", "partner", "lover", "love"):
        topic_advice.append("Honest and gentle communication can clear misunderstandings.")
        topic_advice.append("Reflect on your emotional needs right now.")

    # FRIENDS
    if topic_match("friend", "friends"):
        topic_advice.append("Reaching out to a friend can lighten emotional weight.")
        topic_advice.append("Think of someone you appreciate in your life.")

    # FAMILY
    if topic_match("famili", "parent", "home"):
        topic_advice.append("Family emotions can be complex — patience helps.")
        topic_advice.append("Express your feelings gently and clearly.")

    # HEALTH
    if topic_match("health", "sick", "ill", "pain"):
        topic_advice.append("Listen to your body — rest is important.")
        topic_advice.append("If symptoms continue, consider speaking to a professional.")

    # MONEY
    if topic_match("money", "financ", "salary", "debt"):
        topic_advice.append("Write down your expenses to regain control.")
        topic_advice.append("Financial stress is common — take it one step at a time.")

    # SCHOOL / COLLEGE
    if topic_match("school", "colleg", "class", "univers"):
        topic_advice.append("Consistency creates growth — keep going.")
        topic_advice.append("Don't hesitate to ask for help — you're not alone.")

    # FEAR THEMES
    if topic_match("fear", "danger", "threat"):
        topic_advice.append("Ground yourself by noticing your surroundings — you're safe.")

    # -------------------------
    # FINAL COMBINATION
    # -------------------------
    final = emotion_advice.get(emotion, [])

    if topic_advice:
        final.append("\n### Topic-Based Advice:")
        final.extend(topic_advice)

    if not final:
        final = ["Take a moment to reflect on your feelings today."]

    return final
