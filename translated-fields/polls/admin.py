from django.contrib import admin
from translated_fields import TranslatedFieldAdmin

from .models import Choice, Question

class ChoiceInline(TranslatedFieldAdmin, admin.StackedInline):
    model = Choice
    extra = 3


class QuestionAdmin(TranslatedFieldAdmin, admin.ModelAdmin):

    list_display = ["question_text_ko", "pub_date", "was_published_recently"]
    inlines = [ChoiceInline]
    list_filter = ["pub_date"]
    search_fields = ["question_text"]


admin.site.register(Question, QuestionAdmin)