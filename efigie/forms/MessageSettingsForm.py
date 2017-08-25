#!/usr/bin/python
#-*- coding: utf-8 -*-

from django import forms

from efigie.models import UserEffigy

COLORS_CHOICES = (
  ('0', 'Red'),
  ('1', 'Green'),
  ('2', 'Blue'),
)

BITS_CHOICES = (
  ('3', '1'),
  ('4', '2'),
  ('5', '3'),
  ('6', '4'),
  ('7', '5'),
  ('8', '6'),
  ('9', '7'),
  ('10', '8'),
)

PIXEL_CHOICES = (
  ('11', 'Impar'),
  ('12', 'Par'),
)

class MessageSettingsForm(forms.Form):
  colors = forms.MultipleChoiceField(
    required=True,
    widget=forms.CheckboxSelectMultiple,
    choices=COLORS_CHOICES,
  )

  bits = forms.MultipleChoiceField(
    required=True,
    widget=forms.CheckboxSelectMultiple,
    choices=BITS_CHOICES,
  )

  pixel = forms.MultipleChoiceField(
    required=True,
    widget=forms.CheckboxSelectMultiple,
    choices=PIXEL_CHOICES,
  )

  def __init__(self, *args, **kwargs):
    self.user = kwargs.pop('user')
    super(MessageSettingsForm, self).__init__(*args, **kwargs)

    uf = UserEffigy.objects.get(user = self.user)

    colors = []
    for i in range (0,3):
      if uf.settings[i] == '1':
        colors += [i] 
    self.fields['colors'].initial = colors

    bits = []
    for i in range (3,11):
      if uf.settings[i] == '1':
        bits += [i] 
    self.fields['bits'].initial = bits

    pixel = []
    for i in range (11,13):
      if uf.settings[i] == '1':
        pixel += [i] 
    self.fields['pixel'].initial = pixel


  def save(self, commit=True):
    colors = self.cleaned_data['colors']
    bits = self.cleaned_data['bits']
    pixel = self.cleaned_data['pixel']

    # settings's lenght is 17
    # defaut settings 00100000001010000
    settings = list('00000000000000000')

    for x in colors:
      settings[int(x)] = '1'

    for x in bits:
      settings[int(x)] = '1'

    for x in pixel:
      settings[int(x)] = '1'

    uf = UserEffigy.objects.get(user = self.user)
    uf.settings = ''.join(settings)
    uf.save()