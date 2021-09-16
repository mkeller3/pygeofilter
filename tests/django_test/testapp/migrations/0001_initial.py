# flake8: noqa

# Generated by Django 2.2.5 on 2019-09-09 07:18

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.CharField(max_length=256, unique=True)),
                ('geometry', django.contrib.gis.db.models.fields.GeometryField(srid=4326)),
                ('float_attribute', models.FloatField(blank=True, null=True)),
                ('int_attribute', models.IntegerField(blank=True, null=True)),
                ('str_attribute', models.CharField(blank=True, max_length=256, null=True)),
                ('datetime_attribute', models.DateTimeField(blank=True, null=True)),
                ('choice_attribute', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'A'), (2, 'B'), (3, 'C')], null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RecordMeta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('float_meta_attribute', models.FloatField(blank=True, null=True)),
                ('int_meta_attribute', models.IntegerField(blank=True, null=True)),
                ('str_meta_attribute', models.CharField(blank=True, max_length=256, null=True)),
                ('datetime_meta_attribute', models.DateTimeField(blank=True, null=True)),
                ('choice_meta_attribute', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'X'), (2, 'Y'), (3, 'Z')], null=True)),
                ('record', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='record_metas', to='testapp.Record')),
            ],
        ),
    ]
