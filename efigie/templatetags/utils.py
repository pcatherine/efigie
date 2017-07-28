from django import template
from django.contrib import messages
from django.http import HttpResponse
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe
from django.urls import resolve, reverse

from efigie.models import UserConfirmation, Category, Key
from efigie.urls import breadcrumbResolve


register = template.Library()


@register.simple_tag
def version():
  """
  Returns the current version.
  """
  return "0.3.1070"


@register.filter
def addcssclass(field, css):
  """
  Replaces in form's field placeholder by field's label and css class by css param.
  """
  return field.as_widget(attrs={"class":css, "placeholder": '%s%s' % ('* ' if field.field.required else '', field.label)})


#AGARD
@register.filter(needs_autoescape=True)
def menuTree(name, icon, autoescape=True):
  title, icon = breadcrumbResolve(url_name)
  url = reverse(url_name)
  cssClass = ''
  if url_name == url_current:
  	cssClass = 'active'

  if autoescape:
    esc = conditional_escape
  else:
    esc = lambda x: x
  result = '''
    <li class="%s">
      <a href="%s"><i class="fa %s text-yellow"></i> <span>%s</span></a>
    </li>''' % (esc(cssClass), esc(url), esc(icon), esc(title))
  return mark_safe(result)

@register.filter(needs_autoescape=True)
def menuItem(url_name, url_current, autoescape=True):
  title, icon = breadcrumbResolve(url_name)
  url = reverse(url_name)
  cssClass = ''
  if url_name == url_current:
  	cssClass = 'active'

  if autoescape:
    esc = conditional_escape
  else:
    esc = lambda x: x
  result = '''
    <li class="%s">
      <a href="%s"><i class="fa %s text-yellow"></i> <span>%s</span></a>
    </li>''' % (esc(cssClass), esc(url), esc(icon), esc(title))
  return mark_safe(result)


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
