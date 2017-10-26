#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
  help = "Update Version"
  def handle(self, *args, **options):

    file = open('efigie/release.py', 'r+')
    lines = file.readline()
    words = lines.split('=')
    v = int(words[1]) + 1
    file.seek(0)
    file.write('VERSION = %s' % (v))
    file.close()
