#!/usr/bin/python
#-*- coding: utf-8 -*-

from django import forms
from django.forms import ModelForm

from efigie.controllers import RSA
from efigie.forms import KeyNewForm
from efigie.models import Key


class KeyEditForm(KeyNewForm):
  def __init__(self, *args, **kwargs):
    self.user = kwargs.pop('user')
    self.key = kwargs.pop('key')
    super(KeyNewForm, self).__init__(*args, **kwargs)

    self.fields['name'].initial = self.key.name 
    self.fields['size'].initial = self.key.size 

  def save(self, commit=True):
    self.key.name = self.cleaned_data['name']
    old_size = self.key.size
    self.key.size = self.cleaned_data['size']
    if old_size != self.cleaned_data['size']:
      privateKey, publicKey = RSA.generate(int(self.key.size))
      self.key.privateKey = privateKey
      self.key.publicKey = publicKey

    if commit:
      self.key.save() 

  def clean_name(self):
    name = self.cleaned_data['name']

    if self.key.name != name and Key.objects.filter(name=name).exists():
      raise forms.ValidationError('Chave já cadastrado com este identificador.')
    else:
      return name

  class Meta:
    model = Key
    fields = ['name', 'size']
