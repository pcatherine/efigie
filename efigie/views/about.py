# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from efigie.views import *

@login_required
def about(request):
  return render(request, 'about.html')