from django import template
from babel.numbers import format_currency

register = template.Library()

@register.simple_tag
def currency(amount, currency_code):
    locale = get_language()
    return format_currency(amount, currency_code, locale=locale)
