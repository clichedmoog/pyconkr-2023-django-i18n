# Generated by Django 4.2.3 on 2023-07-15 19:25

from django.db import migrations
import modeltrans.fields


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='i18n',
            field=modeltrans.fields.TranslationField(fields=('choice_text',), required_languages=(), virtual_fields=True),
        ),
        migrations.AddField(
            model_name='question',
            name='i18n',
            field=modeltrans.fields.TranslationField(fields=('question_text',), required_languages=(), virtual_fields=True),
        ),
    ]