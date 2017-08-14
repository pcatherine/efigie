#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
  help = "Heroku Deployment"
  def handle(self, *args, **options):

    # os.system("travis login")
    # os.system("travis encrypt-file efigie/config.py --add")
    # os.system("rm efigie/config.py")
    os.system('replace "efigie/config.py" "XYZ" -- .gitignore')
    os.system("git add .")
    os.system("git commit -m 'deploy'")
    os.system("git push heroku --force")
    os.system('replace "XYZ" "efigie/config.py" -- .gitignore')


    # os.system("python manage.py makemigrations efigie")
    # os.system("python manage.py migrate")
    # os.system("python manage.py loaddata initial")
