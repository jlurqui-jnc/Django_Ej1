# -*- coding: utf-8 -*-

'''
Created on 7 de oct. de 2015

@author: jlurqui
'''

from django.db import models
from django.utils import timezone

class Usuario(models.Model):
    '''
    classdocs
    '''
    fecha = models.DateField(default=timezone.now)
    nombre = models.CharField(max_length=32, default='')
    
    @classmethod
    def create(cls, usuario, fecha):
        return Usuario(usuario=usuario, fecha=fecha)
    
    def __str__(self):
        return self.nombre