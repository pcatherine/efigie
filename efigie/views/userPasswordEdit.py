# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from efigie.controllers import *
from efigie.views import *
from efigie.forms import *

#pela pagina

@login_required
def userPasswordEdit(request):
  template_name = 'accounts/edit_password.html'
  context = {}
  if request.method == 'POST':
    form = PasswordChangeForm(data=request.POST,user=request.user)
    if form.is_valid():
      form.save()
      messages.success(request,'Sua senha foi alterada com sucesso!')
      context['success'] = True

  else:
    form = PasswordChangeForm(user=request.user)

  context['form'] = form
  return render(request,template_name, context)