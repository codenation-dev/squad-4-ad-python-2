from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import Sale, Seller


@api_view(["GET"])
def monthly_comission_view(request, month):
    r = []
    sellers = Seller.objects.all()

    for sell in sellers:
        try:
            sale = Sale.objects.filter(month=month, seller=sell.pk)[0]
            r.append({"id": sell.pk, "nome": sell.name, "comission": sale.comission_value})
        except:
            r.append({"id": sell.pk, "nome": sell.name, "comission": 0.0})

    return Response(sorted(r, key=lambda i: i['comission'], reverse=True))
