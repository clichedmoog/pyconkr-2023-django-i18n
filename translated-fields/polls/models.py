import datetime

from django.db import models
from django.contrib import admin
from django.utils import timezone
from translated_fields import TranslatedField


class Question(models.Model):
    question_text = TranslatedField(
        models.CharField(max_length=200)
    )
    pub_date = models.DateTimeField("date published")

    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = TranslatedField(
        models.CharField(max_length=200)
    )
    votes = models.IntegerField(default=0)
