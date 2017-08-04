from functools import wraps

from django.contrib import messages
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect, reverse
from django.utils.decorators import available_attrs

from efigie.utils import invariants

def model_required(Model, url, user=False, parm=None):
  """
  Checks if an item exists on a specific 'model', if it exists,
  execute the view, if it doesn't exist, set an error
  message and redirect to 'url'. Usage:

    @model_required(MyModel, 'url_name')
    def my_view(request, param1):
      ...

  or

    @model_required(MyModel1, 'url_name1', 'param1')
    @model_required(MyModel2, ('url_name1', 'param1'), 'param2')
    def my_view(request, param1, param2):
      ...

  Note: It is necessary to make an explicit param name when the
  view has 2 or more params and it is possible to redirect to a
  view with params.

  """

  def decorator(func):
    @wraps(func, assigned=available_attrs(func))
    def inner(request, *args, **kwargs):
      if parm == None:
        if len(kwargs) == 1:
          value = ''.join(kwargs.values())
        else:
          return HttpResponseNotFound('<h1>ALGO DE ERRADO NÃO ESTA CERTO</h1>')
      else:
        value = kwargs[parm]

      if not user:
        if not Model.objects.filter(id=value).exists():
          messages.error(request, invariants.alert_not_found_error % (Model._meta.verbose_name.title()))
          if isinstance(url, str):
            return redirect(url)
          else:
            args = []
            for x in range(1 , len(url)):
              args.append(int(kwargs[url[x]]))
            return redirect(reverse(url[0], args=args))
      else:
        if not Model.objects.filter(id=value, user=request.user).exists():
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
