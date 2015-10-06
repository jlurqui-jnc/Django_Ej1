# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    replaces = [('djEj1', '0001_initial'), ('djEj1', '0002_categoria'), ('djEj1', '0003_auto_20151005_0941'), ('djEj1', '0004_auto_20151005_0942'), ('djEj1', '0005_auto_20151005_0943'), ('djEj1', '0006_auto_20151005_1014')]

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('fecha', models.DateField(default=django.utils.timezone.now)),
                ('texto', models.TextField(max_length=2048, null=True)),
                ('titulo', models.TextField(max_length=30, default='')),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('nombre', models.TextField(max_length=50, default='')),
            ],
        ),
    ]
