from django.forms import forms
from . import models

class RecipeCreateForm(forms.Form):
    class Meta:
        model = models.Recipe
        fields = ('cuisine', 'name', 'ingredients', 'instructions', 'about', 'cuisine')
