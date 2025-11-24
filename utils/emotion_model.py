from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

# Load Flan-T5 Base model
model_name = "google/flan-t5-base"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)


def get_emotion(text):
    """
    Emotion detection using FLAN-T5-BASE.
    Produces: primary emotion, secondary emotion, reasoning.
    """

    prompt = f"""
    You are an emotion analysis model.
    Analyze the emotional state expressed in the following text:

    "{text}"

    Respond in JSON format with:
    - primary_emotion: one word
    - secondary_emotion: one word if relevant
    - reasoning: short explanation
    """

    inputs = tokenizer(prompt, return_tensors="pt", truncation=True)
    outputs = model.generate(**inputs, max_new_tokens=120)

    raw_output = tokenizer.decode(outputs[0], skip_special_tokens=True)

    # Basic parsing (LLM outputs consistent JSON)
    primary = "unknown"
    secondary = "-"
    reason = ""

    try:
        # Very simple JSON parsing
        data = eval(raw_output)
        primary = data.get("primary_emotion", "unknown").lower()
        secondary = data.get("secondary_emotion", "-").lower()
        reason = data.get("reasoning", "")
    except:
        # Fallback: treat full output as reasoning
        reason = raw_output

    # Flan-T5 does not give probability, so use dummy confidence
    confidence = 0.90  

    return primary, confidence, secondary, reason
