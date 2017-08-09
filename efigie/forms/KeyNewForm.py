#!/usr/bin/python
#-*- coding: utf-8 -*-

from django import forms
from django.forms import ModelForm

from efigie.controllers import RSA
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

class KeyNewForm(ModelForm):
  name = forms.CharField( 
    widget=forms.TextInput(attrs={'placeholder':'name'}))

  size = forms.ChoiceField(
        widget=forms.Select(attrs={'placeholder': 'Size'}),
        choices=SIZE_CHOICES,
    )

  def __init__(self, *args, **kwargs):
    self.user = kwargs.pop('user')
    super(KeyNewForm, self).__init__(*args, **kwargs)

  def save(self, commit=True):
    user = self.user 
    key = super(KeyNewForm, self).save(commit=False)

    privateKey, publicKey = RSA.generate(int(size))
    if commit:
      key = Key.objects.create(user=user, name=name, size=size, privateKey=privateKey, publicKey=publicKey)
      key.save() 

  def clean_name(self):
    name = self.cleaned_data['name']
    if Key.objects.filter(name=name).exists():
      raise forms.ValidationError('Chave já cadastrado com este identificador.')
    else:
      return name

  class Meta:
    model = Key
    fields = ('name', 'size')
