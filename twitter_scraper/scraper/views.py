# twitter_scraper\scraper\views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers import serialize
from .utils import fetch_tweets
import openai
from .models import Tweet
import json

from decouple import config

openai.api_key = config("OPENAI_API_KEY")


@csrf_exempt
def scrape_tweets(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        limit = request.POST.get('limit', 10) 
        if not username:
            return JsonResponse({'error': 'Username is required'}, status=400)

        try:
            tweets = fetch_tweets(username, limit)
            return JsonResponse({'tweets': tweets}, safe=False)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

@csrf_exempt
def chatgpt_response(request):
    if request.method == 'POST':
        try:
            body = json.loads(request.body)
            user_message = body.get('message')
            if not user_message:
                return JsonResponse({'error': 'Message is required'}, status=400)

            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": user_message}
                ],
                max_tokens=100
            )

            reply = response['choices'][0]['message']['content']
            return JsonResponse({'reply': reply})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=405)