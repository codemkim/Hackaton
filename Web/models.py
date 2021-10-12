from django.contrib.auth.models import User
from django.db import models

class Result(models.Model):

    image = models.ImageField(upload_to='', null=True)

