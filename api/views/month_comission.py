from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["POST"])
def month_comission_view(request):
    """
    TODO

    Criar uma venda para o vendedor
    De acordo com a descrição da view /month_comission em description.py

    """
    data = request.data

    serializer = "Utilizar um serializer para registrar a respectiva venda"

    return Response("created")
