#!/usr/bin/python
#-*- coding: utf-8 -*-

from base64 import b64encode
from io import BytesIO

from django import forms
from django.utils.translation import ugettext_lazy as _

from efigie.forms import *
from efigie.models import Message, Key
from efigie.utils import Effigy, RSA

class MessageWriteForm(ModelForm):

  count = forms.IntegerField(label=_('Times the message can be read'),
    required=False)

  file = forms.FileField(label=_('Image'),
    widget=forms.FileInput(attrs={'accept':'image/*'}),
    required=False)

  key = forms.ModelChoiceField(label=_('RSA key to encrypt the message'),
    queryset=None,
    required=False)

  message = forms.CharField(label=Message._meta.verbose_name,
    widget=forms.Textarea(attrs={'rows': 2}))


  def __init__(self, *args, **kwargs):
    self.user = kwargs.pop('user')
    super(MessageWriteForm, self).__init__(*args, **kwargs)
    self.fields['key'].queryset = Key.objects.filter(friends=self.user)


  def save(self, settings, commit=True, f=None):
    count = self.cleaned_data['count']
    file = f if f != None else self.cleaned_data['file']
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
    fields = '__all__'
