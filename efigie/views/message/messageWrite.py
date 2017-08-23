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
from django.shortcuts import render, redirect
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
  form = MessageWriteForm(request.POST or None, request.FILES or None)
  if form.is_valid():
    image = form.save()

    return render(request, 'message/write_ok.html',
      {'image': image })


  return render(request, 'message/form.html',
    {'form': form,
     'button': 'Encrypt'})
