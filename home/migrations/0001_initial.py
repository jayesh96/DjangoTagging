# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-15 20:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Annotations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('src', models.CharField(blank=True, max_length=300, null=True)),
                ('text', models.CharField(blank=True, max_length=300, null=True)),
                ('shape_type', models.CharField(blank=True, max_length=300, null=True)),
                ('x', models.DecimalField(blank=True, decimal_places=5, max_digits=20, null=True)),
                ('y', models.DecimalField(blank=True, decimal_places=5, max_digits=20, null=True)),
                ('width', models.DecimalField(blank=True, decimal_places=5, max_digits=20, null=True)),
                ('height', models.DecimalField(blank=True, decimal_places=5, max_digits=20, null=True)),
            ],
        ),
    ]
