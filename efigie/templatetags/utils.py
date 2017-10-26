from collections import OrderedDict

from django import template
from django.contrib import messages
from django.contrib.auth.models import User
from django.forms.models import model_to_dict, fields_for_model
from django.http import HttpResponse
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe
from django.urls import resolve, reverse

from efigie.models import Friend, Key, UserConfirmation
from efigie.urls import breadcrumbResolve
import efigie.release as v

register = template.Library()


@register.simple_tag
def version():
  """
  Returns the current version.

  Examples::

    {% version %}
  """
  return "0.9.%s" % (v.VERSION)


@register.assignment_tag
def emailConfirmation(user):
  """
  Checks if user has verified email address.

  Examples::

    {% emailConfirmation request.user as confimation  %}
    {% if confimation %}
      It's necessary to verify the user's email address
    {% endif %}
  """
  if UserConfirmation.objects.filter(user=user, category=UserConfirmation.Category.VERIFICATION, confirmed=False).exists():
    return True
  return False


@register.assignment_tag
def urlResolve(url_name):
  """
  Returns icon and title by ``breadcrumbResolve``.

  Examples::

    {% urlResolve request.resolver_match.url_name %}
  """
  title, icon = breadcrumbResolve(url_name)
  breadcrumb = {'title': title, 'icon': icon, 'url': url_name}
  return breadcrumb


@register.assignment_tag
def urlIcon(url_name):
  """
  Returns the icon by ``breadcrumbResolve``.

  Examples::

    {% urlIcon request.resolver_match.url_name %}
  """
  title, icon = breadcrumbResolve(url_name)
  return icon


@register.assignment_tag
def urlTitle(url_name):
  """
  Returns the title by ``breadcrumbResolve``.

  Examples::

    {% urlTitle request.resolver_match.url_name %}
  """
  title, icon = breadcrumbResolve(url_name)
  return title


@register.simple_tag
def modelName(Model):
  """
  Returns the verbose_name for a Model.

  Examples::

    {% modelName 'User' %}
  """
  return eval(str(Model))._meta.verbose_name


@register.simple_tag
def modelFieldName(Model, field_name):
  """
  Returns the verbose_name for a field.

  Examples::

    {% modelFieldName 'User' 'first_name' %}
  """
  return eval(str(Model))._meta.get_field(field_name).verbose_name.title()


@register.assignment_tag
def modelDict(Model, instance):
  """
  Returns a dict containing field's name and value in model's order
  by instance by instance.

  Examples::

    {% modelDict 'User' request.user as values %}
    {% for key, value in values.items %}
      {% modelFieldName model key %}
      {{ value }}
    {% endfor %}
  """
  d = model_to_dict(instance, exclude='id')
  data = {}
  for key, value in d.items():
    data.update({key:getattr(instance, key)})

  fields = fields_for_model(eval(str(Model)), exclude='id')
  r = OrderedDict(data)
  for field in fields:
    r.move_to_end(field)

  return r


@register.filter
def addcssclass(field, css):
  """
  Adds form's field css class.

  Examples::

    {{ field|addcssclass:'form-control input-lg' }}
  """
  # return field.as_widget(attrs={"class":css, "placeholder": '%s%s' % ('* ' if field.field.required else '', field.label)})

  if field.field.widget.__class__.__name__ == 'CheckboxInput' or field.field.widget.__class__.__name__ == 'CheckboxSelectMultiple':
    return field
  else:
    return field.as_widget(attrs={"class":css})


@register.filter(needs_autoescape=True)
def menuItem(url_name, url_current, autoescape=True):
  """
  Adds an item on the menu and set it active if it's the current url.

  Usage::

    {{ [ url_name ]|menuItem:[ current_url ] }}

  Examples::

    {{ 'login'|menuItem:request.resolver_match.url_name }}
  """
  title, icon = breadcrumbResolve(url_name)

  subtitle = title.split("'")
  if len(subtitle) > 1:
    title = ('%s%s') % (subtitle[0],'s')

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
