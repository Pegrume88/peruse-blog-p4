from ..models import Category
from django import template

register = template.Library()

@register.simple_tag
def categories():
    return Category.objects.all()