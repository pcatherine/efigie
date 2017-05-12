from django import template

register = template.Library()

@register.filter
def addcssclass(field, css):
  return field.as_widget(attrs={"class":css})
