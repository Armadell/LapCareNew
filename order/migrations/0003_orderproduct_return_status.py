# Generated by Django 4.1.1 on 2022-10-10 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("order", "0002_orderproduct_status_alter_order_status"),
    ]

    operations = [
        migrations.AddField(
            model_name="orderproduct",
            name="return_status",
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
    ]
