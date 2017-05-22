#!/usr/bin/python
#-*- coding: utf-8 -*-

from django import forms
from efigie.forms import *

class KeyImportForm(forms.Form):
  file = forms.FileField(
    widget=forms.FileInput(attrs={'accept':'.key'}))
  
  def save(self, user, identifier, size, privateKey, publicKey, commit=True,):
    name = identifier
    count = 0
    key = None

    while True:
      if not Key.objects.filter(identifier=name).exists():
        break
      else: 
        keyVerify = Key.objects.get(identifier=name)
        if keyVerify.privateKey != privateKey or keyVerify.publicKey != publicKey:
          name = identifier + '_' + str(count)
          count += 1
        else:
          return False, ''

    if commit:
      key = Key.objects.create(user = user, identifier = name, size = size, privateKey = privateKey, publicKey = publicKey)
      key.save()
      return True, name