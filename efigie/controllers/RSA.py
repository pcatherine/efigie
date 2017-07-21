# class RSA(object):
#   '''
#   Referencia
#   https://docs.launchkey.com/developer/encryption/python/index.html

#   Download
#   https://pypi.python.org/pypi/pycrypto

#   LSB
#   http://code.google.com/p/stegano-cb/source/browse/LSB.py?r=3584c384b379984b8990ce7614958a8b765e1489&spec=svn571c9517e615f2a46801cabe08d71aa8dce80371
#   '''
#   @staticmethod

from Crypto.PublicKey import RSA 
from Crypto.Cipher import PKCS1_OAEP

from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256
from base64 import b64encode, b64decode


def generate(bits):
  '''
  Generate an RSA keypair with an exponent of 65537 in PEM format
  param: bits The key length in bits
  Return private key and public key
  '''
  # from Crypto.PublicKey import RSA 
  new_key = RSA.generate(bits, e=65537) 
  public_key = new_key.publickey().exportKey("PEM") 
  private_key = new_key.exportKey("PEM")

  return private_key, public_key


# @staticmethod
def encrypt(public_key_loc, message):
  '''
  param: public_key_loc Path to public key
  param: message String to be encrypted
  return base64 encoded encrypted string
  '''
  # from Crypto.PublicKey import RSA
  # from Crypto.Cipher import PKCS1_OAEP
  '''
  open(public_key_loc, "r").read()
  '''
  key = public_key_loc
  rsakey = RSA.importKey(key)
  rsakey = PKCS1_OAEP.new(rsakey)
  encrypted = rsakey.encrypt(message)
  return encrypted.encode('base64')

# @staticmethod
def decrypt(private_key_loc, package):
  '''
  param: public_key_loc Path to your private key
  param: package String to be decrypted
  return decrypted string
  '''
  # from Crypto.PublicKey import RSA
  # from Crypto.Cipher import PKCS1_OAEP
  # from base64 import b64decode
  '''
  open(private_key_loc, "r").read()
  '''
  key = private_key_loc
  rsakey = RSA.importKey(key)
  rsakey = PKCS1_OAEP.new(rsakey)
  decrypted = rsakey.decrypt(b64decode(package))
  return decrypted

# @staticmethod
def signData(private_key_loc, data):
  '''
  param: private_key_loc Path to your private key
  param: package Data to be signed
  return: base64 encoded signature
  '''
  # from Crypto.PublicKey import RSA
  # from Crypto.Signature import PKCS1_v1_5
  # from Crypto.Hash import SHA256
  # from base64 import b64encode, b64decode
  '''
  open(private_key_loc, "r").read()
  '''
  key = private_key_loc
  rsakey = RSA.importKey(key)
  signer = PKCS1_v1_5.new(rsakey)
  digest = SHA256.new()
  # It's being assumed the data is base64 encoded, so it's decoded before updating the digest
  digest.update(b64decode(data))
  sign = signer.sign(digest)
  return b64encode(sign)

# @staticmethod
def verifySign(public_key_loc, signature, data):
  '''
  Verifies with a public key from whom the data came that it was indeed
  signed by their private key
  param: public_key_loc Path to public key
  param: signature String signature to be verified
  return: Boolean. True if the signature is valid; False otherwise.
  '''
  # from Crypto.PublicKey import RSA
  # from Crypto.Signature import PKCS1_v1_5
  # from Crypto.Hash import SHA256
  # from base64 import b64decode
  '''
  open(private_key_loc, "r").read()
  '''
  pub_key = public_key_loc
  rsakey = RSA.importKey(pub_key)
  signer = PKCS1_v1_5.new(rsakey)
  digest = SHA256.new()
  # Assumes the data is base64 encoded to begin with
  digest.update(b64decode(data))
  if signer.verify(digest, b64decode(signature)):
    return True
  return False