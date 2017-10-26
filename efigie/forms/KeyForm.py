#!/usr/bin/python
#-*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _

from efigie.utils import RSA
from efigie.models import Friend, Key, Notification


class KeyForm(ModelForm):
  friends = forms.MultipleChoiceField(
    label = _('Friends with whom you want to share this key'),
    widget=forms.CheckboxSelectMultiple(),
    choices=(),
    required=False)

  def __init__(self, *args, **kwargs):
    self.user = kwargs.pop('user')
    super(KeyForm, self).__init__(*args, **kwargs)
    self.size = self.instance.size
    friends = Friend.objects.get_friends(self.user)
    self.fields['friends'].choices = [(f.id, f.get_full_name()) for f in friends ]

    self.fields['name'].widget.attrs.update({'autofocus': True})
  
  def clean_name(self):
    name = self.cleaned_data['name']
    if Key.objects.filter(name=name, user=self.user).exists():
      raise forms.ValidationError(_('%(model_name)s with this %(field_label)s already exists.') % {
        'model_name': Key._meta.verbose_name,
        'field_label': Key._meta.get_field('name').verbose_name})
    else:
      return name

  def save(self, commit = True):
    key = super(KeyForm, self).save(commit=False)
    key.user = self.user

    new_friends = self.cleaned_data['friends']

    privateKey, publicKey = RSA.generate(int(key.size))
    if commit:
      if self.size == None or self.size != key.size:
        key.privateKey = privateKey
        key.publicKey = publicKey
      key.save()

      # AGARD email
      old_friends = key.friends.all()
      for f in new_friends:
        if f not in old_friends:
          key.friends.add(f)
          notif = Notification(user=f, notification=key, category=Notification.Category.KEY)
          notif.save()

      for f in old_friends:
        if f not in new_friends:
          key.friends.remove(f)
          notif = Notification.objects.filter(user=f,
            notification_type=ContentType.objects.get_for_model(Friend),
            notification_id=key.id,
            category=Notification.Category.KEY)

          notif.delete()

    return key

  class Meta:
    model = Key
    fields = ('name', 'size', 'friends')
