from functools import wraps

from django.contrib import messages
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect, reverse
from django.utils.decorators import available_attrs

from efigie.controllers import invariants

def model_required(Model, url, parm=None):
  def decorator(func):
    @wraps(func, assigned=available_attrs(func))
    def inner(request, *args, **kwargs):
      if(parm == None):
        if len(kwargs) == 1:
          value = ''.join(kwargs.values())
        else:
          return HttpResponseNotFound('<h1>ALGO DE ERRADO NÃO ESTA CERTO</h1>')
      else:
        value = kwargs[parm]


      if not Model.objects.filter(id=value).exists():
        messages.error(request, invariants.alert_not_found_error % (Model._meta.verbose_name.title()))
        if isinstance(url, str):
          return redirect(url)
        else:
          args = []
          for x in range(1 , len(url)):
            args.append(int(kwargs[url[x]]))
          return redirect(reverse(url[0], args=args))

      return func(request, *args, **kwargs)
    return inner
  return decorator
