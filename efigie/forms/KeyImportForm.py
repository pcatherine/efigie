#!/usr/bin/python
#-*- coding: utf-8 -*-

from django import forms
from efigie.forms import *

class KeyImportForm(forms.Form):
  file = forms.FileField(
    widget=forms.FileInput(attrs={'accept':'.key'}))
  # file = forms.ContentTypeRestrictedFileField()
    # widget=forms.ClearableFileInput(attrs={'placeholder':'Select a key'}))

  # def __init__(self, *args, **kwargs):
  #   self.user = kwargs.pop('user')
  #   super(KeyImportForm, self).__init__(*args, **kwargs)

  # # def __init__(self, post_data, files_data):
  # #   self.file = files_data.get('file', None)
  # #   return super(KeyImportForm, self).__init__(post_data, files_data)

  # # def save(self, *args, **kwargs):
  # #   deck = super(DeckCreateForm, self).save(*args, **kwargs)
  # #   self.handle_csv_file(self.csv_file, deck)
  # #   return deck


  # def clean_file(self):
  #   super(KeyImportForm, self).clean()
  #   upload_to = '/some/path'
  #   upload_to += self.cleaned_data['file'].name