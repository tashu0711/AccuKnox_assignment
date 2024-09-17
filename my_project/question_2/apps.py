from django.apps import AppConfig

class Question1Config(AppConfig):
    name = 'question_2'

    def ready(self):
        # Import signal receivers
        from . import views  # Import the module to ensure signals are registered
