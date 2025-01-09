# twitter_scraper\scraper\models.py
from django.db import models


class Influencer(models.Model):
    id = models.AutoField(primary_key=True) 
    username = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField()
    category = models.CharField(max_length=100, null=True, blank=True)
    trend = models.CharField(max_length=100, null=True, blank=True)
    followers = models.CharField(max_length=100, null=True, blank=True)
    tweets_number = models.IntegerField(null=True, blank=True)
    score = models.CharField(max_length=5, null=True, blank=True)

    def __str__(self):
        return self.username


class Tweet(models.Model):
    id = models.AutoField(primary_key=True) 
    influencer = models.ForeignKey(
        Influencer,
        related_name="tweets",
        on_delete=models.CASCADE,
        null=True,
    )
    content = models.TextField()
    created_at = models.DateTimeField()
    url = models.URLField(null=True, blank=True)
    comment = models.CharField(max_length=250, unique=False, null=True, blank=True)
    category = models.CharField(max_length=100, null=True, blank=True)
    percentual = models.CharField(max_length=4, null=True, blank=True)

    def __str__(self):
        return f"{self.influencer.username}: {self.content[:30]}"
