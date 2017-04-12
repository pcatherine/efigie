from django import template

from efigie.models import UserVerification, Category

register = template.Library()

@register.assignment_tag
def emailConfirmation(user):
  if UserVerification.objects.filter(user=user, category=Category.VERIFICATION, confirmed=False).exists():
    return True
  return False