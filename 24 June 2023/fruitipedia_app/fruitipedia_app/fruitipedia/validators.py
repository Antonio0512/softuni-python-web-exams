from django.core.exceptions import ValidationError


def min_name_length_validator(value):
    if len(value) < 2:
        return ValidationError("Your name must be at least 2 characters long.")


def validate_name_letters(value):
    if not value.isalpha():
        raise ValidationError("Fruit name should contain only letters!")
