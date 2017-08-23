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
  return removeNotChar("".join([chr(int(binary[i*8:i*8+8],2)) for i in range(int(len(binary)/8))]))

def removeNotChar(message):
  for i in range(len(message), -1, -1):
    if ord("".join(list(message)[i-1:i])) > 30 and ord("".join(list(message)[i-1:i])) < 256:
      return "".join(list(message)[:i])


# if __name__ == "__main__":
  # print('01100101011001100110100101100111011010010110010100100000001000000011001010110011001101001011001110110100101100101')
  # oi = "00100000001000000"
  # print('%s%s%s' % (toBinary('efigie'),oi,toBinary('efigie')))
  # print(identifySizeImagem('00100000001000000', 'PaOLLA'))

  # message = toBinary('##' + str(1) + '##') + toBinary('PAOLLA') + ('00000000' * 8)
  # print(message)
  # print(toString(message).decode('utf-8') )
