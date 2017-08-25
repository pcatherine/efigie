#!/usr/bin/python
#-*- coding: utf-8 -*-

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import models
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, render_to_response
from django.template import loader, Context, Template, RequestContext
from django.utils.safestring import mark_safe
from django.views.decorators.csrf import csrf_exempt, csrf_protect

from efigie.forms import *
from efigie.views import *

@login_required
@breadcrumbs(['index', 'messageRead'])
@csrf_protect
def messageRead(request):
  form = MessageReadForm(request.POST or None, request.FILES or None)
  if form.is_valid():
    idMessage, m, s = form.save()
    # AGARD idMessage verificar se a mensagem pode ser lida
    # AGARD s verificar se a mensagem precisa ser descriptografada

    messages.success(request, "%s" % (m))

  return render(request, 'message/form.html',
    {'form': form,
     'button': 'Decrypt'})



  # if request.method == 'POST':
  #   image = request.FILES.get('image', '')
  #   if image =='':
  #     return render_to_response(EffigyParameters.MESSAGE_READ,
  #       {'description': EffigyCommunication.IMAGE_BLANK,
  #       'alert': 'danger'}, context_instance=RequestContext(request))

  #   try:
  #     idMessage, message = Effigy.getEffigy(image)

  #     try:

  #       msg = Message.objects.get(id=idMessage)
  #     except:
  #       msg = None

  #     if msg is not None:
  #       if msg.countRead > 0 or msg.countRead == -1:
  #         if msg.countRead > 0:
  #           msg.countRead -= 1
  #           msg.save()
  #           print("bla 8888888")

  #         return render_to_response(EffigyParameters.MESSAGE_READ,
  #           {'description': message,
  #           'alert': 'success'}, context_instance=RequestContext(request))

  #       else:
  #         return render_to_response(EffigyParameters.MESSAGE_READ,
  #           {'description': EffigyCommunication.MESSAGE_LIMIT,
  #           'alert': 'danger'}, context_instance=RequestContext(request))
  #     else:
  #       return render_to_response(EffigyParameters.MESSAGE_READ,
  #         {'description': EffigyCommunication.MESSAGE_NOT_FOUND,
  #         'alert': 'danger'}, context_instance=RequestContext(request))

  #   except Exception as e:
  #     return render_to_response(EffigyParameters.MESSAGE_READ,
  #       {'description': e,
  #       'alert': 'danger'}, context_instance=RequestContext(request))

  #   return HttpResponse(message)
  # return render(request, EffigyParameters.MESSAGE_READ)
