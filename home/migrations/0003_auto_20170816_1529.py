# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-16 09:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20170816_0231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annotations',
            name='height',
            field=models.DecimalField(decimal_places=10, max_digits=20),
        ),
        migrations.AlterField(
            model_name='annotations',
            name='width',
            field=models.DecimalField(decimal_places=10, max_digits=20),
        ),
        migrations.AlterField(
            model_name='annotations',
            name='x',
            field=models.DecimalField(decimal_places=10, max_digits=20),
        ),
        migrations.AlterField(
            model_name='annotations',
            name='y',
            field=models.DecimalField(decimal_places=10, max_digits=20),
        ),
    ]
