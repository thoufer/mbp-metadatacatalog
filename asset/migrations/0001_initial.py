# Generated by Django 2.0 on 2018-01-12 14:08

import asset.validators
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='A descriptive name of the asset.', max_length=200, verbose_name='Asset Name')),
                ('status', models.CharField(choices=[('operational', 'Operational'), ('inactive', 'Inactive'), ('experimental', 'Experimental')], help_text='Selection the value that best represents the current stateof the asset. Inactive should be used for assets that have ceasedoperations or have been discontinued.', max_length=15, verbose_name='Asset Status')),
                ('isContracted', models.BooleanField(default=False, help_text='This should be checked for assets in which the storage ormaintenance of the asset are performed through a contractualaggreeement with a non-fws entity.', verbose_name='Contracted')),
                ('spatial_scale', models.CharField(choices=[('BCR', 'BCR'), ('multi-state', 'multi-State/Province'), ('single state', 'Single State/Province'), ('local', 'local')], help_text='Choose the spatial scale that best represents the largestscale that the data are collected.', max_length=15)),
                ('start_month', models.CharField(choices=[('JAN', 'January'), ('FEB', 'February'), ('MAR', 'March'), ('APR', 'April'), ('MAY', 'May'), ('JUN', 'June'), ('JUL', 'July'), ('AUG', 'August'), ('SEP', 'September'), ('OCT', 'October'), ('NOV', 'November'), ('DEC', 'December')], max_length=3)),
                ('end_month', models.CharField(choices=[('JAN', 'January'), ('FEB', 'February'), ('MAR', 'March'), ('APR', 'April'), ('MAY', 'May'), ('JUN', 'June'), ('JUL', 'July'), ('AUG', 'August'), ('SEP', 'September'), ('OCT', 'October'), ('NOV', 'November'), ('DEC', 'December')], max_length=3)),
                ('description', models.TextField(help_text='Provide an extentive description which provides detailedinformation about the use, timing, location, and methodsof collection or analysis. (Max 10,000 characters)', max_length=10000, verbose_name='Abstract')),
                ('partners', models.CharField(blank=True, help_text='Include all partners that have direct involvement in the collection, storage, or maintenance of the asset.', max_length=100, null=True, verbose_name='Partners')),
                ('start_year', models.CharField(help_text='The year in which data were first collected', max_length=4, validators=[asset.validators.validate_start_year], verbose_name='Starting Year')),
                ('end_year', models.CharField(default='Present', help_text='The last year data were collected, or `Present` if thedata are still being collected.', max_length=7, validators=[asset.validators.validate_end_year], verbose_name='Ending Year')),
                ('primary_contact_name', models.CharField(max_length=50, verbose_name='Primary Contact')),
                ('primary_contact_address', models.CharField(max_length=150, verbose_name='Address')),
                ('primary_contact_city', models.CharField(max_length=50, verbose_name='City')),
                ('primary_contact_state', models.CharField(max_length=2, verbose_name='State')),
                ('primary_contact_zip', models.CharField(max_length=5, verbose_name='Zip')),
                ('primary_contact_email', models.EmailField(max_length=254, validators=[asset.validators.validate_primary_email], verbose_name='Email')),
                ('primary_contact_phone', models.CharField(max_length=13, verbose_name='Phone')),
                ('data_contact_name', models.CharField(max_length=50, verbose_name='Data Contact')),
                ('data_contact_address', models.CharField(max_length=150, verbose_name='Address')),
                ('data_contact_city', models.CharField(max_length=50, verbose_name='City')),
                ('data_contact_state', models.CharField(max_length=2, verbose_name='State')),
                ('data_contact_zip', models.CharField(max_length=5, verbose_name='Zip')),
                ('data_contact_email', models.EmailField(max_length=254, verbose_name='Email')),
                ('data_contact_phone', models.CharField(max_length=13, verbose_name='Phone')),
            ],
            options={
                'db_table': 'Asset',
            },
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('code', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name': 'Organization',
                'db_table': 'organization',
                'ordering': ['code'],
            },
        ),
        migrations.CreateModel(
            name='TaggedPlace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asset.Asset')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='asset_taggedplace_items', to='taggit.Tag')),
            ],
            options={
                'db_table': 'AssetPlace_Tag',
            },
        ),
        migrations.CreateModel(
            name='TaggedSubject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asset.Asset')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='asset_taggedsubject_items', to='taggit.Tag')),
            ],
            options={
                'db_table': 'AssetSubject_Tag',
            },
        ),
        migrations.AddField(
            model_name='asset',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='assets', to='asset.Organization', verbose_name='Primary Stewardship Organziation'),
        ),
        migrations.AddField(
            model_name='asset',
            name='parent',
            field=models.ForeignKey(blank=True, help_text='If this data asset shares a common history, administration,decision context, and/or species+location+platform thatrequires coordinated planning and management, select theassest that is its parent.', null=True, on_delete=django.db.models.deletion.PROTECT, to='asset.Asset', verbose_name='Parent Asset'),
        ),
        migrations.AddField(
            model_name='asset',
            name='place_tags',
            field=taggit.managers.TaggableManager(help_text='??. Select all that apply or create additional ones.', related_name='place_tags', through='asset.TaggedPlace', to='taggit.Tag', verbose_name='Location keywords'),
        ),
        migrations.AddField(
            model_name='asset',
            name='subject_tags',
            field=taggit.managers.TaggableManager(help_text='??. Select all that apply or create additional ones.', related_name='subject_tags', through='asset.TaggedSubject', to='taggit.Tag', verbose_name='Description keywords'),
        ),
    ]
