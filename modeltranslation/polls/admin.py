from django.contrib import admin
from modeltranslation.admin import TranslationAdmin, TranslationStackedInline
from .models import Choice, Question


class ChoiceInline(TranslationStackedInline):
    model = Choice
    extra = 3


class QuestionAdmin(TranslationAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"]}),
    ]
    list_display = ["question_text", "pub_date", "was_published_recently"]
    inlines = [ChoiceInline]
    list_filter = ["pub_date"]
    search_fields = ["question_text"]


admin.site.register(Question, QuestionAdmin)