# Generated by Django 3.2.16 on 2023-02-06 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0013_alter_order_total_amount'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='orderitem',
            index=models.Index(fields=['order', 'product'], name='orders_item_order_i_f64f26_idx'),
        ),
    ]
