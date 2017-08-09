#!/usr/bin/python
#-*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from efigie import settings
from efigie.utils import utils
from efigie.utils import mail
from efigie.forms import *
from efigie.models import UserConfirmation, Category

class UserNewForm(UserCreationForm):

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

  def save(self, url, commit=True):
    user = super(UserNewForm, self).save(commit=False)
    user.set_password(self.cleaned_data['password1'])

    if commit:
      user.save()
      token = utils.generateHashKey(user.username)
      reset = UserConfirmation(token=token, user=user, category=Category.VERIFICATION)
      reset.save()

      subject = '[Efigie] E-mail Confirmation'

      message = '''Olá %s, <br/>
      Você está quase lá, apenas um último passo para certificar-se de que temos todas
      as suas informações. Você entrou como %s, o endereço de e-mail para a sua
      conta Efigie, durante o processo de inscrição. Se este é você, basta clicar no botão
      abaixo e sua conta Efigie está pronta para ir.
      ''' % (user.first_name, user.email)

      button = 'Confirmar E-mail'
      context = {'confirmation_url': url+reset.token, 'email':user.email, 'message': message, 'button': button}

      mail.sendMailTemplate(subject, context, [user.email])
    return user

  class Meta:
    model = User
    fields = ("first_name","last_name","username", "email", "password1", "password2")
