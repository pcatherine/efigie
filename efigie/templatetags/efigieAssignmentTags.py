from django import template

from efigie.models import UserConfirmation, Category

register = template.Library()

@register.assignment_tag
def emailConfirmation(user):
  if UserConfirmation.objects.filter(user=user, category=Category.VERIFICATION, confirmed=False).exists():
    return True
  return False