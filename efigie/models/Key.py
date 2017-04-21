from django.db import models
from django.contrib.auth.models import User

class Key(models.Model):
  user = models.ForeignKey(settings.AUTH_USER_MODEL)
  identifier = models.CharField(max_length=255)
  size = models.IntegerField()
  publicKey  = models.TextField()
  privateKey = models.TextField()