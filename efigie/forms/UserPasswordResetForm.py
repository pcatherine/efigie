#!/usr/bin/python
#-*- coding: utf-8 -*-

from django import forms
from efigie.controllers import utils
from efigie.controllers import mail
from efigie.forms import *
from efigie.models import UserConfirmation, Category

class UserPasswordResetForm(forms.Form):
  email = forms.EmailField(
    widget=forms.TextInput(attrs={'placeholder':'E-mail'}))


  def save(self, url):
    user = User.objects.get(email=self.cleaned_data['email'])
    token = utils.generateHashKey(user.username)
    reset = UserConfirmation(token=token, user=user, category=Category.PASSWORD)
    reset.save()
    
    subject = '[Efigie] New Password'
    
    message = '''Olá %s, <br/>
      Você solicitou uma nova senha de acesso para sua conta Efigie. Se você 
      realmente fez essa solicitação clique no botão abaixo e vocé poderá 
      cadastrar uma nova senha para sua conta Efigie.
      ''' % (user.first_name)

    button = 'Cadastrar Nova Senha'


  def clean_email(self):
    email = self.cleaned_data['email']
    if User.objects.filter(email=email).exists():
      raise forms.ValidationError('Nenhum usuário encontrado com este e-mail')
    else:
      return email


    context = {'confirmation_url': url+reset.token, 'email':user.email, 'message': message, 'button': button}
    mail.sendMailTemplate(subject, context, [user.email])