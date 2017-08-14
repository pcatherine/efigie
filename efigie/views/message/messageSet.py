#!/usr/bin/python
#-*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, render_to_response
from django.template import loader, Context, Template, RequestContext

# from efigie.controller import Effigy, EffigyParameters, EffigyCommunication
from efigie.models import Message, Key
from efigie.views import *

# import urllib, cStringIO

@login_required
def messageSet(request):

# def messageSet(request, image):
  # message = request.session['msgText']
  # count = request.session['msgCount']
  # del request.session['msgText']
  # del request.session['msgCount']

  # if 'msgImgList' and 'msgWrite' in request.session:
  #   imgList = request.session['msgImgList']
  #   del request.session['msgImgList']
  #   del request.session['msgWrite']
  #   image = cStringIO.StringIO(urllib.urlopen(imgList[int(image)]['url']).read())

  # if count == '':
  #   msg = Message.objects.create(countRead = -1)
  # else:
  #   msg = Message.objects.create(countRead = int(count))

  # msg.save()
  # userEfigie = UserEfigie.objects.get(user = request.user)

  # try:
  #   imageEfigie = Effigy.setEffigy(image, userEfigie.settings, message, "", msg.id)
  #   response = HttpResponse(content_type="image/png")
  #   imageEfigie.save(response, "PNG")
  #   imageBase64 = response.getvalue().encode("base64")
  #   response.close()
  #   return render_to_response(EffigyParameters.MESSAGE_WRITE_OK,
  #     {'image': imageBase64 }, context_instance=RequestContext(request))

  # except Exception as e:
  #   return render_to_response(EffigyParameters.MESSAGE_WRITE,
  #     {'description': e,
  #     'alert': EffigyParameters.ALERT_DANGER,
  #     'message' : message,
  #     'count': count}, context_instance=RequestContext(request))

  return render(request, 'index.html')

