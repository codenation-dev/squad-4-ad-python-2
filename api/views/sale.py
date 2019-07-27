from rest_framework import generics

from api.models import Sale
from api.serializer.sale import SaleSerializer


class SaleListView(generics.ListCreateAPIView):
    """Vendas mensais


    Registrar o valor das vendas mensais de cada vendedor para que o sistema possa calcular a comissão de acordo com o plano de comissão escolhido"""

    serializer_class = SaleSerializer

    def get_queryset(self):
        return Sale.objects.all()


class SaleView(generics.RetrieveUpdateDestroyAPIView):
    """Venda mensal


    Gerencia o registro da venda mensal de cada vendedor para que o sistema possa calcular a comissão de acordo com o plano de comissão escolhido"""

    lookup_field = "pk"
    serializer_class = SaleSerializer
    queryset = Sale.objects.all()
