#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

from django.core.management.base import BaseCommand, CommandError
import efigie.release as release

class Command(BaseCommand):
  help = "Heroku Deployment"
  def add_arguments(self, parser):
    parser.add_argument(
      '-m', default='',
        help='Add comment on commit',
      )

  def handle(self, *args, **options):
    # os.system("travis login")
    # os.system("travis encrypt-file efigie/config.py --add")
    # os.system("rm efigie/config.py")

    os.system('python manage.py updateversion')
    os.system('replace "efigie/config.py" "XYZ" -- .gitignore')
    os.system("git add .")
    os.system('git commit -m "Deploy v0.9.%s %s" ' % (release.VERSION+1, options['m']))
    os.system("git push")
    os.system("git push heroku ")
    os.system('replace "XYZ" "efigie/config.py" -- .gitignore')

    # os.system("python manage.py makemigrations")
    # os.system("python manage.py makemigrations efigie")
    # os.system("python manage.py migrate")
    # os.system("python manage.py loaddata initial")

    # os.system("python manage.py makemigrations efigie")
    # os.system("python manage.py migrate")
    # os.system("python manage.py loaddata initial")
