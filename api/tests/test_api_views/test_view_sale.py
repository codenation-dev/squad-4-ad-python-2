import decimal

from django.urls import reverse
from rest_framework.status import (HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_404_NOT_FOUND)

from api.models import Seller, Sale
from api.tests.base_api_test import BaseApiTest


class TestViewSale(BaseApiTest):
    url_list_post = reverse("sales_list")

    def test_get_list(self):
        request = self.client.get(self.url_list_post)
        self.assertEqual(request.status_code, HTTP_200_OK)

    def test_create(self):
        data = {
            "seller": 1,
            "year": 2019,
            "month": 1,
            "amount": 1000.90
        }
        request = self.client.post(path=self.url_list_post, data=data)
        self.assertEqual(request.status_code, HTTP_201_CREATED)

    def test_get_sale(self):
        seller = Seller.objects.get(id=1)
        sale = Sale.objects.create(**{
            "seller": seller,
            "year": 2019,
            "month": 1,
            "amount": decimal.Decimal(0.1)
        })
        url = reverse("sales", kwargs={"pk": sale.id})
        request = self.client.get(path=url)
        data = request.data

        self.assertEqual(data.get("seller"), sale.seller.pk)
        self.assertEqual(data.get("year"), sale.year)
        self.assertEqual(data.get("month"), sale.month)
        self.assertEqual(float(data.get("amount")), sale.amount)

    def test_update_sale(self):
        seller = Seller.objects.get(id=1)
        sale = Sale.objects.create(**{
            "seller": seller,
            "year": 2019,
            "month": 1,
            "amount": decimal.Decimal(0.1)
        })
        sale_put = {
            "seller": seller.pk,
            "year": 2019,
            "month": 1,
            "amount": 1000.90
        }
        url = reverse("sales", kwargs={"pk": sale.id})
        request = self.client.put(path=url, data=sale_put)
        data = request.data

        self.assertEqual(request.status_code, HTTP_200_OK)
        self.assertEquals(sale_put["amount"], float(data.get("amount")))

    def test_delete_sale(self):
        seller = Seller.objects.get(id=1)
        sale = Sale.objects.create(**{
            "seller": seller,
            "year": 2019,
            "month": 1,
            "amount": decimal.Decimal(0.1)
        })
        url = reverse("sales", kwargs={"pk": sale.id})

        delete_request = self.client.delete(path=url)
        self.assertEquals(delete_request.status_code, HTTP_204_NO_CONTENT)

        get_request = self.client.get(path=url)
        self.assertEquals(get_request.status_code, HTTP_404_NOT_FOUND)
