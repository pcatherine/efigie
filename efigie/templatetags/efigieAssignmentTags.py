from django import template
from django.contrib import messages
from django.http import HttpResponse
from django.urls import resolve, reverse

from efigie.models import UserConfirmation, Category, Key

register = template.Library()

@register.assignment_tag
def emailConfirmation(user):
  if UserConfirmation.objects.filter(user=user, category=Category.VERIFICATION, confirmed=False).exists():
    return True
  return False

@register.assignment_tag
def resolveUrl(breadcrumb):
  func, args, kwargs = reverse(breadcrumb)
  url = {'func': func, 'args': args, 'kwargs': kwargs}
  return url

