#!/usr/bin/python
#-*- coding: utf-8 -*-

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _

class Message(models.Model):
  """
  Stores a single key, related to :model:`auth.User`.
  """
  count = models.IntegerField(_('Count'))

  def __str__(self):
    return '%s' % (self.count)

  class Meta:
    verbose_name = _('Message')
    verbose_name_plural = _('Messages')
