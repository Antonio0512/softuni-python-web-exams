# Generated by Django 4.2.2 on 2023-06-24 10:15

from django.db import migrations, models
import fruitipedia_app.accounts.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25, validators=[fruitipedia_app.accounts.validators.min_firstname_length_validator, fruitipedia_app.accounts.validators.validate_first_letter])),
                ('last_name', models.CharField(max_length=35, validators=[fruitipedia_app.accounts.validators.min_lastname_length_validator, fruitipedia_app.accounts.validators.validate_first_letter])),
                ('email', models.EmailField(max_length=40)),
                ('password', models.CharField(max_length=20, validators=[fruitipedia_app.accounts.validators.validate_password_length])),
                ('image_url', models.URLField(blank=True, null=True)),
                ('age', models.IntegerField(blank=True, default=18, null=True)),
            ],
        ),
    ]