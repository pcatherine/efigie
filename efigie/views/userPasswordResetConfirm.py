from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import SetPasswordForm
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect

from efigie.controllers import *
from efigie.forms import *
from efigie.models import UserVerification
from efigie.views import *

def userPasswordResetConfirm(request, key, alert='', description=''):
  if UserVerification.objects.filter(key=key, confirmed=False).exists():
    reset = get_object_or_404(UserVerification, key=key)
    form = UserSetPasswordForm(user=reset.user, data=request.POST or None)
    if form.is_valid():
      form.save()
      reset.confirmed = True
      reset.save()
      return redirect(userLogin)
  else:
    return redirect(userNew)

  return render(request, '_template_login.html', 
    {'form': form, 
     'button': 'Alterar Senha',
     'alert': alert,
     'description': description})
