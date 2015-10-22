# -*- coding: utf-8 -*-

'''
Created on 7 de oct. de 2015

@author: jlurqui
'''

from django.contrib.auth.models import User 
from django.db import models

class Usuario(models.Model):
    '''
    classdocs
    '''
    user = models.OneToOneField(User, default=None)
    observaciones = models.TextField(max_length=1024, default='')
    
    @classmethod
    def create(cls, observaciones):
        return Usuario(observaciones=observaciones)
    
    def __str__(self):
        return self.observaciones[0,31]