from django.db import models
from django.contrib import auth
from django.urls import reverse
# Create your models here.

from taggit.managers import TaggableManager



class Recipe(models.Model):
    user = models.ForeignKey(auth.models.User, on_delete=models.CASCADE, related_name='recipes')
    name = models.CharField(max_length=100)
    instructions = models.TextField()
    ingredients = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    about = models.TextField(blank=True, default='')
    cuisine = TaggableManager()
    pic = models.ImageField(upload_to='images', null=True, blank=True)
    like_id = models.CharField(max_length=20, editable=False)
    save_id = models.CharField(max_length=20, editable=False)

    def get_absolute_url(self):
        return reverse('recipies:detailview', kwargs={
        'pk': self.pk})

    def save(self, *args, **kwargs):
        self.like_id = str(self.pk) + 'l'
        self.save_id = str(self.pk) + 's'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']


class Like(models.Model):
    user = models.ForeignKey(auth.models.User, on_delete=models.CASCADE, related_name='likes')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='likes')
    liked_at = models.DateTimeField(auto_now=True)

class Save(models.Model):
    user = models.ForeignKey(auth.models.User, on_delete=models.CASCADE, related_name='saves')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='saves')
    saved_at = models.DateTimeField(auto_now=True)
