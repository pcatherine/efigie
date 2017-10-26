#!/usr/bin/python
#-*- coding: utf-8 -*-

from enum import IntEnum

from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.text import capfirst
from django.utils.translation import ugettext_lazy as _

from efigie.models import Friend, Key

class Notification(models.Model):
  """
  Stores a single key, related to :model:`auth.User`.
  """
  user = models.ForeignKey(settings.AUTH_USER_MODEL,
    on_delete = models.CASCADE,
    related_name = 'User',
    verbose_name = capfirst(User._meta.verbose_name))

  notification_id = models.PositiveIntegerField()

  notification_type = models.ForeignKey(ContentType,
    on_delete = models.CASCADE,
    verbose_name = _('Content Type'))

  notification = GenericForeignKey('notification_type', 'notification_id')

  read = models.BooleanField(_('Read?'),
    default=False,
    blank=True)

  category = models.IntegerField(_('Category'))

  created_at = models.DateTimeField(_('Created at'),
    auto_now_add=True)

  def __str__(self):
    return _("%(notification_typet)s's Notification to %(user_name)s") % (self.notification_type, self.user)

  def icon(self):
    if   self.category == Notification.Category.FRIEND_ADD:
      return 'fa-user-plus'
    elif self.category == Notification.Category.FRIEND_ACCEPT_YOU or self.category == Notification.Category.FRIEND_I_ACCEPT:
      return 'fa-users'
    elif self.category == Notification.Category.KEY:
      return 'fa-key'
    elif self.category == Notification.Category.MESSAGE:
      return 'fa-comments-o'

  def message(self):
    if   self.category == Notification.Category.FRIEND_ADD:
      return _('sent a friend request.')
    elif self.category == Notification.Category.FRIEND_ACCEPT_YOU:
      return _('accepted your friend request.')
    elif self.category == Notification.Category.FRIEND_I_ACCEPT:
      return _("You accepted %(user)s's friend request.")
    elif self.category == Notification.Category.KEY:
      return _("shared the key %(key)s with you.")
    elif self.category == Notification.Category.MESSAGE:
      return _('sent you a message.')

  def send_by(self):
    if   self.category == Notification.Category.FRIEND_ADD:
      return Friend.objects.get(id=self.notification_id).user
    elif self.category == Notification.Category.FRIEND_ACCEPT_YOU:
      return Friend.objects.get(id=self.notification_id).user
    elif self.category == Notification.Category.FRIEND_I_ACCEPT:
      return Friend.objects.get(id=self.notification_id).user
    elif self.category == Notification.Category.KEY:
      return Key.objects.get(id=self.notification_id).user
    elif self.category == Notification.Category.MESSAGE:
      return None

  def save(self, *args, **kwargs):
    """
    If user exists and not confirmed, confirm
    """
    # AGARD VERIFICAR SE EXISTE
    super(Notification,self).save(*args, **kwargs)

  def delete(self, *args, **kwargs):
    """
    If user exists and not confirmed, confirm
    """
    # AGARD verificar se já foi deletado
    super(Notification,self).delete(*args, **kwargs)

  class Meta:
    verbose_name = _('Notification')
    verbose_name_plural = _('Notifications')
    ordering = ['-created_at']

  class Category(IntEnum):
    """
    Enumerates categories, extends IntEnum
    """
    FRIEND_ADD = 1
    FRIEND_ACCEPT_YOU = 2
    FRIEND_I_ACCEPT = 3
    KEY = 4
    MESSAGE = 5
