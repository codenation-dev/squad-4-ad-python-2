from rest_framework import serializers
from api.models.seller import Seller


class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller

        fields = ["pk", "name", "address", "phone", "birthday", "email", "cpf", "plan"]
