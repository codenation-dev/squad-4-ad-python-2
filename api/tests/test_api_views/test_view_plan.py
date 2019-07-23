from django.urls import reverse
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_404_NOT_FOUND,
    HTTP_204_NO_CONTENT,
)

from api.models import Plan
from api.tests.base_api_test import BaseApiTest


class TestViewPlan(BaseApiTest):
    """
    Tests the Plan viewset
    """

    url_list_post = reverse("plans_list")

    def test_get_list(self):
        request = self.client.get(self.url_list_post)
        self.assertEquals(request.status_code, HTTP_200_OK)

    def test_create(self):
        data = {
            "name": "test",
            "lower_percentage": 0.15,
            "min_value": 10000.00,
            "upper_percentage": 0.25,
        }

        request = self.client.post(path=self.url_list_post, data=data)

        self.assertEquals(request.status_code, HTTP_201_CREATED)

    def test_get_plan(self):

        plan = Plan.objects.create(
            **{
                "name": "plan",
                "lower_percentage": "0.1500",
                "min_value": "10000.00",
                "upper_percentage": "0.2500",
            }
        )

        url = reverse("plans", kwargs={"pk": plan.id})

        request = self.client.get(path=url)

        data = request.data

        self.assertEquals(plan.name, data.get("name"))

        self.assertEquals(plan.lower_percentage, data.get("lower_percentage"))

        self.assertEquals(plan.min_value, data.get("min_value"))

        self.assertEquals(plan.upper_percentage, data.get("upper_percentage"))

    def test_update_plan(self):
        plan_data = {
            "name": "plan",
            "lower_percentage": "0.1500",
            "min_value": "10000.00",
            "upper_percentage": "0.2500",
        }

        plan_updated_data = {
            "name": "updated plan",
            "lower_percentage": "0.2500",
            "min_value": "100000.00",
            "upper_percentage": "0.3500",
        }

        plan = Plan.objects.create(**plan_data)

        url = reverse("plans", kwargs={"pk": plan.id})

        request = self.client.put(path=url, data=plan_updated_data)

        data = request.data

        self.assertEquals(plan_updated_data["name"], data.get("name"))

        self.assertEquals(
            plan_updated_data["lower_percentage"], data.get("lower_percentage")
        )

        self.assertEquals(plan_updated_data["min_value"], data.get("min_value"))

        self.assertEquals(
            plan_updated_data["upper_percentage"], data.get("upper_percentage")
        )

    def test_delete_plan(self):
        plan_data = {
            "name": "plan",
            "lower_percentage": "0.1500",
            "min_value": "10000.00",
            "upper_percentage": "0.2500",
        }

        plan = Plan.objects.create(**plan_data)

        url = reverse("plans", kwargs={"pk": plan.id})

        delete_request = self.client.delete(path=url)

        self.assertEquals(delete_request.status_code, HTTP_204_NO_CONTENT)

        get_request = self.client.get(path=url)

        self.assertEquals(get_request.status_code, HTTP_404_NOT_FOUND)
