#!/usr/bin/python
#-*- coding: utf-8 -*-

from django import forms
from efigie.forms import *

class KeyImportForm(forms.Form):
  keyImport = forms.FileField(
    widget=forms.ClearableFileInput(attrs={'placeholder':'Select a key'}))