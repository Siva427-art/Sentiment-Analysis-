import pandas as pd
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import nltk
import os
from config import AMAZON_REVIEWS_PATH, SOCIAL_MEDIA_PATH, NEWS_PATH

nltk.download('punkt', quiet=True)

# Load data from sources
def load_data():
    data = []
    for path, source in [
        (AMAZON_REVIEWS_PATH, 'amazon'),
        (SOCIAL_MEDIA_PATH, 'social'),
        (NEWS_PATH, 'news')
    ]:
        if os.path.exists(path):
            df = pd.read_csv(path)
            df['source'] = source
            data.append(df)
    if data:
        return pd.concat(data, ignore_index=True)
    return pd.DataFrame(columns=['text', 'source'])

# Sentiment classification
analyzer = SentimentIntensityAnalyzer()
def classify_sentiment(text):
    vs = analyzer.polarity_scores(str(text))
    compound = vs['compound']
    if compound >= 0.05:
        return 'positive'
    elif compound <= -0.05:
        return 'negative'
    else:
        return 'neutral'

# Emotion detection (simple lexicon-based)
EMOTION_LEXICON = {
    'happy': 'joy', 'joyful': 'joy', 'delighted': 'joy',
    'sad': 'sadness', 'angry': 'anger', 'fearful': 'fear',
    'surprised': 'surprise', 'disgusted': 'disgust',
    'love': 'love', 'hate': 'hate'
}
def detect_emotion(text):
    words = nltk.word_tokenize(str(text).lower())
    emotions = [EMOTION_LEXICON[w] for w in words if w in EMOTION_LEXICON]
    return ', '.join(set(emotions)) if emotions else 'none'

# Main analysis pipeline
def analyze():
    df = load_data()
    if df.empty:
        print('No data found. Please add data files to the data/ directory.')
        return
    df['sentiment'] = df['text'].apply(classify_sentiment)
    df['emotion'] = df['text'].apply(detect_emotion)
    df.to_csv('output/analysis_results.csv', index=False)
    print('Analysis complete. Results saved to output/analysis_results.csv')

if __name__ == '__main__':
    analyze()
