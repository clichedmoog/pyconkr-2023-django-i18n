from modeltranslation.translator import register, TranslationOptions
from .models import Choice, Question


@register(Question)
class QuestionTranslationOptions(TranslationOptions):
    fields = ('question_text',)


@register(Choice)
class QuestionTranslationOptions(TranslationOptions):
    fields = ('choice_text',)