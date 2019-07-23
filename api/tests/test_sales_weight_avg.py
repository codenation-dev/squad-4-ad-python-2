from api.models import Seller, Plan, Sale
from api.tests.base_api_test import BaseApiTest

from api.views.check_comission import sales_weight_avg, get_seller_last_sales


class TestSalesWeightAvg(BaseApiTest):
    """
    Tests if weighted average is correct
    """
    def generate_const_sales(self, seller, year, amount):
        for month in range(1, 6):
            Sale.objects.create(
                seller=seller,
                amount=amount,
                year=year,
                month=month
            )

    def create_sale(self, seller, year, month, amount):
        return Sale.objects.create(
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

    def test_sales_weight_avg(self):
        CONSTANT_AMOUNT = 500
        MAX_LAST_SALES = 5

        seller = self.get_seller()

        self.generate_const_sales(seller=seller, year=2019, amount=CONSTANT_AMOUNT)

        last_sales = get_seller_last_sales(seller=seller, max_last_sales=MAX_LAST_SALES)

        sale_weighted_avg = sales_weight_avg(sales=last_sales)

        self.assertEquals(
            sale_weighted_avg,
            CONSTANT_AMOUNT
        )

    def test_const_sales_weight_avg(self):
        MAX_LAST_SALES = 5
        YEAR = 2019
        JANUARY = 1
        FEBRUARY = 2

        seller = self.get_seller()

        january_sale = self.create_sale(seller=seller, month=JANUARY, year=YEAR, amount=4500)
        february_sale = self.create_sale(seller=seller, month=FEBRUARY, year=YEAR, amount=6700)

        january_weight = 1

        february_weight = 2

        weights_sum = january_weight + february_weight

        weighted_avg = ((january_sale.amount * january_weight) + (february_sale.amount * february_weight)) / weights_sum

        last_sales = get_seller_last_sales(seller=seller, max_last_sales=MAX_LAST_SALES)

        sale_weighted_avg = sales_weight_avg(sales=last_sales)

        self.assertEquals(
            sale_weighted_avg,
            weighted_avg
        )
