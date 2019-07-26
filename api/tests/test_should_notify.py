from decimal import Decimal

from api.tests.base_api_test import BaseApiTest
from api.models import Seller, Plan, Sale
from api.views.check_comission import should_notify_user


class TestShouldNotify(BaseApiTest):
    """
    Tests if email is being send
    """

    def generate_sales(self, seller, year, amount):
        for month in range(1, 6):
            Sale.objects.create(seller=seller, amount=amount, year=year, month=month)

    def get_seller(self):
        return Seller.objects.create(
            name="test",
            address="teste",
            phone="47",
            birthday="2000-01-01",
            email="fake@mail.com",
            cpf="12345678901",
            plan=Plan.objects.all().first(),
        )

    def test_should_not_notify_no_sales(self):
        AMOUNT = Decimal(500.0)
        seller = self.get_seller()
        self.assertFalse(should_notify_user(seller=seller, amount=AMOUNT))

    def test_should_not_notify(self):
        AMOUNT = Decimal(500.0)
        seller = self.get_seller()
        self.generate_sales(seller=seller, year=2018, amount=AMOUNT)
        self.assertFalse(should_notify_user(seller=seller, amount=AMOUNT))

    def test_should_notify(self):
        AMOUNT = 1000
        LOWER_AMOUNT = Decimal(100)
        seller = self.get_seller()
        self.generate_sales(seller=seller, year=2019, amount=AMOUNT)
        self.assertTrue(should_notify_user(seller=seller, amount=LOWER_AMOUNT))
