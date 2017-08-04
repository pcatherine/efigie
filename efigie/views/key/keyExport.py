#!/usr/bin/python
#-*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.cache import never_cache

from efigie.views.decorators import model_required

from efigie import *
from efigie.models import Key
from efigie.views import *
from efigie.views.key import *


@login_required
@model_required(Key, 'keyList', user = True)
@never_cache
def keyExport(request, keyId):
  key = Key.objects.get(id = keyId, user = request.user)
  response = HttpResponse(content_type='application/text')
  response['Content-Disposition'] = 'attachment; filename="%s.key"' % (key.name)
  response.write('%s;%s;%s;%d' % (key.privateKey, key.publicKey, key.name, key.size))
  return response
