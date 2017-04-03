# #-*- coding: utf-8 -*-
# from django.views.decorators.cache import never_cache
# from django.views.decorators.csrf import csrf_protect

# from django.contrib.auth.decorators import login_required
# from django.conf import settings
# from django.contrib.auth import authenticate, login, logout
# from django.core.context_processors import csrf
# from django.core.files.base import ContentFile
# from django.core.files.storage import default_storage
# from django.core.mail import send_mail
# from django.core.urlresolvers import reverse

# from django.db import models
# from django.http import HttpResponse, HttpResponseRedirect
# from django.shortcuts import render, redirect, render_to_response
# from django.template import loader, Context, Template, RequestContext
# from django.utils.safestring import mark_safe
# from django.utils import translation


# # from efigie.controller.Encryption import RSA
# # from efigie.controller.Util import *
# from efigie.controller import EffigyParameters, EffigyCommunication, GoogleAPI


# from efigie.models import *

# import qrcode
# from qrcode.image.pure import PymagingImage

# import PIL
# from PIL import ImageFont, Image, ImageDraw

# import requests
# import re
# import urllib2
# import os

# import gettext 
# import locale
# import os
# from efigie.views import *

# @never_cache
# @csrf_protect
# def userLogin(request, alert='', description='', username = ''):
#   if request.user.is_authenticated():
#     return redirect('/')

#   if request.method == 'POST':
#     username  = request.POST.get('username', '')
#     password = request.POST.get('password', '')

#     if username != '' and password != '':
#       if '@' in username:
#         try: 
#           userOb = User.objects.get(email=username)
#           if UserEfigie.objects.get(user=userOb).customer_support_email is None:
#             return render_to_response(EffigyParameters.USER_LOGIN,  
#               {'alert': EffigyParameters.ALERT_DANGER,
#               'description':  EffigyCommunication.USER_CONFIRMATION, 
#               'username': username}, context_instance=RequestContext(request))
#           else:
#             user = authenticate(username=userOb.username, password=password)
#         except:
#           return render_to_response(EffigyParameters.USER_LOGIN,  
#             {'alert': EffigyParameters.ALERT_DANGER,
#             'description':  EffigyCommunication.USER_NOT_FOUND, 
#             'username': username}, context_instance=RequestContext(request))
#       else:
#         try:
#           userOb = User.objects.get(username=username)
#           if UserEfigie.objects.get(user=userOb).customer_support_email is None:
#             return render_to_response(EffigyParameters.USER_LOGIN,  
#               {'alert': EffigyParameters.ALERT_INFO,
#               'description':  EffigyCommunication.USER_CONFIRMATION, 
#               'username': username}, context_instance=RequestContext(request))
#           user = authenticate(username=username, password=password)
#         except:
#           return render_to_response(EffigyParameters.USER_LOGIN,  
#             {'alert': EffigyParameters.ALERT_DANGER,
#             'description':  EffigyCommunication.USER_NOT_FOUND, 
#             'username': username}, context_instance=RequestContext(request))


#       if user is not None:
#         if user.is_active:
#           userEfigie = UserEfigie.objects.get(user = user)
#           if userEfigie.googleAuthenticator == '':
#             login(request, user)
#             return redirect('/')
#           else:
#             request.session['user'] = user.username
#             return redirect('/login2')
#         else:
#           return render_to_response(EffigyParameters.USER_LOGIN,  
#             {'alert': EffigyParameters.ALERT_DANGER,
#             'description':  EffigyCommunication.USER_NOT_FOUND, 
#             'username': username}, context_instance=RequestContext(request))
#       else:
#         return render_to_response(EffigyParameters.USER_LOGIN,  
#           {'alert': EffigyParameters.ALERT_DANGER,
#           'description':  EffigyCommunication.USER_INVALID, 
#           'username': username}, context_instance=RequestContext(request))
     
#   return render_to_response(EffigyParameters.USER_LOGIN,  
#     {'alert': alert,
#     'description': description, 
#     'username': username}, context_instance=RequestContext(request))


from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect

from efigie.controllers import *
from efigie.views import *
from efigie.forms import *


@never_cache
@csrf_protect
def userLogin(request, alert='', description=''):
  if request.user.is_authenticated():
    return index(request)

  form = UserLoginForm(request.POST or None)
  if form.is_valid():
    username = form.cleaned_data['username']
    password = form.cleaned_data['password']

    if '@' in username:
      try:
        user = User.objects.get(email=username)
        user = authenticate(username=user.username, password=password)
      except Exception as e:
        alert = 'danger'
        description = 'Username ou senha inválido.'
    else:
      user = authenticate(username=username, password=password)
      if user is not None:
        login(request, user)
        return index(request)
      else: 
        alert = 'danger'
        description = 'Username ou senha inválido.'

  return render(request, 'user_login.html', 
    {'form': form, 
     'alert': 'danger',
     'description': 'description'})