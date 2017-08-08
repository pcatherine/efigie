#!/usr/bin/python
#-*- coding: utf-8 -*-

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
     'formatters': {
        'simple': {
            'format': '[%(asctime)s] %(levelname)s %(message)s',
            'datefmt': '%d-%m-%Y %H:%M:%S',
        },
    },
    'handlers': {
        'debug': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, '..', 'logs/debug.log'),
            'maxBytes' : 1024*1024*10,
            'formatter': 'simple',
        },
        'error': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR,'..', 'logs/error.log'),
            'maxBytes' : 1024*1024*10,
            'formatter': 'simple',
        },
        'critical': {
            'level': 'CRITICAL',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR,'..', 'logs/critical.log'),
            'maxBytes' : 1024*1024*10,
            'formatter': 'simple',
        },

    },
    'loggers': {
        '': {
            'handlers': ['debug'],
            'level': 'DEBUG',
            'propagate': True,
          },
        'error_logger': {
            'handlers': ['error'],
            'level': 'ERROR',
            'propagate': True,
          },
        'critical_logger': {
            'handlers': ['critical'],
            'level': 'CRITICAL',
            'propagate': True,
          },
    }
  }

import logging
  #  from efigie.utils import log
  #  log.error('Erro: Form inválido') #LOGGER ERROR EXEMPLE
  #  log.critical('Erro Crítico: Form inválido') #LOGGER CRITICAL EXEMPLE
logger = logging.getLogger(__name__)

def error(message):
  logger_error = logging.getLogger('error_logger')
  logger_error.error(message)

def critical(message):
  logger_critical = logging.getLogger('critical_logger')
  logger_critical.critical(message)
