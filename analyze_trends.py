import pandas as pd
import matplotlib.pyplot as plt

def analyze_trends(results_path='output/analysis_results.csv'):
    df = pd.read_csv(results_path)
    sentiment_counts = df['sentiment'].value_counts()
    emotion_counts = df['emotion'].value_counts()
    print('Sentiment Distribution:')
    print(sentiment_counts)
    print('\nEmotion Distribution:')
    print(emotion_counts)
    # Plot sentiment
    sentiment_counts.plot(kind='bar', title='Sentiment Distribution')
    plt.ylabel('Count')
    plt.savefig('output/sentiment_distribution.png')
    plt.close()
    # Plot emotion
    emotion_counts.plot(kind='bar', title='Emotion Distribution')
    plt.ylabel('Count')
    plt.savefig('output/emotion_distribution.png')
    plt.close()
    print('Trend plots saved to output/.')

if __name__ == '__main__':
    analyze_trends()
