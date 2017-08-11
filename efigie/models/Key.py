#!/usr/bin/python
#-*- coding: utf-8 -*-

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _

class Key(models.Model):
  """
  Stores a single key, related to :model:`auth.User`.
  """
  user = models.ForeignKey(settings.AUTH_USER_MODEL,
    on_delete = models.CASCADE,
    verbose_name = _('User'))

  name = models.CharField(_('Name'),
    max_length = 255,
    unique = True)

  size = models.IntegerField(_('Size'))

  publicKey  = models.TextField(_('Public Key'))

  privateKey = models.TextField(_('Private Key'))

  created_at = models.DateTimeField(_('Created at'),
    auto_now_add = True,
    editable = False)

  friends = models.ManyToManyField(settings.AUTH_USER_MODEL,
    related_name=_('Friends'),
    blank=True)

  def __str__(self):
    return '{0} created at {1} by {2}'.format(self.name, self.created_at, self.user)

  class Meta:
    verbose_name = _('Key')
    verbose_name_plural = _('Keys')
    ordering = ['-user']
