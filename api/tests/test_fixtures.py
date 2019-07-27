from django.contrib.auth.models import User

from api.models import Sale, Seller, Plan
from api.tests.base_api_test import BaseApiTest


class TestFixtures(BaseApiTest):
    """
    Teste de exemplo somente testar as fixtures básicas
    """

    def test_user_from_fixture(self):
        user = User.objects.filter(username="luan", email="luan@luan.com")
        self.assertTrue(user.exists())

    def test_seller_from_fixture(self):
        seller = Seller.objects.filter(
            name="Primeiro Vendedor", address="Joinville", cpf="12345678901"
        )
        self.assertTrue(seller.exists())

    def test_plan_from_fixture(self):
        plan = Plan.objects.filter(name="Primeiro plano", min_value=4500.0)
        self.assertTrue(plan.exists())

    def test_sale_from_fixture(self):
        SALE_EXISTS = False
        sale = Sale.objects.all()
        self.assertEquals(sale.exists(), SALE_EXISTS, "Não deveria haver vendas")
