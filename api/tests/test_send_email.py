from django.core import mail

from api.models import Seller, Plan
from api.tests.base_api_test import BaseApiTest
from api.views.check_comission import send_email_sale_notification


class TestMail(BaseApiTest):
    """
    Tests if email is being send
    """

    def test_no_email_sent(self):
        self.assertEqual(len(mail.outbox), 0)

    def test_email_sent(self):
        seller = Seller.objects.create(
            name="test",
            address="teste",
            phone="47",
            birthday="2000-01-01",
            email="fake@mail.com",
            cpf="12345678901",
            plan=Plan.objects.all().first(),
        )
        send_email_sale_notification(seller=seller)
        self.assertEqual(len(mail.outbox), 1)
