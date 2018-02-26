
from django import template


register = template.Library()


def htfy(value):
    if str(value)[0]=='#':
        return value
    else:
        return '#'+str(value)

register.filter('htfy', htfy)
