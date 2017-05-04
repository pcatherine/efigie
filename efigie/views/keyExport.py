#!/usr/bin/python
#-*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect

from efigie import *
from efigie.models import Key
from efigie.views import *

@login_required
def keyExport(request, keyId):
  try:
    key = Key.objects.get(id=keyId) 
    response = HttpResponse(content_type='application/text')
    response['Content-Disposition'] = 'attachment; filename="%s.key"' % (key.identifier)
    response.write('%s;%s;%s;%d' % (key.privateKey, key.publicKey, key.identifier, key.size))
    return response

  except Exception as e:
    messages.error(request, 'Chave não pode ser exportada.')
    return redirect(keyList)