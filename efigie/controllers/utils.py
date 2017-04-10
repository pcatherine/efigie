import hashlib
import string
import random

def randomKey(size=5):
  chars = string.ascii_uppercase + string.digits
  return ''.join(random.choice(chars) for x in range(size))

def generateHashKey(salt, random_str_size=5):
  random_str = randomKey(random_str_size)
  text = random_str + salt
  return hashlib.sha224(text.encode('utf-8')).hexdigest()
