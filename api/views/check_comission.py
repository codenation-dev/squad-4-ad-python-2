from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from api.models import Seller, Sale
from numpy import array, dtype, average


@api_view(["POST"])
def check_comission_view(request):

    data = request.data

    seller_id = data.get('seller')
    amount = data.get('amount')

    seller = get_object_or_404(Seller, id=seller_id)

    email_sent = False

    if should_notify_user(seller=seller, amount=amount):
        send_mail_sale_notification(seller=seller)
        email_sent = True

    return Response({"email_sent": email_sent})


def sales_weight_avg(sales, percentage):
    """
    Returns the sales (weighted average) - percentage
    :param sales: list
    :param percentage: number
    :return: numpy.float64
    """
    sales_values = array([sale['amount'] for sale in sales], dtype=dtype(float))

    weights = [sale['weight'] for sale in sales]

    weighted_avg = average(a=sales_values, weights=weights)

    percentage_cut = weighted_avg / percentage

    weighted_avg_minus_percentage = weighted_avg - percentage_cut

    return weighted_avg_minus_percentage


def should_notify_user(seller, amount):

    MAX_LAST_SALES = 5
    PERCENTAGE = 10

    last_sales = Sale.objects.filter(seller=seller).order_by('-year', '-month')[:MAX_LAST_SALES]

    sales_ordered_by_value = sorted(last_sales, key=lambda x: x.amount)

    weight_sales = [{
        "amount": sale.amount,
        "weight": weight
    } for weight, sale in enumerate(sales_ordered_by_value, 1)]

    sales_weighted_average = sales_weight_avg(sales=weight_sales, percentage=PERCENTAGE)

    return True if amount < sales_weighted_average else False


def send_mail_sale_notification(seller):
    """ TODO
    Sends a notification to the user, about under performing sales average
    """
    pass
