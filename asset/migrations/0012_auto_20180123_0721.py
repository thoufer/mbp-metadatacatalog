# Generated by Django 2.0 on 2018-01-23 12:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0011_auto_20180123_0715'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='historicalasset',
            table='asset_history',
        ),
    ]
