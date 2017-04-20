from django import forms
from django.contrib.auth.models import User

from efigie import settings
from efigie.controllers import utils
from efigie.controllers import mail
from efigie.forms import *
from efigie.models import UserVerification, Category

class UserEditForm(forms.Form):
  first_name = forms.CharField( 
    widget=forms.TextInput(attrs={'placeholder':'First Name'}))

  last_name = forms.CharField(
    widget=forms.TextInput(attrs={'placeholder':'Last Name'}))

  username = forms.CharField(
    widget=forms.TextInput(attrs={'placeholder':'Username'}))

  email = forms.EmailField(
    widget=forms.TextInput(attrs={'placeholder':'E-mail'}))


  def __init__(self, *args, **kwargs):
    self.user = kwargs.pop('user')
    super(UserEditForm, self).__init__(*args, **kwargs)
    
    self.fields['first_name'].initial = self.user.first_name 
    self.fields['last_name'].initial = self.user.last_name 
    self.fields['username'].initial = self.user.username 
    self.fields['email'].initial = self.user.email 


  def save(self, url, commit=True):
    self.user.first_name = self.cleaned_data['first_name']
    self.user.last_name = self.cleaned_data['last_name']
    self.user.username = self.cleaned_data['username']
    old_email = self.user.email
    self.user.email = self.cleaned_data['email']

    if commit:
      self.user.save()
      if old_email != self.cleaned_data['email']:
        key = utils.generateHashKey(self.user.username)
        reset = UserVerification(key=key, user=self.user, category=Category.VERIFICATION)
        reset.save()
        
        subject = '[Efigie] E-mail Confirmation'
        
        message = '''Olá %s, <br/>
        Você está quase lá, apenas um último passo para certificar-se de que temos todas 
        as suas informações. Você entrou como %s, <b>NOVO</b> endereço de e-mail para a sua 
        conta Efigie, durante o processo de inscrição. Se este é você, basta clicar no botão 
        abaixo e sua conta Efigie está pronta para ir.
        ''' % (self.user.first_name, self.user.email)

        button = 'Confirmar E-mail'
        context = {'confirmation_url': url+reset.key, 'email':self.user.email, 'message': message, 'button': button}
        
        mail.sendMailTemplate(subject, context, [self.user.email])
    return self.user


  def clean_username(self):
    username = self.cleaned_data['username']
    
    if self.user.username != username and User.objects.filter(username=username).exists():
      raise forms.ValidationError('Usuário já cadastrado com este username')
    else:
      return username

  def clean_email(self):
    email = self.cleaned_data['email']
    
    if self.user.email != email and User.objects.filter(email=email).exists():
      raise forms.ValidationError('Usuário já cadastrado com este e-mail')
    else:
      return email

  class Meta:
    model = User
    fields = ("first_name","last_name","username", "email")