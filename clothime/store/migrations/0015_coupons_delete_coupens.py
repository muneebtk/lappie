# Generated by Django 4.0.4 on 2022-07-03 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_coupens'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coupon_name', models.CharField(max_length=20)),
                ('discount_amount', models.IntegerField()),
                ('coupon_code', models.CharField(max_length=20)),
                ('limit', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Coupens',
        ),
    ]
