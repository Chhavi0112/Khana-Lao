# Generated by Django 5.0.6 on 2024-07-18 05:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0002_remove_cart_qyautity_cart_qauntity'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='qauntity',
            new_name='quantity',
        ),
    ]
