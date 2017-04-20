# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from efigie.controllers import *
from efigie.views import *
from efigie.forms import *

#AGARD

@login_required
def userPasswordEdit(request, form=None):

  if form == None:
    return redirect('userSettings')


  print ('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')

  if form.is_valid():
    form.save()
    print ('aqui teoricamente foi')
    return request, 'success', 'Sua senha foi alterada com sucesso!'

  return request, 'danger', 'Senha nao pode ser alterada.'