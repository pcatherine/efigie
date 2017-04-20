import re

from django.db import models
from django.core import validators
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.conf import settings

from enum import IntEnum

class UserVerification(models.Model):
  user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Usuário', related_name='resets')
  key = models.CharField('Chave', max_length=100, unique=True)
  created_at = models.DateTimeField('Criado em', auto_now_add=True)
  category = models.IntegerField('Tipo', default=False, blank=True)
  confirmed = models.BooleanField('Confirmado?', default=False, blank=True)

  def __str__(self):
    return '{0} em {1}'.format(self.user, self.created_at)

  def save(self, *args, **kwargs):
    UserVerification.objects.filter(user=self.user,category=self.category, confirmed=False).update(confirmed=True)
    super(UserVerification,self).save(*args, **kwargs)

  class Meta:
    verbose_name = 'Nova Senha'
    verbose_name_plural = 'Novas Senhas'
    ordering = ['-created_at']


class Category(IntEnum):
  VERIFICATION = 1
  PASSWORD = 2