from django.db import models


class Client(models.Model):
    name_client = models.CharField(max_length=20)
    email = models.EmailField()
    phone_number = models.DecimalField(max_digits=15, decimal_places=0)
    address = models.CharField(max_length=20)
    registration_date_client = models.DateField()

    def __str__(self):
        return f' {self.name_client}'


class Product(models.Model):
    name_of_item = models.CharField(max_length=20)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=0)
    date_of_manufacture_product = models.DateField()

    def __str__(self):
        return f'Продукт {self.name_of_item, self.quantity, self.date_of_manufacture_product}'

    def quantity_of_product_sold(self, num):
        """Количество оставшегося товара"""
        self.quantity -= num
        self.save()


class Order(models.Model):
    date_of_the_order = models.DateField()
    total_amount_of_the_order = models.IntegerField(default=0)
    customer_order = models.ForeignKey(Client, related_name='product_id', on_delete=models.CASCADE)
    product_order = models.ManyToManyField(Product, db_table="goods_orders")

    def __str__(self):
        return f'Заказ номер {self.id}, {self.date_of_the_order}'

    def sum_order(self, price):
        """Общая сумма заказа"""
        self.total_amount_of_the_order += price
        self.save()
