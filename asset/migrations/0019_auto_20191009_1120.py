# Generated by Django 2.0.4 on 2019-10-09 15:20

from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0018_merge_20180316_1239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='parent',
            field=models.ForeignKey(blank=True, help_text='If this data asset shares a common history, administration, decision context, and/or species + location + platform that requires coordinated planning and management, select the assest that is its parent.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='child_asset', to='asset.Asset', verbose_name='Parent Asset'),
        ),
        migrations.AlterField(
            model_name='asset',
            name='subject_tags',
            field=taggit.managers.TaggableManager(help_text='Select all that apply. Additional keywords can be created by typing the desired keyword, followed by selecting it from the menu or &lt;Enter&gt;.', related_name='subject_tags', through='asset.TaggedSubject', to='asset.SubjectTag', verbose_name='Keywords'),
        ),
    ]
