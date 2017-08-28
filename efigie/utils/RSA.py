# # class RSA(object):
# #   '''
# #   Referencia
# #   https://docs.launchkey.com/developer/encryption/python/index.html

# #   Download
# #   https://pypi.python.org/pypi/pycrypto

# #   LSB
# #   http://code.google.com/p/stegano-cb/source/browse/LSB.py?r=3584c384b379984b8990ce7614958a8b765e1489&spec=svn571c9517e615f2a46801cabe08d71aa8dce80371
# #   '''
# #   @staticmethod

# from Crypto.PublicKey import RSA
# from Crypto.Cipher import PKCS1_OAEP

# from Crypto.Signature import PKCS1_v1_5
# from Crypto.Hash import SHA256
# from base64 import b64encode, b64decode


# # @staticmethod
# def signData(private_key_loc, data):
#   '''
#   param: private_key_loc Path to your private key
#   param: package Data to be signed
#   return: base64 encoded signature
#   '''
#   # from Crypto.PublicKey import RSA
#   # from Crypto.Signature import PKCS1_v1_5
#   # from Crypto.Hash import SHA256
#   # from base64 import b64encode, b64decode
#   '''
#   open(private_key_loc, "r").read()
#   '''
#   key = private_key_loc
#   rsakey = RSA.importKey(key)
#   signer = PKCS1_v1_5.new(rsakey)
#   digest = SHA256.new()
#   # It's being assumed the data is base64 encoded, so it's decoded before updating the digest
#   digest.update(b64decode(data))
#   sign = signer.sign(digest)
#   return b64encode(sign)

# # @staticmethod
# def verifySign(public_key_loc, signature, data):
#   '''
#   Verifies with a public key from whom the data came that it was indeed
#   signed by their private key
#   param: public_key_loc Path to public key
#   param: signature String signature to be verified
#   return: Boolean. True if the signature is valid; False otherwise.
#   '''
#   # from Crypto.PublicKey import RSA
#   # from Crypto.Signature import PKCS1_v1_5
#   # from Crypto.Hash import SHA256
#   # from base64 import b64decode
#   '''
#   open(private_key_loc, "r").read()
#   '''
#   pub_key = public_key_loc
#   rsakey = RSA.importKey(pub_key)
#   signer = PKCS1_v1_5.new(rsakey)
#   digest = SHA256.new()
#   # Assumes the data is base64 encoded to begin with
#   digest.update(b64decode(data))
#   if signer.verify(digest, b64decode(signature)):
#     return True
#   return False

from base64 import b64decode, b64encode

# from Crypto.Cipher import PKCS1_OAEP
# from Crypto.PublicKey import RSA

# AGARD MENSAGEM COM TAMANHO LIMITADO

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


def encrypt(public_key_loc, message):
  rsakey = RSA.importKey(public_key_loc)
  rsakey = PKCS1_OAEP.new(rsakey)
  encrypted = rsakey.encrypt(bytes(message, 'utf-8'))
  # print(encrypted)
  return b64encode(encrypted)


def decrypt(private_key_loc, package):
  rsakey = RSA.importKey(private_key_loc)
  rsakey = PKCS1_OAEP.new(rsakey)
  decrypted = rsakey.decrypt(b64decode(package))
  return decrypted.decode('utf-8')


# if __name__ == '__main__':
#   pri1,pub1 = generate(1024)
#   pri2,pub2 = generate(1024)
#   msg = 'to puta'
#   text = encrypt(pub1, msg)
#   print(text)
#   oi = decrypt(pri1, text)
#   print(oi)
#   print(bytes(msg, 'utf-8'))
