from django.urls import path
from . import views

app_name = 'api'

urlpatterns=[
    path('recipe/', views.RecipeListCreate.as_view() ),
]
