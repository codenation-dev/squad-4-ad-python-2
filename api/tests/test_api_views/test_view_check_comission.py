from django.urls import reverse
from django.core import mail

from api.models import Sale, Seller, Plan
from api.tests.base_api_test import BaseApiTest


class TestViewCheckComision(BaseApiTest):
    """
    Tests for view check_comission_view
    """

    url = reverse("check_comission")

    @staticmethod
    def generate_sales(seller, year, amount):
        for month in range(1, 6):
            Sale.objects.create(seller=seller, amount=amount, year=year, month=month)

    @staticmethod
    def get_seller():
        return Seller.objects.create(
            name="test",
            address="teste",
            phone="47",
            birthday="2000-01-01",
            email="fake@mail.com",
            cpf="12345678901",
            plan=Plan.objects.all().first(),
        )

    def test_no_notification(self):
        AMOUNT = 500

        seller = self.get_seller()
        data = {"seller": seller.id, "amount": AMOUNT}
        request = self.client.post(
            path=self.url, data=data, content_type="application/json"
        )
        data = request.data
        email_sent = data.get("email_sent")

        self.assertFalse(email_sent)

    def test_notification(self):
        AMOUNT = 500
        LOWER_AMOUNT = AMOUNT - (AMOUNT / 9)

        seller = self.get_seller()
        self.generate_sales(seller=seller, year=2019, amount=AMOUNT)
        data = {"seller": seller.id, "amount": LOWER_AMOUNT}
        request = self.client.post(path=self.url, data=data)
        data = request.data
        email_sent = data.get("email_sent")

        self.assertTrue(email_sent)
        self.assertEqual(len(mail.outbox), 1)
