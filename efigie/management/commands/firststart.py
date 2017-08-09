#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
  help = "Executes manage's commands: startdatabase, makemigrations, makemigrations efigie, migrate and loaddata initial"
  def handle(self, *args, **options):
    os.system("python manage.py startdatabase")
    os.system("python manage.py makemigrations")
    os.system("python manage.py makemigrations efigie")
    os.system("python manage.py migrate")
    os.system("python manage.py loaddata initial")
