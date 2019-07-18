from django.contrib.auth.models import User
from django.http import HttpResponse
from rest_framework import viewsets

from api.models import Plan, Seller, Sale
from api.serializer import UserSerializer, PlanSerializer, SellerSerializer, SaleSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PlanViewSet(viewsets.ModelViewSet):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer


class SellerViewSet(viewsets.ModelViewSet):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer


class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer


def vendedores(request):
    return HttpResponse("OK")


def sellers(request):
    return HttpResponse("OK")


def comissions(request):
    return HttpResponse("OK")


def check_commision(request):
    return HttpResponse("OK")
