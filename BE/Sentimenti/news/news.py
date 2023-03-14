import datetime

from newsapi import NewsApiClient
import json


class NewsApiClass:

    def __init__(self):
        self.newsapi = NewsApiClient(api_key="ea562e9552704073b052102189089ee8")

    def get_articles(self, keyword):

        # Only allowed to query 1 month in past
        from_data = datetime.date.today() - datetime.timedelta(days=28)
        to_data = datetime.date.today()
        response = self.newsapi.get_everything(q=keyword,
                                                    from_param=from_data,
                                                    to=to_data,
                                                    language='en',
                                                    sort_by='relevancy',
                                                    page=1)

        # Only get articles list from call
        articles = response.get('articles')

        # Log
        print("Call to News API returned " + str(len(articles)) + " articles for keyword '" + keyword + "'.")

        return articles


if __name__ == "__main__":
    news = NewsApiClass()
    articels = news.get_articles("Deloitte")
    print('debu')

