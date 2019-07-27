from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models

from televendas.settings import (
    DEFAULT_MAX_DIGITS,
    DEFAULT_DECIMAL_PLACES,
    DEFAULT_PERCENT_DECIMAL_PLACES,
)

NAME_MAX_LENGTH = 50


class Plan(models.Model):
    name = models.CharField(max_length=NAME_MAX_LENGTH)
    lower_percentage = models.DecimalField(
        max_digits=DEFAULT_MAX_DIGITS,
        decimal_places=DEFAULT_PERCENT_DECIMAL_PLACES,
        validators=[MinValueValidator(Decimal("0.0"))],
    )
    min_value = models.DecimalField(
        max_digits=DEFAULT_MAX_DIGITS,
        decimal_places=DEFAULT_DECIMAL_PLACES,
        validators=[MinValueValidator(Decimal("0.0"))],
    )
    upper_percentage = models.DecimalField(
        max_digits=DEFAULT_MAX_DIGITS,
        decimal_places=DEFAULT_PERCENT_DECIMAL_PLACES,
        validators=[MinValueValidator(Decimal("0.0"))],
    )

    def __str__(self):
        return f"Plan - {self.name}"
