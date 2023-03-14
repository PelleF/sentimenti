# Create your views here.
from django.http import HttpResponse
from news.news import NewsApiClass
from sentiment.sentiment import SentimentAnalysis
import json

# Classes instantiated once
news = NewsApiClass()
sentiment = SentimentAnalysis()


def index(request):
    # Logging
    print("Received incoming request for search: " + request.GET.get('companyName', ''))

    # Query parameter
    company_name = request.GET.get('companyName', '')

    # Call news API
    list_of_articles = news.get_articles(company_name)
#
    # Do score
    list_of_articles_sentiments = sentiment.get_list_with_scores(list_of_articles)
#
    # Get top 3
    list_of_articles_sentiments_cropped = sentiment.get_cropped_list_with_top_3(list_of_articles_sentiments)

    # Return as json
    return HttpResponse(json.dumps(list_of_articles_sentiments_cropped))
