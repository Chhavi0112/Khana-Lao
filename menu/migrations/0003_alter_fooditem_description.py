# Generated by Django 5.0.6 on 2024-07-03 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_alter_category_options_alter_fooditem_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fooditem',
            name='description',
            field=models.TextField(blank=True, max_length=250),
        ),
    ]
