from rest_framework import generics
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from api.models import Seller
from api.serializer.seller import SellerSerializer


class SellerListView(generics.ListCreateAPIView):

    serializer_class = SellerSerializer

    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filter_fields = ('name',)
    # ordering_fields = ('sale__value', 'value')

    def get_queryset(self):
        # Duplicated
        # self.filter_backends = (DjangoFilterBackend, OrderingFilter)
        return Seller.objects.all()


class SellerView(generics.RetrieveUpdateDestroyAPIView):

    lookup_field = 'pk'
    serializer_class = SellerSerializer
    queryset = Seller.objects.all()
