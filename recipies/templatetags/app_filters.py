
from django import template
from recipies import models

register = template.Library()


def htfy(value):
    if str(value)[0]=='#':
        return value
    else:
        return '#'+str(value)

register.filter('htfy', htfy)

def get_recipe(value):
    return [val.recipe for val in value]

register.filter('get_recipe', get_recipe)


def get_like(value, inp):
    try:
        tmp = max([(val.recipe.pk == inp) & val.is_liked for val in value])
    except:
        return False
    else:
        return tmp
register.filter('get_like', get_like)


def get_recipe_frpk(value):
    return models.Recipe.objects.get(pk__exact=value)

register.filter('get_recipe_frpk', get_recipe_frpk)
