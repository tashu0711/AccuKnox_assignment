# import time
# from django.db.models.signals import post_save
# from django.dispatch import receiver
from django.contrib.auth.models import User

from django.db import models
from .models import MyModel
from django.db.models.signals import post_save
from django.dispatch import receiver
import time
import datetime


# @receiver(post_save, sender=User)
# def my_signal_receiver(sender, instance, **kwargs):
#     print("Signal received. Starting long task...")
#     time.sleep(5)  # Simulate a long task
#     print("Long task finished.")


@receiver(post_save, sender=MyModel)
def my_signal_handler(sender, instance, **kwargs):
    print(f"Signal handler started at {datetime.datetime.now()}")
    time.sleep(5)  
    print(f"Signal handler finished at {datetime.datetime.now()}")
