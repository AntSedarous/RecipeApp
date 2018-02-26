from django.forms import forms
from . import models

class RecipeCreateForm(forms.Form):
    class Meta:
        model = models.Recipe
        fields = ('name', 'ingredients', 'instructions', 'about', 'cuisine')
