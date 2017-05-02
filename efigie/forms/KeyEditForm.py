from django import forms
from django.forms import ModelForm

from efigie.controllers import RSA
from efigie.forms import KeyForm
from efigie.models import Key


class KeyEditForm(KeyForm):

  def __init__(self, *args, **kwargs):
    self.user = kwargs.pop('user')
    self.key = kwargs.pop('key')
    super(KeyForm, self).__init__(*args, **kwargs)

    self.fields['identifier'].initial = self.key.identifier 
    self.fields['size'].initial = self.key.size 


  def save(self, commit=True):
    user = self.user 
    identifier = self.cleaned_data['identifier']
    size = self.cleaned_data['size']
    privateKey, publicKey = RSA.generate(int(size))
    if commit:
      key = Key.objects.create(user=user, identifier=identifier, size=size, privateKey=privateKey, publicKey=publicKey)
      key.save() 

  class Meta:
    model = Key
    fields = ['identifier', 'size']