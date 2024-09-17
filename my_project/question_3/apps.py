from django.apps import AppConfig

class Question3Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'question_3'

    def ready(self):
        import question_3.signals  # Ensure that signals are registered
