from django.contrib import admin

from myhomeapp.models import Client, Product, Order


@admin.action(description="скидка для тех у кого имя с буквы C")
def prizes(modeladmin, request, queryset):
    """ Клиенты, у которых ммя начинается с буквы С
        получают скидку 50.
        В итоге во всех заказах сумма уменьшается на 50
    """
    clients = queryset.filter(name_client__startswith='C')
    for client in clients:
        all_orders_client = client.product_id.all()
        for order in all_orders_client:
            order.total_amount_of_the_order = order.sum_order(-50)


@admin.action(description="уменьшаем стоимость товара")
def discount(modeladmin, request, queryset):
    """
     Если количество больше 500, то стоимость товара
    уменьшаем на один
    """
    products = queryset.filter(quantity__gt=500)
    for product in products:
        product.price -= 1
        product.save()


class ClientAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name_client', 'phone_number', 'address')
    ordering = ('phone_number',)
    list_filter = ('name_client', 'phone_number')
    search_fields = ('address',)
    search_help_text = "поиск по полю адрес"
    actions = [prizes]


class OrderAdmin(admin.ModelAdmin):
    list_display = ('pk', 'total_amount_of_the_order', 'customer_order')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name_of_item', 'quantity', 'price')
    actions = [discount]


admin.site.register(Client, ClientAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
