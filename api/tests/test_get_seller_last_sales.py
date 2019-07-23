from api.models import Seller, Plan, Sale
from api.tests.base_api_test import BaseApiTest

from api.views.check_comission import get_seller_last_sales


class TestGetSellerLastSales(BaseApiTest):
    """
    Tests if weighted average is correct
    """
    def generate_sales(self, seller, year, amount=500):

        for month in range(1, 13):
            Sale.objects.create(
                seller=seller,
                amount=amount,
                year=year,
                month=month
            )

    def get_seller(self):

        return Seller.objects.create(
            name="test",
            address="teste",
            phone="47",
            birthday='2000-01-01',
            email="fake@mail.com",
            cpf="12345678901",
            plan=Plan.objects.all().first()
        )

    def test_get_no_sales(self):

        MAX_LAST_SALES = 5

        seller = self.get_seller()

        last_sales = get_seller_last_sales(seller=seller, max_last_sales=MAX_LAST_SALES)

        self.assertFalse(last_sales)

    def test_get_sales(self):

        MAX_LAST_SALES = 5

        seller = self.get_seller()

        self.generate_sales(seller=seller, year=2019)

        last_sales_length = len(get_seller_last_sales(seller=seller, max_last_sales=MAX_LAST_SALES))

        self.assertEquals(
            last_sales_length,
            MAX_LAST_SALES
        )
