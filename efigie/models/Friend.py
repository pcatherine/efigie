#!/usr/bin/python
#-*- coding: utf-8 -*-

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.utils.text import capfirst
from django.utils.translation import ugettext_lazy as _


class FriendManager(models.Manager):
  def possible_friend(self, user):
    """
    Returns the user list that user is not blocked.
    """
    users = User.objects.exclude(id = user.id)
    f = Friend.objects.filter(friend=user, blocked=True).values('user')
    return users.exclude(id__in=f).order_by('first_name')


  def relationship(self, user, friend):
    """
    Returns the relationship of two users.
    """
    if Friend.objects.filter(user=user, friend=friend, blocked=False).exists():
      return Friend.objects.get(user=user, friend=friend, blocked=False)
    elif Friend.objects.filter(user=friend, friend=user, blocked=False).exists():
      return Friend.objects.get(user=friend, friend=user, blocked=False)
    return None

  def get_friends(self, user):
    """
    Returns the friend list by user.
    """
    friends = Friend.objects.filter(user = user, friendship = True).values('friend')
    users = User.objects.filter(id__in=friends).order_by('first_name').order_by('last_name')
    return users

  def get_blocked_friends(self, user):
    """
    Returns the blocked friend list by user.
    """
    friends = Friend.objects.filter(user = user, blocked = True).values('friend')
    users = User.objects.filter(id__in=friends).order_by('first_name').order_by('last_name')
    return users

class Friend(models.Model):
  """
  Stores a single key, related to :model:`auth.User`.
  """
  user = models.ForeignKey(settings.AUTH_USER_MODEL,
    on_delete = models.CASCADE,
    verbose_name = capfirst(User._meta.verbose_name))

  friend = models.ForeignKey(settings.AUTH_USER_MODEL,
    related_name=_('Friend'),
    blank=True)

  friendship = models.BooleanField(_('Friendship?'),
    default=False,
    blank=True)

  blocked = models.BooleanField(_('Blocked?'),
    default=False,
    blank=True)

  objects = FriendManager()


  def __str__(self):
    return "%s" % (self.user)

  class Meta:
    verbose_name = _('Friend')
    verbose_name_plural = _('Friends')
    ordering = ['-user']
