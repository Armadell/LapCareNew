# Generated by Django 4.1.1 on 2022-10-08 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cart", "0007_discount"),
    ]

    operations = [
        migrations.AlterField(
            model_name="discount",
            name="reduction",
            field=models.IntegerField(blank=True, max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name="discount",
            name="total",
            field=models.IntegerField(blank=True, max_length=80, null=True),
        ),
    ]
