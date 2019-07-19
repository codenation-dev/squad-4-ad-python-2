from django.contrib.auth.models import User

from api.models import Sale, Seller, Plan
from api.tests.base_api_test import BaseApiTest


class TestFixtures(BaseApiTest):
    """
    Teste de exemplo somente testar as fixtures básicas
    """

    def test_user_from_fixture(self):

        user = User.objects.filter(
            username="luan",
            email="luan@luan.com"
        ).exists()

        self.assertTrue(
            user
        )

    def test_seller_from_fixture(self):

        seller = Seller.objects.filter(
            name="Primeiro Vendedor",
            address="Joinville",
            cpf="12345678901"
        ).exists()

        self.assertTrue(
            seller
        )

    def test_plan_from_fixture(self):

        plan = Plan.objects.filter(
            name="Primeiro plano",
            min_value=4500.0
        )

        self.assertTrue(
            plan
        )

    def test_sale_from_fixture(self):

        SALE_EXISTS = False

        sale = Sale.objects.all().exists()

        self.assertEquals(
            sale,
            SALE_EXISTS,
            "Não deveria haver vendas"
        )
