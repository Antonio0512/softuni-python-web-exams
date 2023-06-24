from django.db import models
from . import validators


class UserProfile(models.Model):
    first_name = models.CharField(blank=False, max_length=25,
                                  validators=[validators.min_firstname_length_validator,
                                              validators.validate_first_letter])

    last_name = models.CharField(blank=False, max_length=35,
                                 validators=[validators.min_lastname_length_validator,
                                             validators.validate_first_letter])

    email = models.EmailField(blank=False, max_length=40)

    password = models.CharField(blank=False, max_length=20, validators=[validators.validate_password_length])

    image_url = models.URLField(blank=True, null=True)

    age = models.IntegerField(blank=True, null=True, default=18)
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
