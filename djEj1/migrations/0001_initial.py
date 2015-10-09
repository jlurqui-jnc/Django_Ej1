# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('nombre', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('fecha', models.DateField(default=django.utils.timezone.now)),
                ('texto', models.TextField(null=True, max_length=2048)),
            ],
        ),
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('fecha', models.DateField(default=django.utils.timezone.now)),
                ('titulo', models.CharField(default='', max_length=128)),
                ('texto', models.TextField(null=True, max_length=2048)),
                ('categoria', models.ForeignKey(default=None, to='djEj1.Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('fecha', models.DateField(default=django.utils.timezone.now)),
                ('nombre', models.CharField(default='', max_length=32)),
            ],
        ),
        migrations.AddField(
            model_name='comentario',
            name='noticia',
            field=models.ForeignKey(default=None, to='djEj1.Noticia'),
        ),
        migrations.AddField(
            model_name='comentario',
            name='usuario',
            field=models.ForeignKey(default=None, to='djEj1.Usuario'),
        ),
    ]
