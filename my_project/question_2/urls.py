# question_1/urls.py
from django.urls import path
from .views import trigger_signal_view

urlpatterns = [
    path('trigger-signal/', trigger_signal_view, name='trigger-signal'),  # Map to the view
]
