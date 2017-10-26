#!/usr/bin/python
#-*- coding: utf-8 -*-

from enum import IntEnum

from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.text import capfirst
from django.utils.translation import ugettext_lazy as _

from efigie.models import *

class UserConfirmation(models.Model):
  """
  Stores the confirmation status data, related to :model:`auth.User`.
  """
  user = models.ForeignKey(settings.AUTH_USER_MODEL,
    on_delete=models.CASCADE,
    verbose_name=capfirst(User._meta.verbose_name))

  token = models.CharField(_('Token'),
    max_length=100,
    unique=True)

  created_at = models.DateTimeField(_('Created at'),
    auto_now_add=True)

  category = models.IntegerField(_('Category'),
    default=False,
    blank=True)

  confirmed = models.BooleanField(_('Confirmed?'),
    default=False,
    blank=True)

  confirmed_at = models.DateTimeField(_('Confirmed at'),
    default= timezone.now,
    blank=True)

  confirmed_by = models.IntegerField(_('Confirmed by'),
    default=False,
    blank=True)

  def __str__(self):
    return '{0} in {1}'.format(self.user, self.created_at)

  def save(self, *args, **kwargs):
    """
    If user exists and not confirmed, confirm
    """
    UserConfirmation.objects.filter(user=self.user, confirmed=False).update(confirmed=True, confirmed_by = UserConfirmation.Confirm.SYSTEM, confirmed_at=timezone.now() )
    super(UserConfirmation,self).save(*args, **kwargs)

  class Meta:
    verbose_name = _('User Confirmation')
    verbose_name_plural = _('User Confirmations')
    ordering = ['-created_at']

  class Category(IntEnum):
    """
    Enumerates categories, extends IntEnum
    """
    VERIFICATION = 1
    PASSWORD = 2

  class Confirm(IntEnum):
    """
    Enumerates Confirmed_by options, extends IntEnum
    """
    USER = 1
    SYSTEM = 2
