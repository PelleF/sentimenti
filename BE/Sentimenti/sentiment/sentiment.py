import nltk
import uuid
from nltk.sentiment import SentimentIntensityAnalyzer


class SentimentAnalysis:

    def __init__(self):
        nltk.download('vader_lexicon')
        self.sentimentEngine = SentimentIntensityAnalyzer()

    def analyse(self, text):
        scores = self.sentimentEngine.polarity_scores(text)

        # Return just the negative score
        return scores.get('neg')

    def get_list_with_scores(self, list_of_articles):

        # List.of< UUID | Sentiment score | Title | URL >
        list_of_articles_sentiment = list()

        # We should have a top 3 or nothing
        if len(list_of_articles) > 2:
            for x in range(len(list_of_articles)):

                # Values in React format
                values = {'id': str(uuid.uuid4()),
                          'score': self.analyse(list_of_articles[x]['content']),
                          'title': list_of_articles[x]['title'],
                          'url': list_of_articles[x]['url'],
                          'content': list_of_articles[x]['content']}

                list_of_articles_sentiment.append(values)

                # Make it a max 1000 sized
                if x == 999:
                    break

        return list_of_articles_sentiment

    @staticmethod
    def get_cropped_list_with_top_3(list_of_articles_sentiment):

        list_of_articles_sentiment_cropped = list()

        # We should have a top 3 or nothing
        if len(list_of_articles_sentiment) > 2:
            # Sort on descending sentiment score
            sortedList = sorted(list_of_articles_sentiment, key=lambda x: x['score'], reverse=True)

            # Add top 3 in new list
            for index in range(3):
                list_of_articles_sentiment_cropped.append(sortedList[index])

        return list_of_articles_sentiment_cropped


if __name__ == '__main__':
    # Just for testing
    from innovationProject.news.news import NewsApiClass

    news = NewsApiClass()
    list_of_articles = news.get_headline_articles("Deloitte")
    engine = SentimentAnalysis()
    list_with_scores = engine.get_list_with_scores(list_of_articles)
    print(engine.get_cropped_list_with_top_3(list_with_scores))

