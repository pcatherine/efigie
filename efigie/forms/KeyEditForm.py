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

  def clean_identifier(self):
    identifier = self.cleaned_data['identifier']

    if self.key.identifier != identifier and Key.objects.filter(identifier=identifier).exists():
      raise forms.ValidationError('Chave já cadastrado com este identificador.')
    else:
      return identifier

  def save(self, commit=True):
    self.key.identifier = self.cleaned_data['identifier']
    old_size = self.key.size
    self.key.size = self.cleaned_data['size']
    if old_size != self.cleaned_data['size']:
      privateKey, publicKey = RSA.generate(int(self.key.size))
      self.key.privateKey = privateKey
      self.key.publicKey = publicKey

    if commit:
      self.key.save() 

  class Meta:
    model = Key
    fields = ['identifier', 'size']