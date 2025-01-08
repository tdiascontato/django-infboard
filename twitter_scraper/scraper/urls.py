# twitter_scraper\scraper\urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('scrape/', views.scrape_tweets, name='scrape_tweets'),
    path('ai/', views.chatgpt_response, name='chatgpt_response'),
]
