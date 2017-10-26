#!/usr/bin/python
#-*- coding: utf-8 -*-

import requests
from io import BytesIO

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.utils.translation import ugettext_lazy as _
from django.views.decorators.csrf import csrf_exempt, csrf_protect

from efigie.utils import invariants, Effigy
from efigie.views.decorators import model_required, breadcrumbs

from efigie import *
from efigie.forms import *
from efigie.models import Message
from efigie.views import *
from efigie.views.message import *

@login_required
@breadcrumbs(['index', 'messageWrite'])
@csrf_protect
def messageWrite(request):
  form = MessageWriteForm(request.POST or None, request.FILES or None, user=request.user)

  url_file = request.POST.get('file_input' or None)
  if url_file != None:
    try:
      r = requests.get(url_file)
      image_file = BytesIO(r.content)
      by_url = True
    except Exception as e:
      by_url = False


  if request.is_ajax():
    res = GoogleAPI.customSearch(imgTheme)

    imgList = []
    for result in res['items']:
      imgList.append({'url': result['link']})
    # print(imgList)
    return JsonResponse({'images': imgList}, status = 200, safe=False)


  if form.is_valid():
    uf = UserEffigy.objects.get(user = request.user)
    image = form.save(uf.settings, f=image_file) if by_url else form.save(uf.settings)

    #AGARD PINTEREST
    return render(request, 'message/write_ok.html',
      {'image': image })

  return render(request, 'message/form_write.html',
    {'form': form,
     'button': _('Encrypt')})
