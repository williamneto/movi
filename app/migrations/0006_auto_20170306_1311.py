# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-06 13:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20170306_1254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nota',
            name='related_to',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='app.Movi'),
        ),
    ]
