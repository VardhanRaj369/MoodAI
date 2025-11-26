import re
import numpy as np
from textblob import TextBlob
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class EmotionalAnalyzer:
    def __init__(self):
        self.emotion_classifier = None
        self.sentiment_analyzer = None
        self.models_loaded = False
        self.load_models()

    def load_models(self):
        """Load models with error handling and fallbacks"""
        try:
            from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification
            import torch

            logger.info("Loading emotion classification model...")
            self.emotion_classifier = pipeline(
                "text-classification",
                model="j-hartmann/emotion-english-distilroberta-base",
                return_all_scores=True,
                device=-1  # Use CPU
            )

            logger.info("Loading sentiment analysis model...")
            self.sentiment_analyzer = pipeline(
                "sentiment-analysis",
                device=-1  # Use CPU
            )

            self.models_loaded = True
            logger.info("All models loaded successfully!")

        except Exception as e:
            logger.error(f"Error loading models: {e}")
            self.models_loaded = False
            self.setup_fallback_analyzer()

    def setup_fallback_analyzer(self):
        """Setup fallback analysis using TextBlob and rule-based methods"""
        logger.info("Setting up fallback analyzer...")
        self.fallback_emotions = {
            'positive': ['joy', 'surprise'],
            'negative': ['anger', 'fear', 'sadness', 'disgust'],
            'neutral': ['neutral']
        }

    def extract_context(self, text):
        """Extract context from text"""
        context = {
            'topics': [],
            'sentiment': '',
            'intensity': 0,
            'key_entities': []
        }

        try:
            # Analyze with TextBlob for additional insights
            blob = TextBlob(text)

            # Sentiment analysis with fallback
            if self.models_loaded:
                sentiment_result = self.sentiment_analyzer(text[:512])[0]
                context['sentiment'] = sentiment_result['label']
                context['intensity'] = sentiment_result['score']
            else:
                # Fallback sentiment analysis using TextBlob
                polarity = blob.sentiment.polarity
                if polarity > 0.1:
                    context['sentiment'] = 'POSITIVE'
                    context['intensity'] = abs(polarity)
                elif polarity < -0.1:
                    context['sentiment'] = 'NEGATIVE'
                    context['intensity'] = abs(polarity)
                else:
                    context['sentiment'] = 'NEUTRAL'
                    context['intensity'] = 0.5

            # Extract potential topics (simple noun phrase extraction)
            context['topics'] = [str(noun) for noun in blob.noun_phrases[:5]]

            # Simple entity extraction (names, places, etc.)
            context['key_entities'] = self.extract_entities(text)

        except Exception as e:
            logger.error(f"Error in context extraction: {e}")
            # Provide default values
            context['topics'] = ['general']
            context['sentiment'] = 'NEUTRAL'
            context['intensity'] = 0.5
            context['key_entities'] = []

        return context

    def extract_entities(self, text):
        """Simple entity extraction using patterns"""
        entities = []

        try:
            # Extract potential names (capitalized words)
            name_pattern = r'\b[A-Z][a-z]+\s+[A-Z][a-z]+\b'
            names = re.findall(name_pattern, text)
            entities.extend(names)

            # Extract potential places (contextual)
            place_indicators = ['at', 'in', 'from', 'to', 'going to']
            words = text.lower().split()
            for i, word in enumerate(words):
                if word in place_indicators and i + 1 < len(words):
                    entities.append(words[i + 1].title())

        except Exception as e:
            logger.error(f"Error in entity extraction: {e}")

        return list(set(entities))[:3]

    def analyze_emotion_fallback(self, text):
        """Fallback emotion analysis using TextBlob and keywords"""
        blob = TextBlob(text)
        polarity = blob.sentiment.polarity
        subjectivity = blob.sentiment.subjectivity

        # Keyword-based emotion detection
        emotion_keywords = {
            'anger': ['angry', 'mad', 'furious', 'annoyed', 'frustrated'],
            'fear': ['scared', 'afraid', 'worried', 'anxious', 'nervous'],
            'joy': ['happy', 'excited', 'joy', 'delighted', 'pleased'],
            'sadness': ['sad', 'unhappy', 'depressed', 'miserable', 'lonely'],
            'surprise': ['surprised', 'shocked', 'amazed', 'astonished'],
            'disgust': ['disgusted', 'gross', 'revolted', 'sickened']
        }

        text_lower = text.lower()
        emotion_scores = {}

        # Score emotions based on keywords
        for emotion, keywords in emotion_keywords.items():
            score = sum(1 for keyword in keywords if keyword in text_lower)
            emotion_scores[emotion] = score / len(keywords) if keywords else 0

        # Adjust based on sentiment
        if polarity > 0.3:
            emotion_scores['joy'] += 0.3
        elif polarity < -0.3:
            emotion_scores['sadness'] += 0.3

        # Determine primary emotion
        if any(emotion_scores.values()):
            primary_emotion = max(emotion_scores.items(), key=lambda x: x[1])
        else:
            primary_emotion = ('neutral', 0.5)

        # Normalize scores
        total = sum(emotion_scores.values()) + 0.1  # Add small value to avoid division by zero
        normalized_scores = {emotion: (score / total) for emotion, score in emotion_scores.items()}
        normalized_scores['neutral'] = 0.1  # Always some neutral component

        return {
            'primary_emotion': primary_emotion[0],
            'primary_score': primary_emotion[1],
            'all_emotions': normalized_scores,
            'emotional_intensity': max(normalized_scores.values()) if normalized_scores else 0.5
        }

    def analyze_emotion(self, text):
        """Analyze emotions from text with fallback"""
        if not self.models_loaded:
            return self.analyze_emotion_fallback(text)

        try:
            emotion_results = self.emotion_classifier(text[:512])[0]

            # Sort emotions by score
            sorted_emotions = sorted(emotion_results, key=lambda x: x['score'], reverse=True)

            emotions = {
                'primary_emotion': sorted_emotions[0]['label'],
                'primary_score': sorted_emotions[0]['score'],
                'all_emotions': {emotion['label']: emotion['score'] for emotion in sorted_emotions},
                'emotional_intensity': max([emotion['score'] for emotion in sorted_emotions])
            }

            return emotions

        except Exception as e:
            logger.error(f"Error in emotion analysis: {e}")
            return self.analyze_emotion_fallback(text)

    def get_suggestions(self, emotion_data, context):
        """Provide suggestions based on emotion and context"""
        primary_emotion = emotion_data['primary_emotion']
        intensity = emotion_data['emotional_intensity']
        sentiment = context['sentiment']

        suggestions = []

        # Emotion-based suggestions
        emotion_suggestions = {
            'anger': [
                "Try deep breathing exercises to calm down",
                "Consider taking a short walk to clear your mind",
                "Write down your thoughts in a journal",
                "Practice mindfulness meditation"
            ],
            'fear': [
                "Break down the situation into smaller, manageable parts",
                "Talk to someone you trust about your concerns",
                "Focus on what you can control",
                "Practice grounding techniques"
            ],
            'joy': [
                "Share your happiness with others",
                "Take a moment to appreciate this feeling",
                "Consider doing something creative",
                "Spread positivity to others"
            ],
            'sadness': [
                "Reach out to friends or family for support",
                "Engage in activities you usually enjoy",
                "Practice self-compassion",
                "Consider light physical activity"
            ],
            'surprise': [
                "Take a moment to process the information",
                "Consider the implications before reacting",
                "Talk to others about the surprising event",
                "Keep an open mind about outcomes"
            ],
            'disgust': [
                "Identify the source of discomfort",
                "Consider if this aligns with your values",
                "Remove yourself from the situation if possible",
                "Reflect on why this triggers such a strong reaction"
            ],
            'neutral': [
                "Maintain your balanced perspective",
                "Consider exploring new interests",
                "Practice mindfulness to stay present",
                "Set some personal goals"
            ]
        }

        # Intensity-based adjustments
        if intensity > 0.8:
            suggestions.append("Your emotions are quite intense. Consider taking a break before making decisions.")
        elif intensity < 0.3:
            suggestions.append("Your emotions seem mild. This might be a good time for reflection.")

        # Add emotion-specific suggestions
        if primary_emotion in emotion_suggestions:
            suggestions.extend(emotion_suggestions[primary_emotion][:2])
        else:
            suggestions.extend(emotion_suggestions['neutral'][:2])

        # Sentiment-based suggestions
        if sentiment == 'NEGATIVE' and intensity > 0.6:
            suggestions.append("Consider speaking with a mental health professional for additional support")
        elif sentiment == 'POSITIVE':
            suggestions.append("Use this positive energy to work on personal projects or help others")

        return suggestions
