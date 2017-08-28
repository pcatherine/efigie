#!/usr/bin/python
#-*- coding: utf-8 -*-

from base64 import b64encode
from io import BytesIO

from django import forms

from efigie.forms import *
from efigie.models import Message, Key
from efigie.utils import Effigy, RSA

class MessageWriteForm(ModelForm):
  count = forms.IntegerField(label='Times the message can be read',
    required=False)

  file = forms.FileField(label='Image',
    widget=forms.FileInput(attrs={'accept':'image/*'}))

  # AGARD FILTRAR POR AMIGO
  key = forms.ModelChoiceField(label='RSA key to encrypt the message',
    queryset=Key.objects.all(),
    required=False)

  message = forms.CharField(label=Message._meta.verbose_name,
    widget=forms.Textarea(attrs={'rows': 2}))


  def __init__(self, *args, **kwargs):
    self.user = kwargs.pop('user')
    super(MessageWriteForm, self).__init__(*args, **kwargs)
    # AGARD receber o usuário e set key by friend


  def save(self, settings, commit=True):
    count = self.cleaned_data['count']
    file = self.cleaned_data['file']
    message = self.cleaned_data['message']
    key = self.cleaned_data['key']

    msg = Message(count=(-1 if count == None else count))
    msg.save()

    if key != None:
      s = list(settings)
      s[13] = '1'
      settings = ''.join(s)
      message = RSA.encrypt(key.publicKey, message).decode('utf-8')

    imageEfigie = Effigy.setEffigy(file, settings, message, msg.id)

    b = BytesIO()
    imageEfigie.save(b, format="PNG")
    img_str = b64encode(b.getvalue())

    return img_str

  class Meta:
    model = Message
    fields = ('count', )
