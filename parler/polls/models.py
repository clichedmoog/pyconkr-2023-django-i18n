import datetime

from django.db import models
from django.contrib import admin
from django.utils import timezone
from parler.models import TranslatableModel, TranslatedFields

class Question(TranslatableModel):
    pub_date = models.DateTimeField("date published")
    translations = TranslatedFields(
        question_text = models.CharField(max_length=200)
    )

    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(TranslatableModel):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    votes = models.IntegerField(default=0)
    translations = TranslatedFields(
        choice_text = models.CharField(max_length=200)
    )