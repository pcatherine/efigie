#!/usr/bin/python
#-*- coding: utf-8 -*-
#OKAY
__author__ = "Paolla Catherine"
__copyright__ = "Copyright 2015-2016, Efigie"
__credits__ = ["Paolla Catherine"]
__version__ = "1.0.0"
__email__ = "paollacath@gmail.com"
__status__ = "Production"

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
    response.write('%s%sIDENTIFIER KEY-----%s-----END IDENTIFIER SIZE KEY-----%d' % (key.privateKey, key.publicKey, key.identifier, key.size))
    return response

  except Exception as e:
    return keyList(request, alert=EffigyParameters.ALERT_DANGER, description=EffigyCommunication.KEY_NOT_EXPORT)