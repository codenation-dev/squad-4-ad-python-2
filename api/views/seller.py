from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import generics
from rest_framework.filters import OrderingFilter

from api.models import Seller
from api.serializer.seller import SellerSerializer


class SellerListView(generics.ListCreateAPIView):
    """Vendedores


    Cadastro dos vendedores de telemarketing que irão receber comissões"""

    serializer_class = SellerSerializer

    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filter_fields = ("name",)

    def get_queryset(self):
        return Seller.objects.all()


class SellerView(generics.RetrieveUpdateDestroyAPIView):
    """Vendedor


    Cadastro de vendedor de telemarketing que vai receber comissões"""

    lookup_field = "pk"
    serializer_class = SellerSerializer
    queryset = Seller.objects.all()
