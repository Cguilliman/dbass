# Generated by Django 4.2.6 on 2023-11-14 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0004_customer_customers_c_birthda_eaf0c8_hash'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='customer',
            name='customers_c_birthda_eaf0c8_hash',
        ),
        migrations.AlterField(
            model_name='customer',
            name='birthday',
            field=models.DateField(db_index=True),
        ),
    ]