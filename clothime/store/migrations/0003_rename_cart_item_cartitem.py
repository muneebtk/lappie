# Generated by Django 4.0.4 on 2022-06-04 12:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_cart_cart_item'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cart_item',
            new_name='CartItem',
        ),
    ]
