from django.shortcuts import HttpResponse
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
import threading

# Signal receiver
@receiver(post_save, sender=User)
def user_post_save_receiver(sender, instance, **kwargs):
    print(f"Signal Handler Thread: {threading.current_thread().name}")
    print(f"User instance saved: {instance.username}")

# View to create a new User
def trigger_signal_view(request):
    print(f"Main Thread: {threading.current_thread().name}")
    
    # Creation of a new User instance, this will trigger the post_save signal
    User.objects.create_user(username="signal_test_user", password="testpassword")
    
    return HttpResponse("Signal triggered, check your console output.")

