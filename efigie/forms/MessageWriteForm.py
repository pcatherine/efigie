#!/usr/bin/python
#-*- coding: utf-8 -*-

from django import forms
from efigie.forms import *
from efigie.models import Message

class MessageWriteForm(ModelForm):
  file = forms.FileField(label='Image',
    widget=forms.FileInput(attrs={'accept':'image/*'}))

  message = forms.CharField(label=Message._meta.verbose_name,
    required = False,
    widget=forms.Textarea(attrs={'rows': 2}))


  class Meta:
    model = Message
    fields = ('count', )
