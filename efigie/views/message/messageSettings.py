#!/usr/bin/python
#-*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.db import models
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, render_to_response
from django.template import loader, Context, Template, RequestContext
from django.utils.safestring import mark_safe

# from django.core.servers.basehttp import FileWrapper

# from efigie.controller import Effigy, EffigyParameters, EffigyCommunication
from efigie.models import Message, Key
# import efigie.config
# import json
from efigie.forms import *
from efigie.views import *

@login_required
def messageSettings(request):
  form = MessageSettingsForm(request.POST or None, request.FILES or None)
  if form.is_valid():
    form.save()
  #   file = request.FILES['file']
  #   try:
  #     imageEfigie = Effigy.setEffigy(image, '000000000000000', message, "", msg.id)

  #     # date = file.read().decode('utf-8')
  #     # privateKey, publicKey, name, size = date.split(';')

  #     # key = form.save(user=request.user, privateKey=privateKey, publicKey=publicKey, name=name, size=size)
  #     # #AGARD trans
  #     # messages.info(request, 'Chave <b>%s</b> já importada.' % (key.name))
  #     # return redirect(keyImport)

  #   except Exception as e:
  #     messages.error(request, 'O arquivo não pode ser importado.')
  #     return redirect(keyImport)

  return render(request, 'message/form.html',
    {'form': form,
     'button': 'Save'})

  # CATHERINE salvar no banco

  # return render(request, EffigyParameters.MESSAGE_SETTINGS)
  # return render(request, 'index.html')
