# !/usr/bin/python
# -*- coding: utf-8 -*-

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt, csrf_protect

from efigie import *
from efigie.forms import *
from efigie.models import Key
from efigie.views import *

@csrf_protect
@login_required
def keyImport(request):
  form = KeyImportForm(request.POST or None, request.FILES or None)
  if form.is_valid():
    file = request.FILES['file']
    date = file.read()
    lines = date.decode("utf-8")
  
    privateKey = ''
    for i in range(len(lines)):
      privateKey += lines[i-1:i]
      if len(privateKey) > 29:
        if privateKey[i-29:] == '-----END RSA PRIVATE KEY-----':
          lines = lines[i:]

    publicKey = ''
    for i in range(len(lines)):
      publicKey += lines[i-1:i]
      if len(publicKey) > 24:
        if publicKey[i-24:] == '-----END PUBLIC KEY-----':
          lines = lines[i:]

    identifier = ''
    for i in range(len(lines)):
      identifier += lines[i-1:i]
      if len(identifier) > 33:
        if identifier[i-33:] == '-----END IDENTIFIER SIZE KEY-----':
          lines = lines[i:]
          identifier = identifier[19:-33]

    print(lines, identifier)


    try: 
      keyVerify = Key.objects.get(identifier=identifier)
      count = 0
      identifier2 = identifier
      if keyVerify.privateKey != privateKey or keyVerify.publicKey != publicKey:
        while True:  
          identifier = identifier2 + '_' + str(count)
          keyVerify = Key.objects.get(identifier=identifier)
          count += 1
      else:
        messages.info(request, 'Chave <b>%s</b> já importada.' % (identifier))
        return redirect(keyList)

    except Key.DoesNotExist:
      key = Key.objects.create(user = request.user, identifier = identifier, size = lines, privateKey = privateKey, publicKey = publicKey)
      key.save()
      messages.success(request, 'Chave <b>%s</b> importada com sucesso.' % (identifier))
      return redirect(keyList)
    
  return render(request, 'form.html',
    {'title': 'Importação de Chave',
     'form': form,
     'button': 'Importar'})