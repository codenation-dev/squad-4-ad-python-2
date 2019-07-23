from django.urls import reverse
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT, HTTP_404_NOT_FOUND)

from api.models import Seller, Plan
from api.tests.base_api_test import BaseApiTest


class TestViewSeller(BaseApiTest):
    """
    Tests the seller viewset
    """

    url_list_post = reverse("sellers_list")

    def test_get_list(self):
        request = self.client.get(self.url_list_post)
        self.assertEquals(request.status_code, HTTP_200_OK)

    def test_create(self):
        data = {
            "name": "Seller AA",
            "address": "rua A1",
            "phone": "+5546984023419",
            "birthday": "1990-01-01",
            "email": "aa@mail.com",
            "cpf": "12345678901",
            "plan": 1
        }

        request = self.client.post(path=self.url_list_post, data=data)

        self.assertEquals(request.status_code, HTTP_201_CREATED)

    def test_get_seller(self):
        plan = Plan.objects.get(id=1)
        seller = Seller.objects.create(
            **{
                "name": "Seller BB",
                "address": "rua B1",
                "phone": "+5546984023419",
                "birthday": "1990-01-02",
                "email": "bb@mail.com",
                "cpf": "22345678901",
                "plan": plan
            }
        )

        url = reverse("sellers", kwargs={"pk": seller.id})

        request = self.client.get(path=url)

        data = request.data

        self.assertEquals(seller.name, data.get("name"))
        self.assertEquals(seller.address, data.get("address"))
        self.assertEquals(seller.phone, data.get("phone"))
        self.assertEquals(seller.birthday, data.get("birthday"))
        self.assertEquals(seller.cpf, data.get("cpf"))
        self.assertEquals(seller.plan.pk, data.get("plan"))

    def test_update_seller(self):
        seller_data = {
            "name": "Seller CC",
            "address": "rua C1",
            "phone": "+5546984023419",
            "birthday": "1990-01-02",
            "email": "cc@mail.com",
            "cpf": "33345678901",
            "plan": Plan.objects.get(id=1)
        }
        seller = Seller.objects.create(**seller_data)

        seller_updated_data = {

            "name": "Seller CC3",
            "address": "rua C3",
            "phone": "+5546984023433",
            "birthday": "1993-03-03",
            "email": "cc3@mail.com",
            "cpf": "33345678933",
            "plan": 1
        }

        url = reverse("sellers", kwargs={"pk": seller.id})

        request = self.client.put(path=url, data=seller_updated_data)
        self.assertEquals(request.status_code, HTTP_200_OK)

        data = request.data

        self.assertEquals(seller_updated_data["name"], data.get("name"))
        self.assertEquals(seller_updated_data["address"], data.get("address"))
        self.assertEquals(seller_updated_data["phone"], data.get("phone"))
        self.assertEquals(seller_updated_data["birthday"], data.get("birthday"))
        self.assertEquals(seller_updated_data["cpf"], data.get("cpf"))
        self.assertEquals(seller_updated_data["plan"], data.get("plan"))

    def test_delete_seller(self):
        plan = Plan.objects.get(id=1)
        seller = Seller.objects.create(
            **{
                "name": "Seller BB",
                "address": "rua B1",
                "phone": "+5546984023419",
                "birthday": "1990-01-02",
                "email": "bb@mail.com",
                "cpf": "22345678901",
                "plan": plan
            }
        )

        url = reverse("sellers", kwargs={"pk": seller.id})

        delete_request = self.client.delete(path=url)

        self.assertEquals(delete_request.status_code, HTTP_204_NO_CONTENT)

        get_request = self.client.get(path=url)

        self.assertEquals(get_request.status_code, HTTP_404_NOT_FOUND)
