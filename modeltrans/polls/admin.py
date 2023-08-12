from django.contrib import admin
from modeltrans.admin import ActiveLanguageMixin

from .models import Choice, Question

class ChoiceInline(ActiveLanguageMixin, admin.StackedInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"]}),
    ]
    list_display = ["question_text", "pub_date", "was_published_recently"]
    inlines = [ChoiceInline]
    list_filter = ["pub_date"]
    search_fields = ["question_text"]


admin.site.register(Question, QuestionAdmin)