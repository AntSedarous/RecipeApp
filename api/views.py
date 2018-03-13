from django.shortcuts import render
from api.serializers import RecipeSerializer
from recipies.models import Recipe
from rest_framework import generics
# Create your views here.

class RecipeListCreate(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
