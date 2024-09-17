
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import UserProfile, ActivityLog

@receiver(post_save, sender=UserProfile)
def log_user_profile_change(sender, instance, created, **kwargs):
    if created:
        action = f"User created: {instance.name}"
    else:
        action = f"User updated: {instance.name}"

    ActivityLog.objects.create(action=action)
    print(f"Signal triggered for {instance.name}")  # Ensure this line is there

