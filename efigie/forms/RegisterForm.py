from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from efigie.models import UserPasswordReset
from efigie.controllers.utils import generate_hash_key
from efigie.controllers.mail import send_mail_template


class RegisterForm(forms.ModelForm):

  #email = forms.EmailField(label='E-mail')
  password1 = forms.CharField(label='Senha', widget=forms.PasswordInput)
  password2 = forms.CharField(label='Confirme sua Senha', widget=forms.PasswordInput)
  
  def clean_password2(self):
    password1 = self.cleaned_data.get('password1')
    password2 = self.cleaned_data.get('password2')
    if password1 and password2 and password1 != password2:
      raise forms.ValidationErros(
        'As senhas não são iguais. Favor digitar novamente.')
    return password2

  def save(self, commit=True):
    user = super(RegisterForm, self).save(commit=False)
    user.set_password(self.cleaned_data['password1'])
    if commit:
      user.save()

    return user

  class Meta:
    model = User
    fields = ['username', 'email']