from django.db import models

from api.models.seller import Seller

from televendas.settings import DEFAULT_MAX_DIGITS, DEFAULT_DECIMAL_PLACES

DEFAULT_COMISSION_VALUE = 0.0


class Sale(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.PROTECT)

    year = models.IntegerField()

    month = models.IntegerField()

    amount = models.DecimalField(
        max_digits=DEFAULT_MAX_DIGITS, decimal_places=DEFAULT_DECIMAL_PLACES
    )

    comission_value = models.DecimalField(
        max_digits=DEFAULT_MAX_DIGITS,
        decimal_places=DEFAULT_DECIMAL_PLACES,
        default=DEFAULT_COMISSION_VALUE,
    )
