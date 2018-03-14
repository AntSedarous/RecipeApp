from django.views.generic import TemplateView, ListView, View
from recipies import models
from braces.views import SelectRelatedMixin
from django.shortcuts import render

class HomePage(ListView, SelectRelatedMixin):
    model = models.Recipe
    template_name = 'index.html'
    select_related = ('user')



#class HomePage(ListView, SelectRelatedMixin):
#    template_name = 'index.html'
#    select_related=('user')
#    model = models.Recipe
#    def get_queryset(self):
#        super().get_queryset()
#        return list(queryset)

class ThanksPage(TemplateView):
    template_name = 'thanks.html'
