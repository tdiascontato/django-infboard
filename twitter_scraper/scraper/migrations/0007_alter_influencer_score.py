# Generated by Django 5.1.4 on 2025-01-08 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0006_influencer_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='influencer',
            name='score',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
    ]