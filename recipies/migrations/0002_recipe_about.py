# Generated by Django 2.0.2 on 2018-02-23 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='about',
            field=models.TextField(blank=True, default=''),
        ),
    ]
