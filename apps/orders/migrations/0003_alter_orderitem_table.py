# Generated by Django 3.2.16 on 2023-01-28 10:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20230128_0634'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='orderitem',
            table='order_item',
        ),
    ]
