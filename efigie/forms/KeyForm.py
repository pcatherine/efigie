from django.forms import ModelForm
from efigie.models import Key

class KeyForm(ModelForm):

  def __init__(self, *args, **kwargs):
    self.user = kwargs.pop('user')
    super(KeyForm, self).__init__(*args, **kwargs)

  def clean_identifier(self):
    identifier = self.cleaned_data['identifier']
    if Key.objects.filter(identifier=identifier).exists():
      raise forms.ValidationError('Chave já cadastrado com este identificador.')
    else:
      return identifier

  class Meta:
    model = Key
    fields = ['identifier', 'size']