# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from efigie.controllers import *
from efigie.views import *
from efigie.forms import *

@login_required
def userLogout(request):
  logout(request)
  return redirect(userLogin)
