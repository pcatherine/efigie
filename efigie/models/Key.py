from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Key(models.Model):
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='User')
  name = models.CharField('Name',max_length=255)
  size = models.IntegerField('Size')
  publicKey  = models.TextField('Public Key')
  privateKey = models.TextField('Private Key')
  created_at = models.DateTimeField('Created at', auto_now_add=True, editable=False)

  class Meta:
    verbose_name = 'Key'
    ordering = ['-user']