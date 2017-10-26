#!/usr/bin/python
#-*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.text import capfirst
from django.utils.translation import ugettext_lazy as _

from efigie import settings
from efigie.utils import utils, mail
from efigie.forms import *
from efigie.models import UserConfirmation, UserEffigy

class UserNewForm(UserCreationForm):

  username = forms.CharField(label='Username')
  email = forms.EmailField(label=capfirst(User._meta.get_field('email').verbose_name))

  def clean_email(self):
    email = self.cleaned_data['email']
    if User.objects.filter(email=email).exists():
      raise forms.ValidationError(_('%(model_name)s with this %(field_label)s already exists.') % {
        'model_name': capfirst(User._meta.verbose_name),
        'field_label': User._meta.get_field('email').verbose_name})
    else:
      return email

  def __init__(self, *args, **kwargs):
    super(UserNewForm, self).__init__(*args, **kwargs)
    self.fields['first_name'].widget.attrs.update({'autofocus': True})
    self.fields['username'].widget.attrs.update({'autofocus': False})


  def save(self, url, commit=True):
    user = super(UserNewForm, self).save(commit=False)
    user.set_password(self.cleaned_data['password1'])

    if commit:
      user.save()
      token = utils.generateHashKey(user.username)
      reset = UserConfirmation(token=token, user=user, category=UserConfirmation.Category.VERIFICATION)
      reset.save()

      uf = UserEffigy(user = user, settings='00100000001010000')
      uf.save()

      # AGARD email
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
