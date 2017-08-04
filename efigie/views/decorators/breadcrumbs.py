#!/usr/bin/python
#-*- coding: utf-8 -*-

from functools import wraps

from django.shortcuts import render, redirect, reverse
from django.utils.decorators import available_attrs

from efigie import urls

def breadcrumbs(items):
  """
  Adds the key optimaster in request.META, add keys breadcrumbs
  and back in request.META.optimaster, where the key breadcrumbs
  is a hierarchical series of hyperlinks displayed at the top
  of a web page, indicating the page's position in the overall
  structure of the website, and back is the previous page url.
  Usage:

    @breadcrumbs(['home', 'my_list', ('my_show', 'param1')])
    def my_view(request, param1):
      ...

  Example of breadcrumbs in template:

    {{ request.META.efigie.breadcrumbs|safe }}

  Example of back button in template:

    <a href="{{ request.META.efigie.back }}">Back</a>

  Note: It is necessary to make an explicit param name when
  redirect needs param.

  """

  def decorator(func):
    @wraps(func, assigned = available_attrs(func))
    def inner(request, *args, **kwargs):

      request.META['efigie'] = {'breadcrumbs': '', 'back': ''}

      breadcrumbs = '<ol class="breadcrumb">'
      for url_name in items:
        url = icon = title = ''
        if not isinstance(url_name, str):
          title, icon = urls.breadcrumbResolve(url_name[0])
          breadcrumb_args = []
          for x in range(1 , len(url_name)):
            value = kwargs[url_name[x]]
            breadcrumb_args.append(value)

          url = reverse(url_name[0], args=breadcrumb_args)
        else:
          url = reverse(url_name)
          title, icon = urls.breadcrumbResolve(url_name)

        if (url_name == items[-1]):
          breadcrumbs += '<li class="active" > <i class="fa %s"></i> <span>%s</span></li> ' % (icon, title)
        else:
          breadcrumbs += '<li ><a href="%s"> <i class="fa %s"></i> <span>%s</span> </a> </li> ' % (url, icon, title )

        if len(items) > 1:
          if url_name == items[-2]:
            request.META['efigie']['back'] = url

      breadcrumbs += '</ol>'

      request.META['efigie']['breadcrumbs'] = breadcrumbs
      return func(request, *args, **kwargs)
    return inner
  return decorator
