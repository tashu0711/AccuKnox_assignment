from django.urls import path
from . import views

urlpatterns = [
    path('rectangle/', views.rectangle_view, name='rectangle_view'),
]
