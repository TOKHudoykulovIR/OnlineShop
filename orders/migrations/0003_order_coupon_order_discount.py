# Generated by Django 4.2.6 on 2023-10-17 07:56

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("coupons", "0001_initial"),
        ("orders", "0002_alter_order_city_alter_order_email_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="coupon",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="orders",
                to="coupons.coupon",
            ),
        ),
        migrations.AddField(
            model_name="order",
            name="discount",
            field=models.IntegerField(
                default=0,
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(100),
                ],
            ),
        ),
    ]
