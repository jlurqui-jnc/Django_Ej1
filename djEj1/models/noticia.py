# -*- coding: utf-8 -*-

'''
Created on 17 de sept. de 2015

@author: jlurqui
'''

from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse

from .categoria import Categoria

class Noticia(models.Model):
    '''
    classdocs
    '''
    fecha = models.DateField(default=timezone.now)
    titulo = models.CharField(max_length=128, default='')
    texto = models.TextField(max_length=2048, null=True)
    categoria = models.ForeignKey(Categoria, default=None, related_name='noticias')
    
    @classmethod
    def create(cls, titulo, texto, fecha, categoria):
        return Noticia(titulo=titulo, texto=texto, fecha=fecha, categoria=categoria)
    
    def __str__(self):
        return self.titulo[0:31]
    
    def get_absolute_url(self):
        return reverse('noticia', args=[str(self.id)])