# Generated by Django 3.2.7 on 2021-09-30 13:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20210930_1628'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customeraddress',
            options={'verbose_name_plural': 'Customer Address'},
        ),
        migrations.AlterModelOptions(
            name='orderproducts',
            options={'verbose_name_plural': 'Order Products'},
        ),
    ]