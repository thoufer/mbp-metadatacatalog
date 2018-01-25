# Generated by Django 2.0 on 2018-01-12 16:04

from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0003_auto_20180112_0947'),
    ]

    operations = [
        migrations.CreateModel(
            name='TypedTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Name')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='Slug')),
                ('isSubject', models.BooleanField(help_text='Check if the tag is a subject tag.', verbose_name='is Subject tag')),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
            },
        ),
        migrations.AlterField(
            model_name='asset',
            name='place_tags',
            field=taggit.managers.TaggableManager(help_text='??. Select all that apply or create additional ones.', related_name='place_tags', through='asset.TaggedPlace', to='asset.TypedTag', verbose_name='Location keywords'),
        ),
        migrations.AlterField(
            model_name='asset',
            name='subject_tags',
            field=taggit.managers.TaggableManager(help_text='??. Select all that apply or create additional ones.', related_name='subject_tags', through='asset.TaggedSubject', to='asset.TypedTag', verbose_name='Description keywords'),
        ),
        migrations.AlterField(
            model_name='taggedplace',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='asset_taggedplace_items', to='asset.TypedTag'),
        ),
        migrations.AlterField(
            model_name='taggedsubject',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='asset_taggedsubject_items', to='asset.TypedTag'),
        ),
    ]
