from django.core.management import BaseCommand
from django.utils import lorem_ipsum
from ...models import Product
import random


class Command(BaseCommand):
    help = "Создаем продукты в нашем магазине"

    def handle(self, *args, **options):
        # for num in range(1, 16):
        #     years = random.randint(2023, 2024)
        #     months = random.randint(1, 12) if years == 2023 else random.randint(1, 3)
        #     days = random.randint(1, 28) if months == 2 else random.randint(1, 30)
        #
        #     random_price = random.randint(10, 101)  # случайная цена продукта
        #     random_quantity = random.randint(30, 1001)  # случайное количество товара
        # #
        #     product = Product(
        #         pk=17,
        #         name_of_item=f'product № {17}',
        #         description=lorem_ipsum.words(10),
        #         price=58,
        #         quantity=400,
        #         date_of_manufacture_product=f'{2023}-{2}-{5}'
        #     )
        #     product.save()
        #     self.stdout.write(msg="создание продуктов прошло успешно")
            products = Product.objects.all()
            for product in products:

                if product.picture:
                    product.picture.delete()

