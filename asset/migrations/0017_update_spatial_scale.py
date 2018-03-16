# Generated by Django 2.0 on 2018-03-07 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0016_auto_20180301_1417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='spatial_scale',
            field=models.CharField(choices=[('', 'Choose Scale'), ('BCR', 'BCR'), ('Multiple states or provinces', 'Multiple states or provinces'), ('Single state or province', 'Single state or province'), ('Local', 'Local')], help_text='Choose the spatial scale that best represents the largest scale that the data are collected.', max_length=50),
        ),
        migrations.AlterField(
            model_name='historicalasset',
            name='spatial_scale',
            field=models.CharField(choices=[('', 'Choose Scale'), ('BCR', 'BCR'), ('Multiple states or provinces', 'Multiple states or provinces'), ('Single state or province', 'Single state or province'), ('Local', 'Local')], help_text='Choose the spatial scale that best represents the largest scale that the data are collected.', max_length=50),
        ),
    ]