from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["POST"])
def check_comission_view(request):
    """
    TODO

    Verifica se é necessário enviar notificação para tal vendedor.
    De acordo com a descrição do projeto no exemplo sobre a /check_commision
    """
    data = request.data

    return Response({
        "should_notify": True or False
    })
