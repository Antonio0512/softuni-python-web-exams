from django.core.exceptions import ValidationError


def validate_first_letter(value):
    if not value[0].isalpha():
        raise ValidationError("Your name must start with a letter!")


def validate_password_length(value):
    if len(value) < 8 or len(value) > 20:
        raise ValidationError("Password must be between 8 and 20 characters long.")


def min_firstname_length_validator(value):
    if len(value) < 2:
        return ValidationError("Your name must be at least 2 characters long.")


def min_lastname_length_validator(value):
    if len(value) < 1:
        return ValidationError("Your name must be at least 1 characters long.")
