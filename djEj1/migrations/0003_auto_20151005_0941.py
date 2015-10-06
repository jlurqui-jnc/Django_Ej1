# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('djEj1', '0002_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='nombre',
            field=models.TextField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='noticia',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2015, 10, 5, 9, 41, 29, 367354)),
        ),
        migrations.AddField(
            model_name='noticia',
            name='texto',
            field=models.TextField(null=True, max_length=2048),
        ),
        migrations.AddField(
            model_name='noticia',
            name='titulo',
            field=models.TextField(default='', max_length=30),
        ),
    ]
