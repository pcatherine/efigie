from django import template
from django.contrib import messages
from django.http import HttpResponse
from django.urls import resolve, reverse

from efigie.models import UserConfirmation, Category, Key
from efigie.urls import breadcrumbResolve


register = template.Library()

@register.assignment_tag
def emailConfirmation(user):
  if UserConfirmation.objects.filter(user=user, category=Category.VERIFICATION, confirmed=False).exists():
    return True
  return False


@register.assignment_tag
def urlResolve(url_name):
  title, icon = breadcrumbResolve(url_name)
  breadcrumb = {'title': title, 'icon': icon, 'url': url_name}
  return breadcrumb


@register.assignment_tag
def urlIcon(url_name):
  title, icon = breadcrumbResolve(url_name)
  return icon


@register.assignment_tag
def urlTitle(url_name):
  title, icon = breadcrumbResolve(url_name)
  return title