#!/usr/bin/python
#-*- coding: utf-8 -*-

import re
from PIL import Image

from django.utils.translation import ugettext_lazy as _

from efigie.utils import RSA, utils

IDENTIFICADOR = u"efigie"

# CATHERINE aparentemente okay

def setEffigy(path, setting, msg, idMessage):
  """
    OKAY
  """
  try:
    img = Image.open(path)
    if img.mode != 'RGB':
      img = img.convert('RGB')
  except Exception as e:
    raise Exception(_('This image could not be opened.'))

  width, height = img.size

  message = utils.toBinary('##' + str(idMessage) + '##') + utils.toBinary(msg) + ('00000000' * 8)

  if (width * height - 4) < identifySizeImagem(setting, message):
    raise Exception(_('This image is too small.'))

  authenticate(img, width, height)
  row, col = setHeader(img, setting, width, height)
  setMessage(img, message, setting, width, height, row, col)
  return img
  # img.save("static/path.png")



def getEffigy(path):
  try:
    img = Image.open(path)
  except Exception as e:
    raise Exception(_('This image could not be opened.'))

  width, height = img.size
  if isAuthenticate(img, width, height):

    header, setting, row, col = getHeader(img, width, height)
    if header:
      idMessage, m = getMessage(img, setting, width, height, row, col)
      return idMessage, m, setting
    else:
      raise Exception(_('This image could not be opened.'))
  else:
    raise Exception(_('This image is not authentic.'))



def authenticate(img, width, height):
  """
    OKAY
  """
  validationBin = list(utils.toBinary(IDENTIFICADOR))
  setAuthenticate(img, (0,0), validationBin[0:12])
  setAuthenticate(img, (width-1, 0), validationBin[12:24])
  setAuthenticate(img, (0, height-1), validationBin[24:36])
  setAuthenticate(img, (width-1, height-1), validationBin[36:48])


def getAuthenticate(img, coo):
  (r, g, b) = img.getpixel(coo)
  msg  = ('{0:08b}'.format(r))[4:8]
  msg += ('{0:08b}'.format(g))[4:8]
  msg += ('{0:08b}'.format(b))[4:8]
  return msg


def setAuthenticate(img, coo, msg):
  (r, g, b) = img.getpixel(coo)

  r_bits = list('{0:08b}'.format(r))
  g_bits = list('{0:08b}'.format(g))
  b_bits = list('{0:08b}'.format(b))

  r_bits[4:8] = msg[0:4]
  g_bits[4:8] = msg[4:8]
  b_bits[4:8] = msg[8:12]

  img.putpixel(coo, (int("".join(r_bits),  2), int("".join(g_bits),  2) , int("".join(b_bits),  2)))


def isAuthenticate(img, width, height):
  validationBin =  getAuthenticate(img, (0,0))
  validationBin += getAuthenticate(img, (width-1, 0))
  validationBin += getAuthenticate(img, (0, height-1))
  validationBin += getAuthenticate(img, (width-1, height-1))
  validationStr = utils.toString("".join(validationBin))
  return True if validationStr == IDENTIFICADOR else False


def getHeader(img, width, height):
  """
    OKAY
  """
  msg = ""
  for row in range(2, height-1):
    for col in range(2, width-1):
      (r, g, b) = img.getpixel((col, row))
      msg += ('{0:08b}'.format(r))[6:8]
      msg += ('{0:08b}'.format(g))[6:8]
      msg += ('{0:08b}'.format(b))[6:8]
      if len(msg) >= 114:
        try:
          return((False, "", row+1, col+1), (True, "".join(msg[48:-48]), row+1, col+1)) [utils.toString("".join(list(msg)[0:48])) == IDENTIFICADOR and utils.toString("".join(list(msg)[0:48])) == IDENTIFICADOR]
        except Exception as e:
          return False


def setHeader(img, setting, width, height):
  """
    OKAY
  """
  validationBin = utils.toBinary(IDENTIFICADOR)
  settingL = list(validationBin + setting + validationBin)
  index = 0
  for row in range(2, height-1):
    for col in range(2, width-1):
      (r, g, b) = img.getpixel((col, row))
      r_bits = list('{0:08b}'.format(r))
      g_bits = list('{0:08b}'.format(g))
      b_bits = list('{0:08b}'.format(b))

      r_bits[6:8] = settingL[index  :index+2]
      g_bits[6:8] = settingL[index+2:index+4]
      b_bits[6:8] = settingL[index+4:index+6]

      img.putpixel((col, row), (int("".join(r_bits),  2), int("".join(g_bits),  2) , int("".join(b_bits),  2)))
      index+= 6

      if index >= len(settingL):
        return row+1, col+1


def getMessage(img, setting, width, height, i, j):
  """
    OKAY
  """
  message = ""

  for row in range(i, height-1):
    for col in range(j, width-1):
      (r, g, b) = img.getpixel((col, row))
      teste = (col * row) % 2
      if((teste == 0 and setting[11:13] == '10') or (teste != 0 and setting[11:13] == '01') or (setting[11:13] == '11')):
        message += "".join(map(lambda x: ('{0:08b}'.format(r)[x[0]] if x[1] == '1' and setting[0] == '1' else ""), [(idx,val) for (idx,val) in enumerate(setting[3:11])]))
        message += "".join(map(lambda x: ('{0:08b}'.format(g)[x[0]] if x[1] == '1' and setting[1] == '1' else ""), [(idx,val) for (idx,val) in enumerate(setting[3:11])]))
        message += "".join(map(lambda x: ('{0:08b}'.format(b)[x[0]] if x[1] == '1' and setting[2] == '1' else ""), [(idx,val) for (idx,val) in enumerate(setting[3:11])]))
      if len(message)>=16 and "".join(list(message)[-16:]) == ('00000000'*2):
        message = utils.toString("".join(list(message)[:-16]))
        try:
          idMessage = re.match('^[#]{2}(\d+)[#]{2}', message).groups(0)[0]
          return idMessage, message[len("".join(idMessage))+4:]
        except Exception:
          raise Exception(_('This image is not authentic.'))
  raise Exception(_('This image is not authentic.'))


def setMessage(img, message, setting, width, height, i, j):
  """
    OKAY
  """
  index = 0
  for row in range(i, height-1):
    for col in range(j, width-1):
      (r, g, b) = img.getpixel((col, row))
      teste = (col * row) % 2
      if((teste == 0 and setting[11:13] == "10") or (teste != 0 and setting[11:13] == "01") or (setting[11:13] == "11")):

        r_bits = list('{0:08b}'.format(r))
        for i in range (0, 8):
          if setting[0] == '1' and setting[3+i] == '1' and index < len(message):
            r_bits[i] = message[index]
            index+=1

        g_bits = list('{0:08b}'.format(g))
        for i in range (0, 8):
          if setting[1] == '1' and setting[3+i]  == '1' and index < len(message):
            g_bits[i] = message[index]
            index+=1

        b_bits = list('{0:08b}'.format(b))
        for i in range (0, 8):
          if setting[2] == '1'and setting[3+i] == '1' and index < len(message):
            b_bits[i] = message[index]
            index+=1
        img.putpixel((col, row), (int("".join(r_bits),  2), int("".join(g_bits),  2) , int("".join(b_bits),  2)))
      if index >= len(message):
        break
    if index >= len(message):
      break


def identifySizeImagem(setting, message):
  """
    OKAY
    Min settings possible:
      "00100000001010000"
      "RGB12345678******"

    efigie
    pixel X+2
    R 00000011 - 0 vermelho e 1 verde
    G 00000011 - 2 azul e 3 0
    B 00000011 - 4 1 e 5 2
    pixel X+3
    R 00000011 - 6 3 e 7 4
    G 00000011 - 8 5 e 9 6
    B 00000010 - 10 7 e 11 NADA
    pixel X+4
    R 00000011 - 12 13 par ou impar ou ambos (10 01 11)
    G 00000011 - 14 chave publica 15 chave privada
    B 00000000 - 16 17 NADA
    efigie
    chave especial: true; false
    tamanho chave: >= 1024
    tamanho da imagem: calc
    quantidade de cores: 0

  """

  j = 0;
  k = 0;
  for i in range (0, 3):
    if setting[i] == '1':
      j += 1

  for i in range(3,11):
    if setting[i] == '1':
      k += 1

  return 4 + (len(setting) / 6)  + (len(message) / (j * k)) + 1
