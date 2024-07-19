
from transformers import pipeline

class SentimentAnalyzer:
    def __init__(self):
        self.sentiment_pipeline = pipeline("sentiment-analysis")

    def analyze_sentiment(self, text):
        result = self.sentiment_pipeline(text)
        return result[0]
