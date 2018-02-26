from django.urls import path
from . import views
app_name = 'recipies'

urlpatterns = [
    path('create/', views.CreateRecipe.as_view(), name='create'),
    path('<int:pk>/', views.RecipeView.as_view(), name='detailview'),
    path('list/', views.RecipeList.as_view(), name='list'),
    path('by/<str:username>/', views.MyRecipeList.as_view(), name='by_recipe'),
    path('update/<int:pk>/', views.EditRecipeView.as_view(), name='update'),
    path('delete/<int:pk>/', views.DeleteRecipeView.as_view(), name='delete'),
]
