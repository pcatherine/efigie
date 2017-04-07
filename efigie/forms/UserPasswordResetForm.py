#!/usr/bin/python
#-*- coding: utf-8 -*-

from django import forms
from efigie.controllers import utils
from efigie.controllers import mail
from efigie.forms import *
from efigie.models import UserVerification

class UserPasswordResetForm(forms.Form):
  email = forms.EmailField(
    widget=forms.TextInput(attrs={'placeholder':'E-mail'}))

  def clean_email(self):
    email = self.cleaned_data['email']
    if User.objects.filter(email=email).exists():
      return email
    else:
      raise forms.ValidationError('Nenhum usuário encontrado com este e-mail')

  def save(self, url, category):
    user = User.objects.get(email=self.cleaned_data['email'])
    key = utils.generateHashKey(user.username)
    reset = UserVerification(key=key, user=user, category=category)
    reset.save()
    template_name = 'user_password_reset_mail.html'
    subject = '[Efigie] New Password'
    context = {'confirmation_url': url+reset.key, 'email':user.email}
    mail.sendMailTemplate(subject, template_name, context, [user.email])
