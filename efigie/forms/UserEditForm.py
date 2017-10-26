#!/usr/bin/python
#-*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import ugettext_lazy as _

from efigie import settings
from efigie.utils import mail, utils
from efigie.forms import *
from efigie.models import UserConfirmation

class UserEditForm(forms.Form):
  first_name = forms.CharField(
    label=capfirst(User._meta.get_field('first_name').verbose_name),
    widget=forms.TextInput())

  last_name = forms.CharField(
    label=capfirst(User._meta.get_field('last_name').verbose_name),
    widget=forms.TextInput())

  username = forms.CharField(
    label='Username',
    widget=forms.TextInput())

  email = forms.EmailField(
    label=capfirst(User._meta.get_field('email').verbose_name),
    widget=forms.TextInput())


  def clean_username(self):
    username = self.cleaned_data['username']
    if User.objects.filter(username=username).exists() and username != self.user.username:
      raise forms.ValidationError(_('%(model_name)s with this %(field_label)s already exists.') % {
        'model_name': capfirst(User._meta.verbose_name),
        'field_label': User._meta.get_field('email').verbose_name})
    else:
      return username

  def clean_email(self):
    email = self.cleaned_data['email']
    if User.objects.filter(email=email).exists() and email != self.user.email:
      raise forms.ValidationError(_('%(model_name)s with this %(field_label)s already exists.') % {
        'model_name': capfirst(User._meta.verbose_name),
        'field_label': User._meta.get_field('email').verbose_name})
    else:
      return email


  def __init__(self, *args, **kwargs):
    self.user = kwargs.pop('user')
    super(UserEditForm, self).__init__(*args, **kwargs)

    self.fields['first_name'].initial = self.user.first_name
    self.fields['last_name'].initial = self.user.last_name
    self.fields['username'].initial = self.user.username
    self.fields['email'].initial = self.user.email

    # self.fields['first_name'].widget.attrs.update({'autofocus': True})


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
        reset = UserConfirmation(key=key, user=self.user, category=UserConfirmation.Category.VERIFICATION)
        reset.save()
        # AGARD arrumar os emails
        subject = '[Efigie] E-mail Confirmation'

        message = '''Olá %s, <br/>
        Você está quase lá, apenas um último passo para certificar-se de que temos todas
        as suas informações. Você entrou como %s, <b>NOVO</b> endereço de e-mail para a sua
        conta Efigie, durante o processo de inscrição. Se este é você, basta clicar no botão
        abaixo e sua conta Efigie está pronta para ir.
        ''' % (self.user.first_name, self.user.email)

        button = 'Confirmar E-mail'
        context = {'confirmation_url': url+reset.key,
          'email':self.user.email,
          'message': message,
          'button': button,
          'name': self.user.email}

        mail.sendMailTemplate(subject, context, [self.user.email])
    return self.user
