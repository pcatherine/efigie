#!/usr/bin/python
#-*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect

from efigie.views.decorators import model_required, breadcrumbs

from efigie import *
from efigie.models import Friend
from efigie.views import *
from efigie.views.friend import *
from efigie.utils import invariants


@login_required
@breadcrumbs(['index', 'friendSearch', 'friendSearchResults']) #agard
@csrf_protect
def friendSearchResults(request, results=None):
  """
  Search View

  Display a search's results form of :model:`auth.User` by name.

  **Templates**

    :template:`friend/search_results.html`.

  """
  search = request.POST.get('search' or None)
  users = None

  if search != None:
    users = Friend.objects.possible_friend(user=request.user)
    for term in search.split():
      users = users.filter( Q(first_name__icontains = term) | Q(last_name__icontains = term) | Q(email__icontains = term))

    for u in users:
      if Friend.objects.filter(user=request.user, friend=u).exists():
        f = Friend.objects.get(user=request.user, friend=u)

        if not f.friendship and not f.blocked:
          u.username = 2
        elif not f.friendship and f.blocked:
          u.username = 4
        elif f.friendship and not f.blocked:
          u.username = 3
        elif f.friendship and f.blocked:
          u.username = 4
      elif Friend.objects.filter(user=u, friend=request.user).exists():
        u.username = 2
      else:
        u.username = 1

  return render(request, 'friend/search_results.html',
    {'friends': users })
