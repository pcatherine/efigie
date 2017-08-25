#!/usr/bin/python
#-*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.text import capfirst

from efigie import settings
from efigie.utils import utils
from efigie.utils import mail
from efigie.forms import *
from efigie.models import UserConfirmation, Category

class UserNewForm(UserCreationForm):

  email = forms.EmailField(label=capfirst(User._meta.get_field('email').verbose_name))

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

  def save(self, url, commit=True):
    user = super(UserNewForm, self).save(commit=False)
    user.set_password(self.cleaned_data['password1'])

    if commit:
      user.save()
      token = utils.generateHashKey(user.username)
      reset = UserConfirmation(token=token, user=user, category=Category.VERIFICATION)
      reset.save()

      uf = UserEffigy(user = self.user, settings='00100000001010000')
      uf.save()

      subject = '[Efigie] E-mail Confirmation'

      message = '''Olá %s, <br/>
      Você está quase lá, apenas um último passo para certificar-se de que temos todas
      as suas informações. Você entrou como %s, o endereço de e-mail para a sua
      conta Efigie, durante o processo de inscrição. Se este é você, basta clicar no botão
      abaixo e sua conta Efigie está pronta para ir.
      ''' % (user.first_name, user.email)

      button = 'Confirmar E-mail'
      context = {'confirmation_url': url+reset.token,
        'email':user.email,
        'message': message,
        'button': button,
        'name': user.first_name}

      mail.sendMailTemplate(subject, context, [user.email])
    return user

  class Meta:
    model = User
    fields = ("first_name","last_name","username", "email", "password1", "password2")
