# -*- coding: utf-8 -*-
'''
Created on 7 de oct. de 2015

@author: jlurqui
'''

from django.contrib import admin

from .models.categoria import Categoria
from .models.comentario import Comentario
from .models.noticia import Noticia
from .models.usuario import Usuario

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    pass

class ComentarioInLine(admin.StackedInline):
    model = Comentario
    extra = 0

@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    inlines = [ComentarioInLine]
    list_display = ['fecha', 'titulo', 'texto', 'categoria']
    ordering = ['fecha']
    
@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    pass