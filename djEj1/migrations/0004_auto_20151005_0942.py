# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('djEj1', '0003_auto_20151005_0941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2015, 10, 5, 7, 42, 40, 110401, tzinfo=utc)),
        ),
    ]
