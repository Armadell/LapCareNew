# Generated by Django 4.1.1 on 2022-10-03 04:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0005_category_is_discount_activate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='is_discount_activate',
            new_name='is_discount_active',
        ),
    ]
