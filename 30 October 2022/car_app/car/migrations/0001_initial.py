# Generated by Django 3.2.18 on 2023-03-07 14:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Sports Car', 'Sports Car'), ('Pickup', 'Pickup'), ('Crossover', 'Crossover'), ('Minibus', 'Minibus'), ('Other', 'Other')], max_length=10)),
                ('model', models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(2, 'Model should be at least 2 characters long!')])),
                ('year', models.IntegerField(validators=[django.core.validators.MaxValueValidator(2049, 'Year must be between 1980 and 2049'), django.core.validators.MinValueValidator(1980, 'Year must be between 1980 and 2049')])),
                ('image_url', models.URLField()),
                ('price', models.FloatField(validators=[django.core.validators.MinValueValidator(1, 'Price must be at least 1!')])),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=10, validators=[django.core.validators.MinLengthValidator(2, 'The username must be a minimum of 2 chars')])),
                ('email', models.EmailField(max_length=254)),
                ('age', models.IntegerField(validators=[django.core.validators.MinValueValidator(18, 'You should be at least 18 years old to register!')])),
                ('password', models.CharField(max_length=30)),
                ('first_name', models.CharField(blank=True, max_length=20)),
                ('last_name', models.CharField(blank=True, max_length=20)),
                ('profile_picture', models.URLField(blank=True)),
            ],
        ),
    ]