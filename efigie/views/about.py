#!/usr/bin/python
#-*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django import http

from efigie import *
from efigie.views import *
from django.urls import resolve, reverse, reverse_lazy

import efigie.urls 


@login_required
@breadcrumbs(['index', 'about'])
def about(request):

  return render(request, 'about.html', 
    {'breadcrumbs': breadcrumbs })