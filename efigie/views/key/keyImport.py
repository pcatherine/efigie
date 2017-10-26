# !/usr/bin/python
# -*- coding: utf-8 -*-

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.shortcuts import render, redirect
from django.utils.translation import ugettext_lazy as _
from django.views.decorators.csrf import csrf_exempt, csrf_protect

from efigie.utils import invariants
from efigie.views.decorators import model_required, breadcrumbs

from efigie import *
from efigie.forms import *
from efigie.models import Key
from efigie.views import *
from efigie.views.key import *

@login_required
@breadcrumbs(['index', 'keyList', 'keyImport'])
@csrf_protect
def keyImport(request):
  form = KeyImportForm(request.POST or None, request.FILES or None)
  if form.is_valid():
    file = request.FILES['file']
    try:
      date = file.read().decode('utf-8')
      privateKey, publicKey, name, size = date.split(';')

      key = form.save(user=request.user, privateKey=privateKey, publicKey=publicKey, name=name, size=size)
      messages.success(request, _('%(model_key)s <b>%(item_name)s</b> was successfully imported.') % (Key._meta.verbose_name, key.name))
      return redirect(keyList)

    except Exception as e:
      messages.error(request, _('The file could not be imported.'))
      return redirect(keyImport)

  return render(request, 'key/form.html',
    {'form': form,
     'button': _('Import')})
