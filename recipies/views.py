from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from . import models
from braces.views import SelectRelatedMixin, UserPassesTestMixin
from django.http import Http404
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
# Create your views here.

User = get_user_model()

class OwnershipMixin(object):
    """
    Mixin providing a dispatch overload that checks object ownership. is_staff and is_supervisor
    are considered object owners as well. This mixin must be loaded before any class based views
    are loaded for example class SomeView(OwnershipMixin, ListView)
    """
    def dispatch(self, request, *args, **kwargs):
        self.request = request
        self.args = args
        self.kwargs = kwargs
        # we need to manually "wake up" self.request.user which is still a SimpleLazyObject at this point
        # and manually obtain this object's owner information.
        current_user = request.user
        object_owner = getattr(self.get_object(), 'user')

        if current_user.username != object_owner.username:
            raise PermissionDenied
        return super(OwnershipMixin, self).dispatch(request, *args, **kwargs)


class CreateRecipe(LoginRequiredMixin, generic.CreateView):
    model = models.Recipe
    fields = ('name', 'ingredients', 'instructions', 'about')
    template_name = 'recipies/create_recipe.html'
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class RecipeList(generic.ListView, SelectRelatedMixin):
    model = models.Recipe
    select_related = ('user')
    template_name = 'recipies/recipe_list.html'


class RecipeView(generic.DetailView, SelectRelatedMixin):
    model = models.Recipe
    select_related = ('user')
    template_name = 'recipies/single_recipe.html'


class MyRecipeList(generic.ListView, SelectRelatedMixin, LoginRequiredMixin):
    model = models.Recipe
    select_related = ('user')
    template_name = 'recipies/my_recipies.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recipe_user'] = self.recipe_user
        return context

    def get_queryset(self):
        try:
            self.recipe_user = User.objects.prefetch_related('recipes').get(username__iexact=self.kwargs.get('username'))
        except User.DoesNotExist:
            raise Http404

        else:
            return self.recipe_user.recipes.all()

        self.queryset = self.model.objects.filter()

class EditRecipeView(OwnershipMixin, generic.UpdateView, SelectRelatedMixin):
    model = models.Recipe
    select_related=('user')
    fields = ('name', 'ingredients', 'instructions', 'about', 'cuisine')
    template_name = 'recipies/recipe_update.html'


class DeleteRecipeView(OwnershipMixin, generic.DeleteView):
    model = models.Recipe
    template_name='recipies/delete_confirm.html'
    success_url = reverse_lazy('home')
