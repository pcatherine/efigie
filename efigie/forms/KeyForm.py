#!/usr/bin/python
#-*- coding: utf-8 -*-

from django import forms
from django.forms import ModelForm

from efigie.utils import RSA
from efigie.models import Key

SIZE_CHOICES = (
  ('1024', '1024'),
  ('1280', '1280'),
  ('1536', '1536'),
  ('1792', '1792'),

  ('2048', '2048'),
  ('2304', '2304'),
  ('2560', '2560'),
  ('2816', '2816'),

  ('3072', '3072'),
  ('3328', '3328'),
  ('3584', '3584'),
  ('3840', '3840'),

  ('4096', '4096'),
  ('4352', '4352'),
  ('4608', '4608'),
  ('4864', '4864')
)

class KeyForm(ModelForm):
  size = forms.ChoiceField(
    label = Key._meta.get_field('size').verbose_name,
    choices=SIZE_CHOICES
  )

  def __init__(self, *args, **kwargs):
    self.user = kwargs.pop('user')
    super(KeyForm, self).__init__(*args, **kwargs)
    self.size = self.instance.size

  def save(self, commit = True):
    key = super(KeyForm, self).save(commit=False)
    key.user = self.user

    privateKey, publicKey = RSA.generate(int(key.size))
    if commit:
      if self.size == None or self.size != key.size:
        key.privateKey = privateKey
        key.publicKey = publicKey
      key.save()
    return key


  class Meta:
    model = Key
    fields = ('name', 'size')
