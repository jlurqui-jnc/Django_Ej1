# -*- coding: utf-8 -*-

'''
Created on 2 de oct. de 2015

@author: jlurqui
'''

from django.db import models

class Categoria(models.Model):
    '''
    classdocs
    '''
    nombre = models.TextField(max_length=50, default='')
    
    @classmethod
    def create(cls, nombre):
        return Categoria(nombre=nombre)