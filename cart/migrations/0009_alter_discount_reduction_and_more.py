# Generated by Django 4.1.1 on 2022-10-08 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cart", "0008_alter_discount_reduction_alter_discount_total"),
    ]

    operations = [
        migrations.AlterField(
            model_name="discount",
            name="reduction",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="discount",
            name="total_discount",
            field=models.FloatField(blank=True, null=True),
        ),
    ]