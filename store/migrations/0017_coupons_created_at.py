# Generated by Django 4.0.4 on 2022-07-04 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0016_remove_coupons_coupon_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupons',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
