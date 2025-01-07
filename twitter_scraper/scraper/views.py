# twitter_scraper\scraper\views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers import serialize
from .utils import fetch_tweets

from .models import Tweet
import json

@csrf_exempt
def scrape_tweets(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        limit = request.POST.get('limit', 10) 
        if not username:
            return JsonResponse({'error': 'Username is required'}, status=400)

        tweets = fetch_tweets(username, limit)
        return JsonResponse({'tweets': tweets })

