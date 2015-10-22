# -*- coding: utf-8 -*-

'''
Created on 8 de oct. de 2015

@author: jlurqui
'''

from django import forms
from djEj1.models.comentario import Comentario
from django.forms.widgets import HiddenInput

class ComentarioForm(forms.ModelForm):
     
    class Meta:
        model = Comentario
        fields = ('texto', 'usuario', 'noticia', 'fecha')
        
        widgets = {
            'noticia': HiddenInput(),
            'fecha': HiddenInput(),            
            'usuario': HiddenInput(),            
        }