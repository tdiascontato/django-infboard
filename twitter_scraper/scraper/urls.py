from django.urls import path
from . import views

urlpatterns = [
    path('recent-tweets/', views.recent_tweets, name='recent_tweets'),
    path('numbers-stats-general/', views.numbers_stats_general, name='numbers_stats_general'),
    path('influencer-rank/', views.influencer_rank, name='influencer_rank'),
    path('tweets/', views.all_tweets, name='all_tweets'),
    path('influencer-save/', views.influencer_save, name='influencer_save'),
]