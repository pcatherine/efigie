#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
  help = ""
  def handle(self, *args, **options):
    os.system("travis login")
    os.system("travis encrypt-file efigie/config.py --add")
    os.system("git add .")
    os.system("git commit -m 'teste'")
    os.system("git push github")

    # os.system("python manage.py makemigrations efigie")
    # os.system("python manage.py migrate")
    # os.system("python manage.py loaddata initial")
