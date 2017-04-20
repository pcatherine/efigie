from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from efigie import settings
from efigie.controllers import utils
from efigie.controllers import mail
from efigie.forms import *
from efigie.models import UserConfirmation, Category

class UserNewForm(UserCreationForm):
  first_name = forms.CharField(
    widget=forms.TextInput(attrs={'placeholder':'First Name'}))

  last_name = forms.CharField(
    widget=forms.TextInput(attrs={'placeholder':'Last Name'}))

  username = forms.CharField(
    widget=forms.TextInput(attrs={'placeholder':'Username'}))

  email = forms.EmailField(
    widget=forms.TextInput(attrs={'placeholder':'E-mail'}))

  password1 = forms.CharField(
    widget=forms.PasswordInput(attrs={'placeholder':'Password'}))

  password2 = forms.CharField(
    widget=forms.PasswordInput(attrs={'placeholder':'Re-Password'}))


  def save(self, url, commit=True):
    user = super(UserNewForm, self).save(commit=False)
    user.set_password(self.cleaned_data['password1'])

    if commit:
      user.save()
      key = utils.generateHashKey(user.username)
      reset = UserConfirmation(key=key, user=user, category=Category.VERIFICATION)
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
      if User.objects.filter(username=username).exists():
        raise forms.ValidationError('Usuário já cadastrado com este username')
      else:
        return username


  def clean_email(self):
    email = self.cleaned_data['email']
    if User.objects.filter(email=email).exists():
      raise forms.ValidationError('Usuário já cadastrado com este e-mail')
    else:
      return email


  def clean_password2(self):
    password_length = settings.MIN_PASSWORD_LENGTH
    password1 = self.cleaned_data.get("password1")
    if len(password1) < password_length:
      raise forms.ValidationError("Password must be longer than " "{} characters".format(password_length))
    password2 = self.cleaned_data.get("password2")
    if password1 and password2 and password1 != password2:
      raise forms.ValidationError("The passwords are not equal.")
    return password2


  class Meta:
    model = User
    fields = ("first_name","last_name","username", "email", "password1", "password2")