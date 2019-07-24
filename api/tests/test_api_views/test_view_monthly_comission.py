from django.urls import reverse
from api.models import Sale, Seller, Plan
from api.tests.base_api_test import BaseApiTest


class TestViewMontlhlyComision(BaseApiTest):
    """
    Tests for view check_comission_view
    """

    def create_sale(self, seller, year, month, amount):
        return Sale.objects.create(
            seller=seller,
            amount=amount,
            year=year,
            month=month
        )

    def create_seller(self, name):
        return Seller.objects.create(
            name=name,
            address="teste",
            phone="47",
            birthday='2000-01-01',
            email="fake@mail.com",
            cpf="12345678901",
            plan=Plan.objects.all().first()
        )

    def test_no_monthly_comission(self):
        MONTH = 4
        url = reverse("monthly_comission", kwargs={"month": MONTH})
        request = self.client.get(path=url)
        data = request.data
        self.assertFalse(len(data))

    def test_monthly_comission(self):
        MONTH = 1
        YEAR = 2019
        FIRST_SELLER_AMOUNT = 200
        SECOND_SELLER_AMOUNT = 300

        first_seller = self.create_seller(name="First seller")
        self.create_sale(seller=first_seller, year=YEAR, month=MONTH, amount=FIRST_SELLER_AMOUNT)

        second_seller = self.create_seller(name="Second seller")
        self.create_sale(seller=second_seller, year=YEAR, month=MONTH, amount=SECOND_SELLER_AMOUNT)

        url = reverse("monthly_comission", kwargs={"month": MONTH})
        request = self.client.get(path=url)

        data = request.data

        self.assertEquals(
            data[0]['name'],
            second_seller.name
        )

        self.assertEquals(
            data[1]['name'],
            first_seller.name
        )
