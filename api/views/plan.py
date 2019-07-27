from rest_framework import generics

from api.models.plan import Plan
from api.serializer.plan import PlanSerializer


class PLanListView(generics.ListCreateAPIView):
    """Planos de Comissões


    Cadastro dos planos de comissões para que os vendedores possam escolher qual o melhor plano para eles.
    Cada plano possui dum nível básico de remuneração e outro nível maior quando a meta de vendas é cumprida"""

    serializer_class = PlanSerializer

    def get_queryset(self):
        return Plan.objects.all()


class PlanView(generics.RetrieveUpdateDestroyAPIView):
    """Plano de comissão


    Gerenciamento do plano de comissão"""

    lookup_field = "pk"
    serializer_class = PlanSerializer
    queryset = Plan.objects.all()
