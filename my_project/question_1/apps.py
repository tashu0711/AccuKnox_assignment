# from django.apps import AppConfig


# class Question1Config(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'question_1'

from django.apps import AppConfig

class MyappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'question_1'

    def ready(self):
        import question_1.signals
