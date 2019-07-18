from django.db import models

from api.models.plan import Plan

NAME_MAX_LENGTH = 100
ADDRESS_MAX_LENGTH = 1000
PHONE_MAX_LENGTH = 20
EMAIL_MAX_LENGTH = 100
CPF_MAX_LENGTH = 11


class Seller(models.Model):
    name = models.CharField(max_length=NAME_MAX_LENGTH)

    address = models.CharField(max_length=ADDRESS_MAX_LENGTH)

    phone = models.CharField(max_length=PHONE_MAX_LENGTH)

    birthday = models.DateField()

    email = models.EmailField(max_length=EMAIL_MAX_LENGTH)

    cpf = models.CharField(max_length=CPF_MAX_LENGTH)

    plan = models.ForeignKey(Plan, on_delete=models.PROTECT)
