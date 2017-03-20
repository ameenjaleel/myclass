"""from django.contrib.auth.models import User
#from django.db import models
from passlib.hash import pbkdf2_sha256
#Django default user model is used
# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    def verify_password(raw_password):
        return pbkdf2_sha256.verify(raw_password,self.password)
    def __unicode__(self):
        return self.username
"""
