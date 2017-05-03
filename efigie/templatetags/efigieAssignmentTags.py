from django import template
from django.contrib import messages
from django.http import HttpResponse

from efigie.models import UserConfirmation, Category, Key

register = template.Library()

@register.assignment_tag
def emailConfirmation(user):
  if UserConfirmation.objects.filter(user=user, category=Category.VERIFICATION, confirmed=False).exists():
    return True
  return False
