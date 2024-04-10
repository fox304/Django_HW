import datetime
import logging

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, View

from myhomeapp.forms import ImageForm
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


class ProductsList(TemplateView):
    template_name = 'myhomeapp/products.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # для получения данных за год, пол года, месяц
        t_year = datetime.datetime.now() - datetime.timedelta(days=365)
        half_year = datetime.datetime.now() - datetime.timedelta(days=180)
        t_day = datetime.datetime.now() - datetime.timedelta(days=30)

        orders_list = []
        products_list = []

        for period in t_year, half_year, t_day:
            pk = kwargs.get('client')
            products_unique = set()  # для получения уникальных данных
            orders = Order.objects.filter(customer_order__pk=pk)  # выборка заказов по клиенту
            orders = orders.filter(date_of_the_order__gte=period).order_by('date_of_the_order')

            # получение множества уникальных продуктов всех заказов клиента
            [products_unique.update(order.product_order.all()) for order in orders]

            orders_list.append(orders)
            products_list.append(products_unique)

        context['orders'] = orders_list
        context['products_unique'] = products_list
        context['client'] = Client.objects.get(pk=pk)
        return context


def home(request):
    return render(request, 'myhomeapp/toys.html')


def list_toys(request):
    toys = Product.objects.all()
    return render(request, 'myhomeapp/list_toys.html', {'toys': toys})


def load_photo(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.cleaned_data['product']
            photo = form.cleaned_data['photo']
            product.picture = photo  # запись фото в каталог
            product.save()  # запись фото в базу
            return render(request, 'myhomeapp/view_toy.html', {'prod': product})
    else:
        form = ImageForm()
    return render(request, 'myhomeapp/load_forms.html', {'form': form})
