from django.urls import path
from . import views  # Import your views

urlpatterns = [
    path('create-user/', views.create_user_profile, name='create_user'),   #to create user
    path('update-user/', views.update_user_profile, name='update_user'),   #to update user
    # path('create-user-with-rollback/', views.create_user_with_rollback, name='create_user_with_rollback'), #to test rollback
    
]
