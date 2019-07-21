from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from django.core.mail import send_mail
from django.template.loader import render_to_string

from api.models import Seller, Sale
from numpy import array, dtype, average

from televendas.settings import DEBUG, EMAIL_HOST_USER


@api_view(["POST"])
def check_comission_view(request):

    data = request.data

    seller_id = data.get('seller')
    amount = data.get('amount')

    seller = get_object_or_404(Seller, id=seller_id)

    email_sent = False

    if should_notify_user(seller=seller, amount=amount):
        send_email_sale_notification(seller=seller)
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
    """
    Checks if user should or should not be notified about under performing sales,
    according to specified rules.
    :param seller: Seller
    :param amount: int float
    :return: boolean
    """

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


def send_email_sale_notification(seller):
    """
    Sends e-mail to seller about under performing sales.
    :param seller: Seller
    :return:
    """
    if DEBUG:
        print("EMAIL WON'T BE SEND WHILE DEBUGGING")
        return

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
