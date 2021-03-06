#!/usr/bin/python
#-*- coding: utf-8 -*-

from django import forms
from django.utils.translation import ugettext_lazy as _

from efigie.forms import *

class KeyImportForm(forms.Form):
  file = forms.FileField(
    label=_("File"),
    widget=forms.FileInput(attrs={'accept':'.key'}))

  def save(self, user, name, size, privateKey, publicKey, commit=True,):
    name = name
    count = 0
    key = None

    while True:
      if not Key.objects.filter(name=name, user=user).exists():
        break
      else:
        keyVerify = Key.objects.get(name=name, user=user)
        if keyVerify.privateKey != privateKey or keyVerify.publicKey != publicKey:
          name = name + '_' + str(count)
          count += 1
        else:
          return None

    if commit:
      key = Key.objects.create(user = user, name = name, size = size, privateKey = privateKey, publicKey = publicKey)
      key.save()
      return key
