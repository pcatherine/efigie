#!/usr/bin/python
#-*- coding: utf-8 -*-

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.utils.text import capfirst
from django.utils.translation import ugettext_lazy as _

SIZE_CHOICES = (
  (1024, '1024'),
  (1280, '1280'),
  (1536, '1536'),
  (1792, '1792'),

  (2048, '2048'),
  (2304, '2304'),
  (2560, '2560'),
  (2816, '2816'),

  (3072, '3072'),
  (3328, '3328'),
  (3584, '3584'),
  (3840, '3840'),

  (4096, '4096'),
  (4352, '4352'),
  (4608, '4608'),
  (4864, '4864')
)

class Key(models.Model):
  """
  Stores a single key, related to :model:`auth.User`.
  """
  user = models.ForeignKey(settings.AUTH_USER_MODEL,
    on_delete = models.CASCADE,
    verbose_name = capfirst(User._meta.verbose_name))

  name = models.CharField(_('Name'),
    max_length = 255)

  size = models.IntegerField(_('Size'),
    choices=SIZE_CHOICES)

  publicKey  = models.TextField(_('Public Key'))

  privateKey = models.TextField(_('Private Key'))

  created_at = models.DateTimeField(_('Created at'),
    auto_now_add = True,
    editable = False)

  friends = models.ManyToManyField(settings.AUTH_USER_MODEL,
    related_name=_('Friends'),
    blank=True)

  def __str__(self):
    return self.name

  class Meta:
    verbose_name = _('Key')
    verbose_name_plural = _('Keys')
    ordering = ['-user']
