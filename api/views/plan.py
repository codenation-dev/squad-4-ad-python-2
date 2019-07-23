from rest_framework import generics

from api.models.plan import Plan
from api.serializer.plan import PlanSerializer


class PLanListView(generics.ListCreateAPIView):
    """ Cadastro dos planos de comissões para que os vendedores possam escolher qual o melhor plano para eles.
Cada plano possui dum nível básico de remuneração e outro nível maior quando a meta de vendas é cumprida

GET retorna a lista de todos os planos
POST inclusão de novo plano"""

    serializer_class = PlanSerializer

    def get_queryset(self):
        return Plan.objects.all()


class PlanView(generics.RetrieveUpdateDestroyAPIView):
    """ Cadastro dos planos de comissões para que os vendedores possam escolher qual o melhor plano para eles.
Cada plano possui dum nível básico de remuneração e outro nível maior quando a meta de vendas é cumprida

{id}: Código do plano

GET Retorna os dados do plano {id}
PUT Atualização dos dados do plano {id}
PATCH Atualização parcial dos dados do plano {id}
DELETE Exclusão do registro"""

    lookup_field = 'pk'
    serializer_class = PlanSerializer
    queryset = Plan.objects.all()
