# Generated by Django 5.1.4 on 2025-01-08 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0008_remove_influencer_comment_tweet_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='influencer',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
