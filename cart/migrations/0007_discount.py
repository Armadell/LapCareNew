# Generated by Django 4.1.1 on 2022-10-08 07:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("cart", "0006_coupon_repeated_check"),
    ]

    operations = [
        migrations.CreateModel(
            name="discount",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("total", models.FloatField(blank=True, max_length=80, null=True)),
                (
                    "total_discount",
                    models.FloatField(blank=True, max_length=80, null=True),
                ),
                ("reduction", models.FloatField(blank=True, max_length=80, null=True)),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]