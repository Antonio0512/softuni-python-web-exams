# Generated by Django 3.2.18 on 2023-03-05 14:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_note_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='author',
        ),
    ]