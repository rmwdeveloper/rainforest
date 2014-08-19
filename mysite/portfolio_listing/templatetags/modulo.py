from django import template
import re
register = template.Library()

@register.filter
def modulo(num, val):
    return num % val