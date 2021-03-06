# Generated by Django 4.0.4 on 2022-06-14 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_payment_order_id_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('New', 'New'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled'), ('Accepted', 'Accepted')], default='New', max_length=10),
        ),
    ]
