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
    return '{0} created at {1} by {2}'.format(self.name, self.created_at, self.user)

  class Meta:
    verbose_name = _('Message')
    verbose_name_plural = _('Messages')
    # ordering = ['-user']
