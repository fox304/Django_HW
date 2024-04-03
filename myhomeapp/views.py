import logging

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from myhomeapp.models import Client, Product, Order

logger = logging.getLogger(__name__)


def main_page(request):
    logger.info("Main page called")
    return HttpResponse("<h1>Лучший магазин игрушек </h1>")


def about(request):
    logger.info("About page called")
    return HttpResponse("<ol>"
                        "   <li><b>Адрес:</b> Лапландия</li> "
                        "   <li><b>Тел:</b> +9999999999</li> "
                        "   <li><b>Почта:</b> ...@...com</li> "
                        "   <li><b>Режим работы:</b> круглые сутки</li>"
                        "</ol>")


def read_home_table(request):
    """сделал пробные запросы"""

    clients = Client.objects.all()
    clients = [f'{i}<br>' for i in clients]

    products = Product.objects.all()
    products = [f'{i}<br>' for i in products]

    order = Order.objects.all()
    order = [f'{i}<br>' for i in order]

    select_ = Client.objects.get(pk=4).product_id.all()

    select_ = Product.objects.get(pk=4).order_set.all()

    select_ = [f'{i}<br>' for i in select_]

    # заменить для проверки в return на clients,products или order
    return HttpResponse(select_)


