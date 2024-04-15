from django.core.management import BaseCommand
from ...models import Client
import random_address, names, random


class Command(BaseCommand):
	help = "Создаем базу наших клиентов"

	def handle(self, *args, **options):

		for num in range(10):
			years = random.randint(2020, 2022)
			months = random.randint(1, 12)
			days = random.randint(1, 28) if months == 2 else random.randint(1, 30)

			random_name = names.get_full_name()  # случайное имя
			random_number = random.randint(1000, 100000)
			random_phone_number = random.randint(1000000000, 9999999999)  # случайный номер телефона
			random_address_ = random_address.real_random_address()['address1']  # случайный адрес

			client = Client(
				name_client=random_name,
				email=f'{random_name[:3]}{random_number}@gmail.com',
				phone_number=random_phone_number,
				address=random_address_,
				registration_date_client=f'{years}-{months}-{days}'
			)

			client.save()
		self.stdout.write(msg="создание клиентов прошло успешно")
