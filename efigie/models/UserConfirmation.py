from django.db import models
from django.core import validators
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.conf import settings

from enum import IntEnum

class UserConfirmation(models.Model):
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='User')
  token = models.CharField('Token', max_length=100, unique=True)
  created_at = models.DateTimeField('Created at', auto_now_add=True, editable=False)
  category = models.IntegerField('Category', default=False, blank=True)
  confirmed = models.BooleanField('Confirmed?', default=False, blank=True)

  def __str__(self):
    return '{0} em {1}'.format(self.user, self.created_at)

  def save(self, *args, **kwargs):
    UserConfirmation.objects.filter(user=self.user,category=self.category, confirmed=False).update(confirmed=True)
    super(UserConfirmation,self).save(*args, **kwargs)

  class Meta:
    verbose_name = 'User Confirmation'
    ordering = ['-created_at']


class Category(IntEnum):
  VERIFICATION = 1
  PASSWORD = 2