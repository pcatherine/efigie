from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from efigie import settings

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

  def save(self, commit=True):
    user = super(UserNewForm, self).save(commit=False)
    user.set_password(self.cleaned_data['password1'])
    if commit:
      user.save()
    return user

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