from django import forms
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm

from efigie import settings

class UserPasswordChangeForm(PasswordChangeForm):
  old_password = forms.CharField(
    widget=forms.PasswordInput(attrs={'placeholder': 'Current password'}))
  new_password1 = forms.CharField(
    widget=forms.PasswordInput(attrs={'placeholder': 'New password'}))
  new_password2 = forms.CharField(
    widget=forms.PasswordInput(attrs={'placeholder': 'Password again'}))


  # def __init__(self, *args, **kwargs):
  #   self.instance = kwargs.pop('instance', None)
  #   assert self.instance is not None
  #   super(PasswordChangeForm, self).__init__(*args, **kwargs)
    
  #   # self.user = kwargs.pop('user')
  #   # super(PasswordChangeForm, self).__init__(*args, **kwargs)


  def clean_new_password2(self):
    password_length = settings.MIN_PASSWORD_LENGTH
    new_password1 = self.cleaned_data.get("new_password1")
    if len(new_password1) < password_length:
      raise forms.ValidationError("Password must be longer than " "{} characters".format(password_length))
    new_password2 = self.cleaned_data.get("new_password2")
    if new_password1 and new_password2 and new_password1 != new_password2:
      raise forms.ValidationError("The passwords are not equal.")
    return new_password2





  class Meta:
    fields = ("old_password","new_password1","new_password2")