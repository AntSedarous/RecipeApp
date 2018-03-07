# Generated by Django 2.0.2 on 2018-03-07 03:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipies', '0008_auto_20180306_0441'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cuisine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cuisine', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='cuisine',
        ),
        migrations.AddField(
            model_name='recipe',
            name='cuisine',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='recipies.Cuisine'),
        ),
    ]
