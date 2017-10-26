#!/usr/bin/python
#-*- coding: utf-8 -*-

from django import forms
from django.utils.translation import ugettext_lazy as _

from efigie.forms import *
from efigie.models import Message
from efigie.utils import Effigy, invariants, RSA


class MessageReadForm(forms.Form):
  file = forms.FileField(label=_('Image'),
    widget=forms.FileInput(attrs={'accept':'image/*'}))

  key = forms.ModelChoiceField(label=_('RSA Key to encrypt the message'),
    queryset=None,
    required=False)

  def __init__(self, *args, **kwargs):
    self.user = kwargs.pop('user')
    super(MessageReadForm, self).__init__(*args, **kwargs)

    self.fields['key'].queryset = Key.objects.filter(user=self.user).exclude(friends=None)


  def save(self, commit=True):
    file = self.cleaned_data['file']
    key = self.cleaned_data['key']

    try:
      i, m, s = Effigy.getEffigy(file)
    except Exception as e:
      print(e)

    if s[13] == '1' and key == None:
      raise forms.ValidationError(_('RSA key is required in this case.'))
    elif s[13] == '1' and key != None:
      try:
        m = RSA.decrypt(key.privateKey, m)
      except ValueError as e:
        raise ValueError(_("RSA key didn't match."))
      except:
        raise Exception(invariants.unknown_error)

    return i, m, s

  class Meta:
    model = Message
    fields = ('count', )
