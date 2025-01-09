# twitter_scraper\scraper\views.py
import openai
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers import serialize
from .utils import fetch_recents_tweets
from .models import Tweet, Influencer
from decouple import config
from django.db.models import Avg

openai.api_key = config("OPENAI_API_KEY")

@csrf_exempt
def recent_tweets(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        limit = request.POST.get('limit', 10) 
        if not username:
            return JsonResponse({'error': 'Username is required'}, status=400)

        try:
            tweets = fetch_recents_tweets(username, limit)
            return JsonResponse({'tweets': tweets}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
        
@csrf_exempt
def numbers_stats_general(request):
    if request.method == 'GET':
        try:
            num_influencers = Influencer.objects.count()
            num_tweets = Tweet.objects.count()
            avg_score = Influencer.objects.aggregate(Avg('score'))['score__avg']

            stats = {
                'num_influencers': num_influencers,
                'num_tweets': num_tweets,
                'avg_score': avg_score
            }

            return JsonResponse(stats, safe=False)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

@csrf_exempt
def influencer_rank(request):
    if request.method == 'GET':
        try:
            influencers = Influencer.objects.all()
            for influencer in influencers:
                tweets = Tweet.objects.filter(influencer=influencer)
                if tweets.exists():
                    avg_score = tweets.aggregate(Avg('percentual'))['percentual__avg']
                    influencer.score = avg_score
                    influencer.save()
            influencers = influencers.order_by('-score')
            influencer_list = serialize('json', influencers)
            return JsonResponse(influencer_list, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)