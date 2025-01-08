# twitter_scraper\scraper\models.py
from django.db import models


class Influencer(models.Model):
    username = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField()

    def __str__(self):
        return self.handle

class Tweet(models.Model):
    influencer = models.ForeignKey(
        Influencer,
        related_name="tweets",
        on_delete=models.CASCADE,
        null=True,
    )
    content = models.TextField()
    created_at = models.DateTimeField()

    def __str__(self):
        return f"{self.username}: {self.content[:30]}"