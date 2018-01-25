# Generated by Django 2.0 on 2018-01-19 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0006_auto_20180117_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='partners',
            field=models.CharField(blank=True, help_text='Include all partners as a comma separate list, that have direct involvement in the collection, storage, or maintenance of the asset.', max_length=100, null=True, verbose_name='Partners'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='region',
            field=models.CharField(max_length=2),
        ),
    ]
