import datetime
from decimal import Decimal

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from api.models.seller import Seller
from televendas.settings import DEFAULT_MAX_DIGITS, DEFAULT_DECIMAL_PLACES

DEFAULT_COMISSION_VALUE = 0.0


class Sale(models.Model):
    MONTH = (
        (1, "Janeiro"),
        (2, "Fevereiro"),
        (3, "Março"),
        (4, "Abril"),
        (5, "Maio"),
        (6, "Junho"),
        (7, "Julho"),
        (8, "Agosto"),
        (9, "Setembro"),
        (10, "Outubro"),
        (11, "Novembro"),
        (12, "Dezembro"),
    )
    seller = models.ForeignKey(Seller, on_delete=models.PROTECT)

    year = models.IntegerField(validators=[MaxValueValidator(datetime.datetime.now().year), MinValueValidator(1990)])

    month = models.PositiveSmallIntegerField(choices=MONTH)

    amount = models.DecimalField(
        max_digits=DEFAULT_MAX_DIGITS, decimal_places=DEFAULT_DECIMAL_PLACES,
        validators=[MinValueValidator(Decimal('0.0'))]
    )

    comission_value = models.DecimalField(
        max_digits=DEFAULT_MAX_DIGITS,
        decimal_places=DEFAULT_DECIMAL_PLACES,
        default=DEFAULT_COMISSION_VALUE,
        editable=False,
    )

    class Meta:
        unique_together = ('seller', 'year', 'month')

    def __str__(self):
        return '{0}/{1} R$ {2}'.format(self.month, self.year, self.amount)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        pan = self.seller.plan

        if (self.amount >= pan.min_value):
            self.comission_value = self.amount * pan.upper_percentage / 100
        else:
            self.comission_value = self.amount * pan.lower_percentage / 100

        super(Sale, self).save()
