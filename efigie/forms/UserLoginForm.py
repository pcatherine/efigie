#!/usr/bin/python
#-*- coding: utf-8 -*-

from django import forms
from efigie.forms import *

class UserLoginForm(forms.Form):

  username = forms.CharField(
    widget=forms.TextInput(attrs={'placeholder':'Username or E-mail'}))
  
  password = forms.CharField(
    widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
