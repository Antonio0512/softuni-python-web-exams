from django.core.validators import MinLengthValidator, RegexValidator
from django.db import models


class Profile(models.Model):
    username = models.CharField(
        max_length=15,
        validators=[
            MinLengthValidator(2, 'The field must contain at least 2 characters!'),
            RegexValidator(r'^[A-Za-z0-9_-]+$', "Ensure this value contains only letters, numbers, and underscore."),
        ],
        blank=False
    )
    email = models.EmailField(
        blank=False,
    )
    age = models.PositiveIntegerField(
        blank=True
    )


class Album(models.Model):
    POP_MUSIC = 'Pop Music'
    JAZZ_MUSIC = 'Jazz Music'
    RNB_MUSIC = 'R&B Music'
    ROCK_MUSIC = 'Rock Music'
    COUNTRY_MUSIC = 'Country Music'
    DANCE_MUSIC = 'Dance Music'
    HIP_HOP_MUSIC = 'Hip Hop Music'
    OTHER_MUSIC = "Other "

    GENRE_CHOICES = (
        (POP_MUSIC, POP_MUSIC),
        (JAZZ_MUSIC, JAZZ_MUSIC),
        (RNB_MUSIC, RNB_MUSIC),
        (ROCK_MUSIC, ROCK_MUSIC),
        (COUNTRY_MUSIC, COUNTRY_MUSIC),
        (DANCE_MUSIC, DANCE_MUSIC),
        (HIP_HOP_MUSIC, HIP_HOP_MUSIC),
        (OTHER_MUSIC, OTHER_MUSIC)
    )

    album_name = models.CharField(
        max_length=30,
        unique=True,
        blank=False
    )

    artist = models.CharField(
        max_length=30,
        blank=False
    )

    genre = models.CharField(
        max_length=30,
        choices=GENRE_CHOICES,
        blank=False
    )

    description = models.TextField(
        blank=True
    )

    image_url = models.URLField(
        blank=False
    )

    price = models.PositiveIntegerField(
        blank=False,
    )
