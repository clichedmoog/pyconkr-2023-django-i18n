from django import template
from django.utils import translation
from babel.numbers import format_currency
import phonenumbers

register = template.Library()

@register.simple_tag
def currency(amount, currency_code):
    locale = translation.get_language()
    return format_currency(amount, currency_code, locale=locale)


@register.simple_tag
def smart_phonenumber(phone_number):
    try:
        pn = phonenumbers.parse(phone_number, None)
        phone_region = phonenumbers.region_code_for_number(pn)
        current_language = translation.get_language()
        current_region = current_language.split('-')[-1].upper() if '-' in current_language else current_language.upper()
        
        # Check if the current language's region matches the phone number's region
        if current_region == phone_region:
            return phonenumbers.format_number(pn, phonenumbers.PhoneNumberFormat.NATIONAL)
        else:
            return phonenumbers.format_number(pn, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
    except phonenumbers.NumberParseException:
        return phone_number  # Return the original number if parsing fails