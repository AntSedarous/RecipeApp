# Generated by Django 2.0.2 on 2018-03-12 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipies', '0009_auto_20180307_0346'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='is_liked',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='like',
            name='recent_like',
            field=models.DateTimeField(auto_now=True),
        ),
    ]