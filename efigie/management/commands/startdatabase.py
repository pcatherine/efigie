#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from psycopg2 import connect
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

from django.core.management.base import BaseCommand, CommandError

import efigie.settings as settings

class Command(BaseCommand):
  help = "Starts postgres's database"
    # def add_arguments(self, parser):
    #    parser.add_argument('book_id', nargs='+', type=int)
    #    parser.add_argument('author' , nargs='+', type=str)

  def handle(self, *args, **options):
    # bookid = options['book_id']
    # author = options['author']

    con = None
    try:
      con = connect(dbname='postgres',
        user=settings.DATABASES['default']['USER'],
        password=settings.DATABASES['default']['PASSWORD'],
        host=settings.DATABASES['default']['HOST'])
    except Exception as e:
      print("FATAL:  password authentication failed for user '%s'" % (settings.DATABASES['default']['USER']))


    if con != None:
      con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

      cur = con.cursor()
      try:
        cur.execute('CREATE DATABASE %s' % (settings.DATABASES['default']['NAME']))
        cur.close()
        con.close()
        print("Database '%s' created" % (settings.DATABASES['default']['NAME']))
      except Exception as e:
        print("Database '%s' already exists" % (settings.DATABASES['default']['NAME']))
