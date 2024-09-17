# question_2/urls.py
from django.urls import path
from . import views
urlpatterns = [
    path('create/', views.create_model_instance, name='create_model_instance'),
]
