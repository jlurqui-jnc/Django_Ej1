# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('djEj1', '0004_auto_20151005_0942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2015, 10, 5, 7, 43, 11, 778212, tzinfo=utc)),
        ),
    ]
