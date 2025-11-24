from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import torch.nn.functional as F

# Load tokenizer & model
tokenizer = AutoTokenizer.from_pretrained("SamLowe/roberta-base-go_emotions")
model = AutoModelForSequenceClassification.from_pretrained("SamLowe/roberta-base-go_emotions")

def get_emotion(text):
    """Return the top predicted emotion from GoEmotions model."""
    # Tokenize input text
    inputs = tokenizer(text, return_tensors="pt", truncation=True)

    # Forward pass through model
    outputs = model(**inputs)

    # Convert logits to probabilities
    probabilities = F.softmax(outputs.logits, dim=1)

    # Index of highest probability
    top_idx = probabilities.argmax().item()

    # Extract emotion label
    emotion = model.config.id2label[top_idx]

    # Highest probability score
    confidence = probabilities[0][top_idx].item()

    return emotion, confidence
