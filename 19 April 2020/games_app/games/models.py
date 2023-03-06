from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Profile(models.Model):
    email = models.EmailField(
        blank=False
    )
    age = models.IntegerField(
        validators=[MinValueValidator(12, "Age must be at least 12!")],
        blank=False
    )
    password = models.CharField(
        max_length=30,
        blank=False
    )
    first_name = models.CharField(
        max_length=30,
        blank=True
    )
    last_name = models.CharField(
        max_length=30,
        blank=True
    )
    profile_picture = models.URLField(
        blank=True
    )


class Game(models.Model):
    CATEGORY_CHOICES = (
        ('Action', 'Action'),
        ('Adventure', 'Adventure'),
        ('Puzzle', 'Puzzle'),
        ('Strategy', 'Strategy'),
        ('Sports', 'Sports'),
        ('Board/Card Game', 'Board/Card Game'),
        ('Other', 'Other'),
    )

    title = models.CharField(
        max_length=30,
        unique=True,
        blank=False
    )
    category = models.CharField(
        max_length=15,
        choices=CATEGORY_CHOICES,
        blank=False
    )
    rating = models.FloatField(
        validators=[MinValueValidator(0.1), MaxValueValidator(5.0, "Rating must be between 0.1 and 5.0!")],
        blank=False
    )
    max_level = models.IntegerField(
        validators=[MinValueValidator(1, 'Level must be at least 1!')],
        blank=True
    )
    image_url = models.URLField(
        blank=False
    )
    summary = models.TextField(
        blank=True
    )
