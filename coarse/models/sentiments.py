from enum import Enum

class Sentiment(str, Enum):
    NEG="Negative"
    NEU="Neutral"
    POS="Positive"