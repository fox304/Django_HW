# Generated by Django 5.0.3 on 2024-04-09 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myhomeapp', '0002_product_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='picture',
            field=models.ImageField(upload_to='med'),
        ),
    ]
