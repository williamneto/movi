# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-06 12:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20170306_1158'),
    ]

    operations = [
        migrations.AddField(
            model_name='notas',
            name='categoria',
            field=models.CharField(choices=[(b'Nota', b'Nota'), (b'Tarefa', b'Tarefa')], default=b'Nota', max_length=150),
        ),
    ]
