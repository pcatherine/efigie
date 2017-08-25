#!/usr/bin/python
#-*- coding: utf-8 -*-

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _

class UserEffigy(models.Model):
  """
    Stores the Effigy's configurations, related to :model:`auth.User`.
  """

  user = models.ForeignKey(settings.AUTH_USER_MODEL,
    on_delete = models.CASCADE,
    verbose_name = _('User'))

  settings = models.CharField(_('Settings'),
    max_length = 255)
