from django import template

from efigie.models import UserVerification, Category


register = template.Library()

@register.simple_tag
def version():
  return "0.3.988" 


@register.simple_tag
def emailConfirmation(user):
  if UserVerification.objects.filter(user_id=6, category=Category.VERIFICATION, confirmed=True).exists():
    return True
  return False