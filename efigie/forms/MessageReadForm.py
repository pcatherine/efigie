#!/usr/bin/python
#-*- coding: utf-8 -*-

from django import forms
from efigie.forms import *
from efigie.models import Message

from efigie.utils import Effigy, RSA


class MessageReadForm(forms.Form):
  file = forms.FileField(label='Image',
    widget=forms.FileInput(attrs={'accept':'image/*'}))

  # AGARD FILTRAR POR AMIGO
  key = forms.ModelChoiceField(label='RSA key to encrypt the message',
    queryset=Key.objects.all(),
    required=False)

  # def __init__(self, *args, **kwargs):
  #   self.user = kwargs.pop('user')
  #   super(MessageWriteForm, self).__init__(*args, **kwargs)
  #   # AGARD receber o usuário e set key by friend

  def save(self, commit=True):
    file = self.cleaned_data['file']
    key = self.cleaned_data['key']

    try:
      i, m, s = Effigy.getEffigy(file)
    except Exception as e:
      print(e)

    if s[13] == '1' and key == None:
      raise forms.ValidationError('RSA key is required in this case.')
    elif s[13] == '1' and key != None:
      try:
        m = RSA.decrypt(key.privateKey, m)
      except ValueError as e:
        raise ValueError("RSA key didn't match.")
      except:
        raise Exception('Unknown error.')

    return i, m, s

  class Meta:
    model = Message
    fields = ('count', )
