import vinaigrette
from django.apps import AppConfig

class PollsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'polls'

    def ready(self) -> None:
        from .models import Choice, Question
        Choice = self.get_model('Choice')
        Question = self.get_model('Question')
        vinaigrette.register(Choice, fields=['choice_text'])
        vinaigrette.register(Question, fields=['question_text'])