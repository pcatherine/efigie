#!/usr/bin/python
#-*- coding: utf-8 -*-

from django import forms
from django.utils.text import capfirst

from efigie.utils import mail, utils
from efigie.forms import *
from efigie.models import UserConfirmation
from efigie.utils import invariants



class UserPasswordResetForm(forms.Form):
  email = forms.EmailField(label=capfirst(User._meta.get_field('email').verbose_name))

  def clean_email(self):
    email = self.cleaned_data['email']
    if not User.objects.filter(email=email).exists():
      raise forms.ValidationError(invariants.alert_not_found_error % {
        'model_name': capfirst(User._meta.verbose_name)})
    else:
      return email

  def __init__(self, *args, **kwargs):
    super(UserPasswordResetForm, self).__init__(*args, **kwargs)
    self.fields['email'].widget.attrs.update({'autofocus': True})

  def save(self, url):
    user = User.objects.get(email=self.cleaned_data['email'])
    token = utils.generateHashKey(user.username)
    reset = UserConfirmation(token=token, user=user, category=UserConfirmation.Category.PASSWORD)
    reset.save()

    # AGARD email
    subject = '[Efigie] New Password'

    message = '''Olá %s, <br/>
      Você solicitou uma nova senha de acesso para sua conta Efigie. Se você
      realmente fez essa solicitação clique no botão abaixo e vocé poderá
      cadastrar uma nova senha para sua conta Efigie.
      ''' % (user.first_name)

    button = 'Cadastrar Nova Senha'

    context = {'confirmation_url': url+reset.token,
      'email':user.email,
      'message': message,
      'button': button,
      'name': user.first_name}

    mail.sendMailTemplate(subject, context, [user.email])
