#!/usr/bin/python
#-*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.models import User
from django.utils.text import capfirst
from django.utils.translation import ugettext_lazy as _

from efigie.forms import *

class UserLoginForm(forms.Form):
  username = forms.CharField(
    label = _("Username or Email Address"))

  password = forms.CharField(label=capfirst(User._meta.get_field('password').verbose_name),
    widget=forms.PasswordInput())

  def __init__(self, *args, **kwargs):
    super(UserLoginForm, self).__init__(*args, **kwargs)
    self.fields['username'].widget.attrs.update({'autofocus': True})
