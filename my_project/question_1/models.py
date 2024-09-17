# Create your models here.

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import time
import datetime

class MyModel(models.Model):
    name = models.CharField(max_length=100)

