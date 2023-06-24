from django.db import models

from fruitipedia_app.fruitipedia import validators


class Fruit(models.Model):
    name = models.CharField(blank=False, max_length=30,
                            validators=[validators.min_name_length_validator, validators.validate_name_letters])

    image_url = models.URLField(blank=False)

    description = models.TextField(blank=False)

    nutrition = models.TextField(blank=True, null=True)
