from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm

from efigie import settings
from efigie.controllers import utils
from efigie.controllers import mail
from efigie.forms import *
from efigie.models import UserVerification

class UserEditForm(UserChangeForm):
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
    super(SetPasswordForm, self).__init__(*args, **kwargs)

  def save(self, url, category, commit=True):
    user = super(UserNewForm, self).save(commit=False)
    user.set_password(self.cleaned_data['password1'])

    if user.first_name != self.cleaned_data['first_name']:
      user.first_name = self.cleaned_data['first_name']

    if user.last_name != self.cleaned_data['last_name']:
      user.last_name = self.cleaned_data['last_name']

    if user.username != self.cleaned_data['username']:
      user.username = self.cleaned_data['username']

    if user.email != self.cleaned_data['email']:
      user.email = self.cleaned_data['email']


    if commit:
      user.save()
      key = utils.generateHashKey(user.username)
      reset = UserVerification(key=key, user=user, category=category)
      reset.save()
      
      subject = '[Efigie] E-mail Confirmation'
      
      message = '''Olá %s, <br/>
      Você está quase lá, apenas um último passo para certificar-se de que temos todas 
      as suas informações. Você entrou como %s, o endereço de e-mail para a sua 
      conta Efigie, durante o processo de inscrição. Se este é você, basta clicar no botão 
      abaixo e sua conta Efigie está pronta para ir.
      ''' % (user.first_name, user.email)

      button = 'Confirmar E-mail'
      context = {'confirmation_url': url+reset.key, 'email':user.email, 'message': message, 'button': button}
      
      mail.sendMailTemplate(subject, context, [user.email])
    return user


  def clean_username(self):
      username = self.cleaned_data['username']
      user = super(UserNewForm, self)
      
      if user.username != username:
        if User.objects.filter(username=username).exists():
          raise forms.ValidationError('Usuário já cadastrado com este username')
        else:
          return username

  def clean_email(self):
    email = self.cleaned_data['email']
    user = super(UserNewForm, self)
    
    if user.email != email:
      if User.objects.filter(email=email).exists():
        raise forms.ValidationError('Usuário já cadastrado com este e-mail')
      else:
        return email

  class Meta:
    model = User
    fields = ("first_name","last_name","username", "email")