# -*- coding: utf-8 -*-

'''
Created on 17 de sept. de 2015

@author: jlurqui
'''

from django.db import models
from django.utils import timezone
from djEj1.models.categoria import Categoria

class Noticia(models.Model):
    '''
    classdocs
    '''
    fecha = models.DateField(default=timezone.now)
    titulo = models.TextField(max_length=30, default='')
    texto = models.TextField(max_length=2048, null=True)
    categoria = models.ForeignKey(Categoria, default=None)
    
    @classmethod
    def create(cls, titulo, texto, fecha, categoria):
        return Noticia(titulo=titulo, texto=texto, fecha=fecha, categoria=categoria)    