from rest_framework import serializers
from api.models.sale import Sale


class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale

        fields = ["pk", "seller", "year", "month", "amount", "comission_value"]
