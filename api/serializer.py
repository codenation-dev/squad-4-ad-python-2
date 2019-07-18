from django.contrib.auth.models import User
from rest_framework import serializers

from api.models import Plan, Seller, Sale


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


class PlanSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Plan
        fields = '__all__'
        ordering = ['nome']


class SellerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Seller
        fields = '__all__'


class SaleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sale
        fields = '__all__'
