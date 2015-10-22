# -*- coding: utf-8 -*-
'''
Created on 16 de oct. de 2015

@author: jlurqui
'''

from datetime import date

from django import template
from django.http.response import HttpResponseRedirect
from django.contrib.auth.models import User

from djEj1.forms.comentarioForm import ComentarioForm
from djEj1.mixins import CategoriasMixin
from djEj1.models import Noticia

register = template.Library()

@register.inclusion_tag('djEj1/altacomentario.html', takes_context=True)
def ctt_altacomentario(context, noticia):
    
    request = context.get('request')
    
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        
        if form.is_valid():
            form.save()
            noticia = Noticia.objects.get(pk=noticia.pk)
        form = ComentarioForm()
    else:
        form = ComentarioForm(initial={'fecha': date.today(), 'noticia': context['noticia'], 'usuario': User.objects.get(pk=1)})
        
    return { 'form' : form, 'noticia' : noticia, 'categorias' : CategoriasMixin.categorias()}