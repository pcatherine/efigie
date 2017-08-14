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
import efigie.config
import json
from efigie.views import *

@login_required
def messageSettings(request):
  # CATHERINE salvar no banco

  # return render(request, EffigyParameters.MESSAGE_SETTINGS)
  return render(request, 'index.html')
