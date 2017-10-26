#!/usr/bin/python
#-*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect

from efigie.utils import GoogleAPI
from efigie.views import *

#CATHERINE verificar o tamanho correto das coisas
@login_required
def imageSearch(request):
  imgTheme = request.POST.get('imgTheme', '')
  if imgTheme != '':
    res = GoogleAPI.customSearch(imgTheme)

    imgList = []
    for result in res['items']:
      imgList.append({'idx':res['items'].index(result), 'url':result['link']})


    return render(request, 'message/image_search.html',
      {'imgList': imgList})

  return render(request, 'message/image_search.html')
