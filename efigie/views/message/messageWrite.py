#!/usr/bin/python
#-*- coding: utf-8 -*-

# from django.contrib.auth.decorators import login_required
# from django.db import models
# from django.http import HttpResponse, HttpResponseRedirect
# from django.shortcuts import render, redirect, render_to_response
# from django.template import loader, Context, Template, RequestContext
# from django.utils.safestring import mark_safe

# # from django.core.servers.basehttp import FileWrapper

# # from efigie.models import UserEfigie, Message, Key, Friend
# # from efigie.controller import EffigyParameters, EffigyCommunication
# import efigie.config
# import json
# from efigie.views import *

#!/usr/bin/python
#-*- coding: utf-8 -*-

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt, csrf_protect

from efigie.utils import invariants
from efigie.views.decorators import model_required, breadcrumbs

from efigie import *
from efigie.forms import *
from efigie.models import Message
from efigie.views import *
from efigie.views.message import *

@login_required
@breadcrumbs(['index', 'messageWrite'])
def messageWrite(request):
  form = MessageWriteForm(request.POST or None, request.FILES or None)
  if form.is_valid():
    file = request.FILES['file']
    try:
      imageEfigie = Effigy.setEffigy(image, '000000000000000', message, "", msg.id)

      # date = file.read().decode('utf-8')
      # privateKey, publicKey, name, size = date.split(';')

      # key = form.save(user=request.user, privateKey=privateKey, publicKey=publicKey, name=name, size=size)
      # #AGARD trans
      # messages.info(request, 'Chave <b>%s</b> já importada.' % (key.name))
      # return redirect(keyImport)

    except Exception as e:
      messages.error(request, 'O arquivo não pode ser importado.')
      return redirect(keyImport)

  return render(request, 'form.html',
    {'form': form,
     'button': 'Encrypt'})


  # return render(request, "index.html")

  # if request.method == 'POST':
  #   message = request.POST.get('message', '')
  #   image   = request.FILES.get('image', '')
  #   count   = request.POST.get('count', '')

    # if count != '':
    #   try:
    #     if int(count) <= 0:
    #       message.error()
    #       return render(request, 'message/write.html')
    #       return render_to_response(EffigyParameters.MESSAGE_WRITE,
    #         {'description': EffigyCommunication.MESSAGE_BLANK_SIZE,
    #         'alert': 'danger',
    #         'message' : message,
    #         'count': count}, context_instance=RequestContext(request))
    #   except:
    #     return render_to_response(EffigyParameters.MESSAGE_WRITE,
    #       {'description': EffigyCommunication.MESSAGE_BLANK_SIZE,
    #       'alert': 'danger',
    #       'message' : message,
    #       'count': count}, context_instance=RequestContext(request))

  #   descriptionErr = ''
  #   inputEmpty = []

  #   if message == '':
  #     return render_to_response(EffigyParameters.MESSAGE_WRITE,
  #       {'description': EffigyCommunication.MESSAGE_BLANK,
  #       'alert': 'danger'}, context_instance=RequestContext(request))


  #   if len(inputEmpty) == 1:
  #     descriptionErr += inputEmpty[0]
  #     descriptionErr += EffigyCommunication.IS_BLANK + EffigyCommunication.SPACE

  #   elif len(inputEmpty) > 1:
  #     descriptionErr += inputEmpty[0]
  #     descriptionErr += EffigyCommunication.AND + EffigyCommunication.SPACE
  #     descriptionErr += inputEmpty[1]
  #     descriptionErr += EffigyCommunication.ARE_BLANK

  #     if descriptionErr != '':
  #       return render_to_response(EffigyParameters.MESSAGE_WRITE,
  #         {'description': descriptionErr,
  #         'alert': 'danger',
  #         'message' : message,
  #         'count': count}, context_instance=RequestContext(request))

  #   request.session['msgText'] = message
  #   request.session['msgCount'] = count
  #   if 'msgWrite' in request.session :
  #     del request.session['msgWrite']

  #   if image  == '':
  #     return imageSearch(request, 'info', EffigyCommunication.MESSAGE_SEARCH)

  #   userEfigie = UserEfigie.objects.get(user = request.user)

  #   return messageSet(request, image)
  # return render(request, EffigyParameters.MESSAGE_WRITE)
