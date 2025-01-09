# twitter_scraper\scraper\utils.py
import re
import time
import json
from django.utils import timezone
import tweepy
import openai
from decouple import config
from .models import Tweet, Influencer


def fetch_recents_tweets(username, limit=10):
    bearer_token = config("BEARER_TOKEN")
    client = tweepy.Client(bearer_token=bearer_token)

    try:
        response = client.search_recent_tweets(
            query=f"from:{username}",
            tweet_fields=["text", "created_at", "entities"],
            max_results=limit,
        )
        tweets = response.data if response.data else []
        tweet_list = []

        for tweet in tweets:
            entities = tweet.get("entities", {})
            urls = entities.get("urls", [])
            tweet_url = urls[0].get("expanded_url") if urls else None

            tweet_list.append({
                "content": tweet.text,
                "username": username,
                "created_at": tweet.created_at,
                "url": tweet_url,
            })

        tweet_response = influencer_percentual_comment_category(tweet_list, username)
        return json.dumps(tweet_response, default=str)

    except tweepy.TooManyRequests as e:
        reset_time = int(e.response.headers.get("x-rate-limit-reset", time.time() + 60))
        wait_time = reset_time - int(time.time())
        raise Exception(f"Rate limit exceeded. Try again in {wait_time} seconds.")
    
    except tweepy.TweepyException as e:
        raise Exception(f"Error: {str(e)}")
    


def influencer_percentual_comment_category(tweets, influencer):    
    try:
        influencer_obj, created = Influencer.objects.get_or_create(
            username=influencer,
            defaults={"created_at": timezone.now()}
        )

        tweet_responses = []
        for tweet in tweets:
            prompt = (
                "You are a content analysis expert. Evaluate the factuality of the information "
                "in the following set of tweets, providing a confidence percentage, a simple description of authenticity (one simple prhase), "
                ", the category that best fits the profile (Technology, Entertainment, Beauty, Sports, Business, Health, "
                "Politics, Education, Travel). Return the result in JSON format only, without additional explanations (percentage, comment, category):\n\n"
                f"{tweet}\n\n"
            )
            response = openai.ChatCompletion.create(
                model="gpt-4o",
                messages=[{"role": "user", "content": prompt}]
            )
            try:
                content = response['choices'][0]['message']['content']

                try:
                    json_match = re.search(r'```json\n(.*?)\n```', content, re.DOTALL)
                    if json_match:
                        json_string = json_match.group(1)
                        analysis = json.loads(json_string)
                    else:
                        raise ValueError("JSON block not found in the content.")
                except json.JSONDecodeError as e:
                    print("Failed to parse JSON:", e)
                except Exception as e:
                    print("An error occurred:", e)

                category = analysis.get("category", "Unknown")
                comment = analysis.get("comment", "")
                percentual = analysis.get("percentual", 0)

                tweet_response = Tweet.objects.get_or_create(
                    influencer=influencer_obj,
                    content=tweet["content"],
                    created_at=tweet["created_at"],
                    defaults={
                        "url": tweet["url"],
                        "comment": comment,
                        "category": category,
                        "percentual": percentual,
                    }
                )[0]
                tweet_responses.append(tweet_response)

            except json.JSONDecodeError as e:
                raise Exception(f"Failed to parse JSON response: {content}")

        return tweet_responses

    except Exception as e:
        raise Exception(f"Error at analyzing tweets with ChatGPT: {str(e)}")

def influencer_followers_tweets(username):
    bearer_token = config("BEARER_TOKEN")
    client = tweepy.Client(bearer_token=bearer_token)

    try:
        user = client.get_user(username=username, user_fields=["public_metrics"])
        user_data = user.data
        if user_data:
            followers_count = user_data.public_metrics["followers_count"]
            tweet_count = user_data.public_metrics["tweet_count"]
            return {
                "followers_count": followers_count,
                "tweet_count": tweet_count,
            }
        else:
            raise Exception("User not found")

    except tweepy.TweepyException as e:
        raise Exception(f"Error: {str(e)}")