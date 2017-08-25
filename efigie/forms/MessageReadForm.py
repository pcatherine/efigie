#!/usr/bin/python
#-*- coding: utf-8 -*-

from django import forms
from efigie.forms import *
from efigie.models import Message

from efigie.utils import Effigy

class MessageReadForm(forms.Form):
  file = forms.FileField(label='Image',
    widget=forms.FileInput(attrs={'accept':'image/*'}))

  def save(self, commit=True):
    file = self.cleaned_data['file']

    return Effigy.getEffigy(file)

  class Meta:
    model = Message
    fields = ('count', )
