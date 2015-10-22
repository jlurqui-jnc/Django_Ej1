# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('djEj1', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='fecha',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='nombre',
        ),
        migrations.AddField(
            model_name='usuario',
            name='observaciones',
            field=models.TextField(default='', max_length=1024),
        ),
        migrations.AddField(
            model_name='usuario',
            name='user',
            field=models.OneToOneField(default=None, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comentario',
            name='noticia',
            field=models.ForeignKey(default=None, related_name='comentarios', to='djEj1.Noticia'),
        ),
        migrations.AlterField(
            model_name='comentario',
            name='usuario',
            field=models.ForeignKey(default=None, related_name='comentarios', to='djEj1.Usuario'),
        ),
        migrations.AlterField(
            model_name='noticia',
            name='categoria',
            field=models.ForeignKey(default=None, related_name='noticias', to='djEj1.Categoria'),
        ),
    ]
