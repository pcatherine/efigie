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
@breadcrumbs(['index', 'friendSearch']) #agard
@csrf_protect
def friendSearch(request):
  """
  Search View

  Display a search form of :model:`auth.User` by name.

  **Templates**

    :template:`friend/search.html`.

  """

  if request.is_ajax():
    value = " ".join(request.GET['search'].split())

    if len(value) > 3:
      users = Friend.objects.possible_friend(user=request.user)
      for term in value.split():
        users = users.filter( Q(first_name__icontains = term) | Q(last_name__icontains = term) | Q(email__icontains = term))

      data = []
      for u in users:
        if Friend.objects.filter(user=request.user, friend=u).exists():
          f = Friend.objects.get(user=request.user, friend=u)

          if not f.friendship and not f.blocked:
            category = 2
          elif not f.friendship and f.blocked:
            category = 4
          elif f.friendship and not f.blocked:
            category = 3
          elif f.friendship and f.blocked:
            category = 4
        elif Friend.objects.filter(user=u, friend=request.user).exists():
          category = 2
        else:
          category = 1

        data.append({'id': u.id, 'name': u.get_full_name(), 'email': u.email, 'category':category })

      return JsonResponse(data, status = 200, safe=False)
    return JsonResponse({}, status = 200, safe=False)

  return render(request, 'friend/search.html')
