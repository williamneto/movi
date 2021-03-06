# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-06 11:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20170221_1101'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=150)),
                ('texto', models.CharField(max_length=500)),
            ],
        ),
        migrations.AlterField(
            model_name='movi',
            name='bairro',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='movi',
            name='end',
            field=models.CharField(blank=True, default=None, max_length=150),
        ),
        migrations.AddField(
            model_name='notas',
            name='related_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Movi'),
        ),
    ]
