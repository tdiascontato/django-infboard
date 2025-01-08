# twitter_scraper\scraper\utils.py
import time
import tweepy
from decouple import config
from django.utils import timezone
from .models import Tweet, Influencer

def fetch_tweets(username, limit=10):
    bearer_token = config("BEARER_TOKEN")
    client = tweepy.Client(bearer_token=bearer_token)

    try:
        response = client.search_recent_tweets(
            query=f"from:{username}",
            tweet_fields=["text", "created_at"],
            max_results=limit,
        )
        tweets = response.data if response.data else []
        tweet_list = []

        influencer, created = Influencer.objects.get_or_create(
            username=username,
            defaults={"created_at": timezone.now()}
        )

        for tweet in tweets:
            tweet_obj, created = Tweet.objects.get_or_create(
                influencer=influencer,
                created_at=tweet.created_at,
                defaults={
                    "content": tweet.text,
                }
            )
            tweet_list.append({
                "content": tweet.text,
                "username": username,
                "created_at": tweet.created_at,
            })

        return tweet_list
    except tweepy.TooManyRequests as e:
        reset_time = int(e.response.headers.get("x-rate-limit-reset", time.time() + 60))
        wait_time = reset_time - int(time.time())
        raise Exception(f"Rate limit exceeded. Try again in {wait_time} seconds.")
    except tweepy.TweepyException as e:
        raise Exception(f"Error: {str(e)}")
