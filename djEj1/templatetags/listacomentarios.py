# -*- coding: utf-8 -*-

'''
Created on 16 de oct. de 2015

@author: jlurqui
'''

from django import template

register = template.Library()

@register.inclusion_tag('djEj1/listacomentarios.html')
def ctt_listacomentarios(noticia):
    return { 'comentarios' : noticia.comentarios.all() }