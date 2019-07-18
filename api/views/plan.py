from rest_framework import generics

from api.models.plan import Plan
from api.serializer.plan import PlanSerializer


class PLanListView(generics.ListCreateAPIView):

    serializer_class = PlanSerializer

    def get_queryset(self):
        return Plan.objects.all()


class PlanView(generics.RetrieveUpdateDestroyAPIView):

    lookup_field = 'pk'
    serializer_class = PlanSerializer
    queryset = Plan.objects.all()
