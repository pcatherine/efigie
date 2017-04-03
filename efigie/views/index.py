from django.shortcuts import render
from efigie.views import *

def index(request):
  return render(request, 'index.html')