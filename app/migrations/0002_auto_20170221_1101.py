# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-21 11:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movi',
            name='end',
            field=models.CharField(default=None, max_length=150),
        ),
        migrations.AlterField(
            model_name='movi',
            name='categoria',
            field=models.CharField(choices=[(b'Contato', b'Contato'), (b'Movimento', b'Movimento'), (b'Pauta', b'Pauta'), (b'Midia', b'Evento')], max_length=150),
        ),
    ]
