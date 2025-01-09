# twitter_scraper\scraper\urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('recent-tweets/', views.recent_tweets, name='recent_tweets'),
    path('numbers-stats-general/', views.numbers_stats_general, name='numbers_stats_general'),
    path('influencer-rank/', views.influencer_rank, name='influencer_rank'),
]

    # path('influencer-followers-tweets/', views.scrape_tweets, name='scrape_tweets'),
    # path('number-tweets/', views.scrape_tweets, name='scrape_tweets'),
    # path('rank-influencer/', views.scrape_tweets, name='scrape_tweets'),
    # path('tweets/', views.scrape_tweets, name='scrape_tweets'),
    # path('score-general/', views.scrape_tweets, name='scrape_tweets'),