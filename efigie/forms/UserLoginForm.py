#!/usr/bin/python
#-*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.models import User
from django.utils.text import capfirst

from efigie.forms import *

class UserLoginForm(forms.Form):
  username = forms.CharField(label="%s or %s" % (capfirst(User._meta.get_field('password').verbose_name), capfirst(User._meta.get_field('password').verbose_name))
    widget=forms.TextInput(attrs={'placeholder':'Username or E-mail'}))

  password = forms.CharField(label=capfirst(User._meta.get_field('password').verbose_name),
    widget=forms.PasswordInput())
