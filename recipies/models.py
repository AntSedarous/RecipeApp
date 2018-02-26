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

    def get_absolute_url(self):
        return reverse('recipies:detailview', kwargs={
        'pk': self.pk})

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']
