from decimal import Decimal

from api.models import Sale, Seller
from api.tests.base_api_test import BaseApiTest


class TestViewCheckComision(BaseApiTest):
    """
    Tests for sales
    """

    def get_seller(self):
        return Seller.objects.all().first()

    def test_calculate_comission(self):
        DIFFERENCE = Decimal(100.0)
        seller = self.get_seller()
        plan = seller.plan
        min_value = plan.min_value

        lower_amount = min_value - DIFFERENCE
        lower_comission = lower_amount * plan.lower_percentage
        sale_lower_comission = Sale.calculate_comission(plan=plan, amount=lower_amount)
        self.assertEquals(lower_comission, sale_lower_comission)

        upper_amount = min_value
        upper_comission = upper_amount * plan.upper_percentage
        sale_upper_comission = Sale.calculate_comission(plan=plan, amount=upper_amount)
        self.assertEquals(upper_comission, sale_upper_comission)
