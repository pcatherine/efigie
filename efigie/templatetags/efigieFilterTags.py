from django import template
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe
from django.urls import resolve, reverse

from efigie.urls import breadcrumbResolve

register = template.Library()

@register.filter
def addcssclass(field, css):
  return field.as_widget(attrs={"class":css})

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