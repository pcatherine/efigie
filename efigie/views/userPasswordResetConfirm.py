from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import SetPasswordForm
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect

from efigie.controllers import *
from efigie.views import *
from efigie.forms import *

def userPasswordResetConfirm(request, key, alert='', description=''):
  template_name = 'user_password_reset_confirm.html'
  context = {}
  reset = get_object_or_404(UserPasswordReset, key=key)
  form = UserSetPasswordForm(user=reset.user, data=request.POST or None)
  if form.is_valid():
    form.save()
    return redirect(userLogin)
    # context['success'] = True
  # context['form'] = form
  # return render(request, template_name, context)
  return render(request, '_template_login.html', 
    {'form': form, 
     'button': 'Alterar Senha',
     'alert': alert,
     'description': description})



# @never_cache
# @csrf_protect
# def userNew(request, alert='', description=''):
#   if request.user.is_authenticated():
#     return redirect(index)

#   form = UserNewForm(request.POST or None)
  
#   if form.is_valid():
#     user = form.save()
#     user = authenticate(username=user.username, password=form.cleaned_data['password1'])
#     login(request, user)
#     return redirect(index)

#   return render(request, '_template_login.html', 
#     {'form': form, 
#      'button': 'Cadastrar-se',
#      'alert': alert,
#      'description': description})