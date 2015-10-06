# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djEj1', '0001_squashed_0006_auto_20151005_1014'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticia',
            name='categoria',
            field=models.ForeignKey(default=None, to='djEj1.Categoria'),
        ),
    ]
