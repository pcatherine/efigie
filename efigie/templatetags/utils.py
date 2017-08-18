from collections import OrderedDict

from django import template
from django.contrib import messages
from django.forms.models import model_to_dict, fields_for_model
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

  Examples:
    {% version %}
  """
  return "0.3.1070"


@register.filter
def addcssclass(field, css):
  """
  Replaces in form's field placeholder by field's label and css class by css param.

  Examples:
    {{ field|addcssclass:'form-control input-lg' }}
  """
  # return field.as_widget(attrs={"class":css, "placeholder": '%s%s' % ('* ' if field.field.required else '', field.label)})
  return field.as_widget(attrs={"class":css})



#AGARD arrmar daqui para baixo
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






@register.simple_tag
def modelName(Model):
  """
  Returns verbose_name for a Model.
  """
  return eval(str(Model))._meta.verbose_name


@register.simple_tag
def modelFieldName(Model, field_name):
  """
  Returns verbose_name for a field.
  """
  return eval(str(Model))._meta.get_field(field_name).verbose_name.title()


@register.assignment_tag
def modelDict(Model, instance):
  """
  Return a dict containing the data in ``instance`` suitable for passing as
  a Form's ``initial`` keyword argument in order.
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
