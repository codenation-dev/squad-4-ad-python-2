from django.db import models


class Plan(models.Model):
    name = models.CharField("Nome", max_length=200)
    lower_percentage = models.DecimalField("Comissao Abaixo", max_digits=10, decimal_places=2)
    min_value = models.DecimalField("Meta", max_digits=10, decimal_places=2)
    upper_percentage = models.DecimalField("Comissao", max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Seller(models.Model):
    name = models.CharField("Nome", max_length=100)
    address = models.CharField("Endereço", max_length=200)
    telefone = models.CharField("Telefone", max_length=200)
    idade = models.IntegerField("Idade")
    email = models.EmailField("E-Mail", max_length=254)
    cpf = models.CharField("CPF", max_length=11)
    commission_plan = models.ForeignKey(Plan, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Sale(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.PROTECT)
    amount = models.DecimalField("Vendas", max_digits=10, decimal_places=2)
    year = models.IntegerField("Ano")
    month = models.IntegerField("Mês")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return
