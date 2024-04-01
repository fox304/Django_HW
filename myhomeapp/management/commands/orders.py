import random
from django.core.management import BaseCommand
from ...models import Order, Client, Product


class Command(BaseCommand):
    help = "Создаем базу наших заказов"

    def handle(self, *args, **options):
        clients = Client.objects.all()
        products = Product.objects.all()

        def fill_orders(order, selected_products):
            #  проходим по всем выбранным продуктам
            for product in selected_products:
                amount_of_product = product.quantity
                random_number_of_product = random.randrange(3)

                # проверяем на наличие товара в базе
                if amount_of_product - random_number_of_product < 0:
                    print("выберите меньше")
                else:
                    #  отнимаем из базы купленное количество товара
                    product.quantity_of_product_sold(random_number_of_product)

                    #  сумма купленного количества определенного товара
                    order.sum_order(product.price * random_number_of_product)

        for num_order in range(1, 30):
            years = random.randint(2023, 2024)
            months = random.randint(1, 12) if years == 2023 else random.randint(1, 3)
            days = random.randint(1, 28) if months == 2 else random.randint(1, 30)

            order = Order.objects.create(
                customer_order=random.choice(clients),
                date_of_the_order=f'{years}-{months}-{days}'
            )
            number_type_products = 0
            if not order.product_order.count():  # проверка заказа на наличие ключа многие ко многим
                num = random.randint(2, len(products))  # создаем количество некоторых видов продуктов
                number_type_products = random.choices(products, k=num)  # создаем партию из этого количества
                order.product_order.set(number_type_products)

            # Выполняем доп. опции с заказом и продуктом
            fill_orders(order, number_type_products)
        self.stdout.write(msg="создание заказов прошло успешно")
