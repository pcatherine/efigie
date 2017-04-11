from django import template

from efigie.models import UserVerification, Category

register = template.Library()

@register.filter
def addcssclass(field, css):
  return field.as_widget(attrs={"class":css})

# @register.filter
# def emailConfirmation(user):
#   if UserVerification.objects.filter(user_id=6, category=Category.VERIFICATION, confirmed=False).exists():
#     return True
#   return False