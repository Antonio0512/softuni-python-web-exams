from django.core.validators import MinLengthValidator, RegexValidator
from django.db import models


class Profile(models.Model):
    username = models.CharField(
        blank=False,
        max_length=30,
        validators=[
            MinLengthValidator(2, "Username must have at least 2 characters!")
        ]
    )

    first_name = models.CharField(
        blank=False,
        max_length=20,
        validators=[
            RegexValidator(
                regex=r'^([A-Z][a-z]+)$',
                message="Your name must start with a capital letter and consists of only letters!",
                code='invalid_username'
                )
        ]
    )

    last_name = models.CharField(
        blank=False,
        max_length=20,
        validators=[
            RegexValidator(
                regex=r'^([A-Z][a-z]+)$',
                message="Your name must start with a capital letter and consists of only letters!",
                code='invalid_username'
            )
        ]
    )

    profile_picture = models.URLField(
        blank=True
    )


class Plant(models.Model):
    PLANT_CHOICES = (
        ('Outdoor Plants', 'Outdoor Plants'),
        ('Indoor Plants', 'Indoor Plants')
    )

    type = models.CharField(
        blank=False,
        max_length=14,
        choices=PLANT_CHOICES
    )

    name = models.CharField(
        blank=False,
        max_length=20,
        validators=[
            MinLengthValidator(2, "Username must have at least 2 characters!"),
            RegexValidator(
                regex='^([A-Za-z]+)+$',
                message="Plant name should contain only letters!",
                code='invalid_username'
            )
        ]
    )

    image_url = models.URLField(
        blank=False
    )

    description = models.TextField(
        blank=False
    )

    price = models.FloatField(
        blank=False
    )