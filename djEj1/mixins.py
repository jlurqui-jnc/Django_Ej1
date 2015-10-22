# -*- coding: utf-8 -*-

'''
Created on 13 de oct. de 2015

@author: jlurqui
'''

from django.forms.models import modelform_factory

from djEj1.models.categoria import Categoria
from djEj1.models.noticia import Noticia

class CategoriasMixin:
    
    @classmethod
    def categorias(cls):
        return (categoria for categoria in Categoria.objects.all() if Noticia.objects.filter(categoria=categoria.id).exists()) 

class ModelFormWidgetMixin(object):
    def get_form_class(self):
        return modelform_factory(self.model, fields=self.fields, widgets=self.widgets)