#!/usr/bin/python
#-*- coding: utf-8 -*-

import hashlib
import string
import random
from functools import reduce


def randomKey(size=5):
  chars = string.ascii_uppercase + string.digits
  return ''.join(random.choice(chars) for x in range(size))

def generateHashKey(salt, random_str_size=5):
  random_str = randomKey(random_str_size)
  text = random_str + salt
  return hashlib.sha224(text.encode('utf-8')).hexdigest()

def toBinary(message):
  return bin(reduce(lambda x, y : (x<<8)+y, (ord(c) for c in message), 1))[3:]

def toString(binary):
  # print(binary)
  # print(len(binary))
  # print(len(binary)/8)
  # print(chr(int(binary[i*8:i*8+8],2)) for i in range(len(binary)/8))
  return removeNotChar("".join([chr(int(binary[i*8:i*8+8],2)) for i in range(int(len(binary)/8))]))

def removeNotChar(message):
  for i in range(len(message), -1, -1):
    if ord("".join(list(message)[i-1:i])) > 30 and ord("".join(list(message)[i-1:i])) < 256:
      return "".join(list(message)[:i])

# import efigie.config
# import efigie.settings

# def sendNotificationDeveloper(eventName, message):
#   insta = Instapush(user_token=config.INSTAPUSH_USER_TOKEN)
#   app = App(appid=config.INSTAPUSH_APPID, secret=config.INSTAPUSH_SECRET)
#   app.notify(event_name=eventName, trackers={'message': message})

# def alert(description, alert):
#   return {'description': description,
#     'alert': alert}

# def confirm(confirmTitle, confirmDescription, confirmUrl, confirmButton):
#   return {'confirmTitle': confirmTitle,
#     'confirmDescription': confirmDescription,
#     'confirmUrl': confirmUrl,
#     'confirmButton': confirmButton}
