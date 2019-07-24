from datetime import datetime

from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import Sale, Seller


@api_view(["GET"])
def monthly_comission_view(request, month):
    """Recuperar lista de vendedores ordenados pelo valor da comissão


    Recupera Lista de vededores ordenados por valor das vendas no mês informado
    :param month: Mês do Filtro
    :return: List<>
    """
    CURRENT_YEAR = datetime.now().year
    r = []
    sellers = Seller.objects.all()

    for sale in sellers:
        try:
            sale = Sale.objects.get(year=CURRENT_YEAR, month=month, seller=sale.pk)
            r.append({"id": sale.pk, "name": sale.seller.name, "comission": sale.comission_value})
        except (Sale.DoesNotExist, Sale.MultipleObjectsReturned) as e:
            print(f"{e}")

    return Response(sorted(r, key=lambda i: i['comission'], reverse=True))
