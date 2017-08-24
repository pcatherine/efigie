#!/usr/bin/python
#-*- coding: utf-8 -*-

import base64
from io import BytesIO

from django import forms

from efigie.forms import *
from efigie.models import Message
from efigie.utils import Effigy

class MessageWriteForm(ModelForm):
  count = forms.IntegerField(label='How many times the message can be read')

  file = forms.FileField(label='Image',
    widget=forms.FileInput(attrs={'accept':'image/*'}))

  message = forms.CharField(label=Message._meta.verbose_name,
    widget=forms.Textarea(attrs={'rows': 2}))


  def save(self, commit=True):
    count = self.cleaned_data['count']
    file = self.cleaned_data['file']
    message = self.cleaned_data['message']

    imageEfigie = Effigy.setEffigy(file, '00100000001010000', message, "", 1)

    b = BytesIO()
    imageEfigie.save(b, format="PNG")
    img_str = base64.b64encode(b.getvalue())

    return img_str

  class Meta:
    model = Message
    fields = ('count', )
