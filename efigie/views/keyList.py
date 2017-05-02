from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from efigie.models import Key

@login_required
def keyList(request, alert='', description=''):
  keyList = Key.objects.filter(user = request.user).order_by('identifier')
  
  return render(request, 'key_list.html',
    {'keyList': keyList})