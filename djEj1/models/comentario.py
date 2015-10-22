# -*- coding: utf-8 -*-

'''
Created on 7 de oct. de 2015

@author: jlurqui
'''

from django.contrib.auth.models import User  
from django.db import models
from django.utils import timezone

from .noticia import Noticia
#from .usuario import Usuario

class Comentario(models.Model):
    '''
    classdocs
    '''
    fecha = models.DateField(default=timezone.now)
    texto = models.TextField(max_length=2048, null=True)
    noticia = models.ForeignKey(Noticia, default=None, related_name='comentarios')
    usuario = models.ForeignKey(User, default=None, related_name='comentarios')
    
    @classmethod
    def create(cls, fecha, texto, noticia, usuario):
        return Comentario(fecha=fecha, texto=texto, noticia=noticia, usuario=usuario)
    
    def __str__(self):
        return self.usuario.nombre + ': ' + self.texto[0:31]   