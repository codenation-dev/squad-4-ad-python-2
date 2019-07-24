from decimal import Decimal

from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from django.core.mail import send_mail
from django.template.loader import render_to_string

from api.models import Seller, Sale
from numpy import array, dtype, average

from televendas.settings import EMAIL_HOST_USER


@api_view(["POST"])
def check_comission_view(request):

    data = request.data

    seller_id = data.get('seller')
    amount = Decimal(data.get('amount'))

    seller = get_object_or_404(Seller, id=seller_id)

    email_sent = False

    if should_notify_user(seller=seller, amount=amount):
        send_email_sale_notification(seller=seller)
        email_sent = True

    return Response({"email_sent": email_sent})


def comission_weight_avg(sales: list):
    """
    Returns the comission_vale weighted average
    :param sales: list
    :return: Decimal
    """
    comission_values = array([sale['comission_value'] for sale in sales], dtype=dtype(float))

    weights = [sale['weight'] for sale in sales]

    weighted_avg = average(a=comission_values, weights=weights)

    return Decimal(weighted_avg)


def percent(number: int = 10):
    """
    Considers number as integer percentage and converts to standard percentage
    :param number:
    :return: float
    """
    return Decimal(number) / 100


def sale_percentage(sales_comission_value_avg: Decimal, percentage: Decimal):
    return sales_comission_value_avg * percentage


def should_notify_user(seller: Seller, amount: Decimal):
    """
    Checks if user should or should not be notified about under performing sales,
    according to specified rules.
    :param seller: Seller
    :param amount: Decimal
    :return: boolean
    """
    MAX_LAST_SALES = 5
    PERCENTAGE = percent(10)
    comission_value = Sale.calculate_comission(plan=seller.plan, amount=amount)
    
    weight_sales = get_seller_last_sales(seller=seller, max_last_sales=MAX_LAST_SALES)

    seller_has_sales = len(weight_sales)
    if not seller_has_sales:
        return False

    comissions_weighted_average = comission_weight_avg(sales=weight_sales)

    percentage_cut = sale_percentage(sales_comission_value_avg=comissions_weighted_average, percentage=PERCENTAGE)

    comissions_weighted_average_minus_percentage_cut = comissions_weighted_average - percentage_cut

    return True if comission_value < comissions_weighted_average_minus_percentage_cut else False


def get_seller_last_sales(seller: Seller, max_last_sales: int):
    """
    Returns the seller last max_last_sales
    :param seller: Seller
    :param max_last_sales:
    :return: list
    """
    last_sales = Sale.objects.filter(seller=seller).order_by('-year', '-month')[:max_last_sales]

    sales_ordered_by_comission_value = sorted(last_sales, key=lambda x: x.comission_value)

    weight_sales_by_comission_value = [{
        "comission_value": sale.comission_value,
        "weight": weight
    } for weight, sale in enumerate(sales_ordered_by_comission_value, 1)]

    return weight_sales_by_comission_value


def send_email_sale_notification(seller: Seller):
    """
    Sends e-mail to seller about under performing sales.
    :param seller: Seller
    :return:
    """

    subject = 'Suas vendas estão abaixo da média!'
    from_email = EMAIL_HOST_USER

    recipient_list = [seller.email]

    context = {
        "title": subject,
        "seller_name": seller.name
    }

    msg_txt = render_to_string('sales_value_email.txt', context=context)
    msg_html = render_to_string('sales_value_email.html', context=context)

    send_mail(
        subject=subject,
        message=msg_txt,
        from_email=from_email,
        recipient_list=recipient_list,
        fail_silently=False,
        html_message=msg_html
    )
