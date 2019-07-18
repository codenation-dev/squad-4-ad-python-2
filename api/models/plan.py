from django.db import models

from televendas.settings import DEFAULT_MAX_DIGITS, DEFAULT_DECIMAL_PLACES

NAME_MAX_LENGTH = 50


class Plan(models.Model):
    name = models.CharField(max_length=NAME_MAX_LENGTH)

    lower_percentage = models.DecimalField(
        max_digits=DEFAULT_MAX_DIGITS, decimal_places=DEFAULT_DECIMAL_PLACES
    )

    min_value = models.DecimalField(
        max_digits=DEFAULT_MAX_DIGITS, decimal_places=DEFAULT_DECIMAL_PLACES
    )

    upper_percentage = models.DecimalField(
        max_digits=DEFAULT_MAX_DIGITS, decimal_places=DEFAULT_DECIMAL_PLACES
    )
