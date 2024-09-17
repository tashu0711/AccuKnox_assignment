from django.shortcuts import render
# # Create your views here.
from django.http import HttpResponse
from .models import UserProfile

def create_user_profile(request):
    user = UserProfile.objects.create(name="Ashu", email="ashu@example.com")
    return HttpResponse(f"User profile created: {user.name}")

def update_user_profile(request):
    try:
        user = UserProfile.objects.get(name="Ashu")
        user.email = "newemail@example.com"
        user.save()  # This will trigger the post_save signal and log the update
        return HttpResponse(f"User profile updated: {user.name}")
    except UserProfile.DoesNotExist:
        return HttpResponse("User does not exist")


# Create your views here.
# from django.shortcuts import HttpResponse
# from .models import UserProfile, ActivityLog
# from django.db import transaction

# def create_user_with_rollback(request):
#     try:
#         with transaction.atomic():
#             # Create user profile
#             user = UserProfile.objects.create(name="Ashu Bhai", email="ashuu@example.com")
            
#             # Simulate an error to trigger a rollback
#             raise Exception("Simulated rollback error")
        
#         return HttpResponse("User created")
#     except Exception as e:
#         return HttpResponse(f"Error: {e}")
