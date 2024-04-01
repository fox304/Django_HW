from django.core.management import BaseCommand
from django.utils import lorem_ipsum
from ...models import Product
import random


class Command(BaseCommand):
    help = "Создаем продукты в нашем магазине"

    def handle(self, *args, **options):
        for num in range(1, 16):
            years = random.randint(2023, 2024)
            months = random.randint(1, 12) if years == 2023 else random.randint(1, 3)
            days = random.randint(1, 28) if months == 2 else random.randint(1, 30)

            random_price = random.randint(10, 101)  # случайная цена продукта
            random_quantity = random.randint(30, 1001)  # случайное количество товара

            product = Product(
                name_of_item=f'product № {num}',
                description=lorem_ipsum.words(10),
                price=round(random_price, 2),
                quantity=random_quantity,
                date_of_manufacture_product=f'{years}-{months}-{days}'
            )
            product.save()
        self.stdout.write(msg="создание продуктов прошло успешно")
