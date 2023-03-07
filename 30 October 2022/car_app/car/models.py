from django.core.validators import MinValueValidator, MinLengthValidator, MaxValueValidator
from django.db import models


class Profile(models.Model):
    username = models.CharField(
        blank=False,
        max_length=10,
        validators=[
            MinLengthValidator(2, "The username must be a minimum of 2 chars")
        ]
    )

    email = models.EmailField(
        blank=False
    )

    age = models.IntegerField(
        blank=False,
        validators=[
            MinValueValidator(18, "You should be at least 18 years old to register!")
        ]
    )

    password = models.CharField(
        blank=False,
        max_length=30
    )

    first_name = models.CharField(
        blank=True,
        max_length=20
    )

    last_name = models.CharField(
        blank=True,
        max_length=20
    )

    profile_picture = models.URLField(
        blank=True,
    )


class Car(models.Model):
    AVAILABLE_CHOICES = (
        ('Sports Car', 'Sports Car'),
        ('Pickup', 'Pickup'),
        ('Crossover', 'Crossover'),
        ('Minibus', 'Minibus'),
        ('Other', 'Other'),
    )

    type = models.CharField(
        blank=False,
        max_length=10,
        choices=AVAILABLE_CHOICES
    )

    model = models.CharField(
        blank=False,
        max_length=20,
        validators=[
            MinLengthValidator(2, "Model should be at least 2 characters long!")
        ]
    )

    year = models.IntegerField(
        blank=False,
        validators=[
            MaxValueValidator(2049, "Year must be between 1980 and 2049"),
            MinValueValidator(1980, "Year must be between 1980 and 2049")
        ]
    )

    image_url = models.URLField(
        blank=False,
    )

    price = models.FloatField(
        blank=False,
        validators=[
            MinValueValidator(1, 'Price must be at least 1!')
        ]
    )