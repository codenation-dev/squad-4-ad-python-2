from rest_framework import generics

from api.models import Sale
from api.serializer.sale import SaleSerializer


class SaleListView(generics.ListCreateAPIView):

    serializer_class = SaleSerializer

    def get_queryset(self):
        return Sale.objects.all()


class SaleView(generics.RetrieveUpdateDestroyAPIView):

    lookup_field = 'pk'
    serializer_class = SaleSerializer
    queryset = Sale.objects.all()
