from django.db import models

class Tweet(models.Model):
    tweet_id = models.CharField(max_length=50, unique=True)
    content = models.TextField()
    username = models.CharField(max_length=50)
    created_at = models.DateTimeField()
    fetched_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.username}: {self.content[:30]}"

class Influencer(models.Model):
    username = models.CharField(max_length=100)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    created_at = models.DateTimeField()

    def __str__(self):
        return self.handle