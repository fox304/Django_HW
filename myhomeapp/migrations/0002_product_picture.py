# Generated by Django 5.0.3 on 2024-04-08 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myhomeapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='picture',
            field=models.ImageField(blank=True, upload_to='.media/'),
        ),
    ]