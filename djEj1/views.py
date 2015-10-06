# -*- coding: utf-8 -*-

'''
Created on 15 de sept. de 2015

@author: jlurqui
'''

# import csv
# import os

from django.shortcuts import render_to_response
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import TemplateView, ListView

from djEj1.models.categoria import Categoria
from djEj1.models.noticia import Noticia

# from djEj1.settings import BASE_DIR

def contacto(request):
    return render_to_response('djEj1/sidebar.html',
                              {'titulo': 'Contacto'})  
def home(request):
    return render_to_response('djEj1/base.html',
                              {'titulo': 'Inicio'})  

def inmuebles(request):
    return render_to_response('djEj1/base.html',
                              {'titulo': 'Inmuebles'})  


def buscanoticias(request):
    busqueda = request.GET['busqueda']
    return pintaNoticias(request, Noticia.objects.filter(Q(titulo__icontains=busqueda) | Q(texto__icontains=busqueda) | Q(categoria__nombre__icontains=busqueda)))
    
def filtraCategorias():
    return (categoria for categoria in Categoria.objects.all() if Noticia.objects.filter(categoria=categoria.id).exists())
    
def noticia(request, idnoticia, nota=None):
    return render_to_response('djEj1/noticia.html', 
                              {'noticia': Noticia.objects.get(id=idnoticia),
                               'nota': nota,
                               'categorias' : filtraCategorias()})

def noticias(request, idcategoria=None):
    if (idcategoria != None):
        return pintaNoticias(request, Noticia.objects.filter(categoria=idcategoria))
    else:
        return pintaNoticias(request, Noticia.objects.all())        

def pintaNoticias(request, lista_noticias):
    paginador = Paginator(lista_noticias, 2)
    pagina = request.GET.get('pagina')
    
    try:
        noticias = paginador.page(pagina)
    except PageNotAnInteger:
        # Si no hay página o no es entero devolvemos la primera
        noticias = paginador.page(1)
    except EmptyPage:
        # Si la página está fuera de las existentes devolvemos la última página existente
        noticias = paginador.page(paginador.num_pages)
   
    return render_to_response('djEj1/noticias.html', 
                        {'noticias': noticias,
                         'categorias' : filtraCategorias()})



#####################
# Class-Based Views #
#####################

class TemplateViewBasico(TemplateView):
    template_name = 'djEj1/base.html'
    titulo = ''
        
    def get_context_data(self, **kwargs):
        # Conseguimos el contexto desde la implementación de la clase base
        context = super(TemplateViewBasico, self).get_context_data(**kwargs)
        # Añadimos al contexto los elementos necesarios
        context['titulo'] = self.titulo
        return context

class ContactoView(TemplateViewBasico):
    template_name = 'djEj1/sidebar.html'
    titulo = 'Contacto'
    
class HomeView(TemplateViewBasico):
    titulo = 'Inicio'
        
class InmueblesView(TemplateViewBasico):
    titulo = 'Inmuebles'
    

##############################################
#EL CODIGO AQUÍ DEBAJO NO SE USA: ES ANTIGUO #
##############################################

# def lector_noticias():
#     with open(os.path.join(BASE_DIR, 'djEj1', 'noticias.csv'), newline='') as csvfile:
#         return csv.DictReader(csvfile, delimiter=',', quotechar='|')

#Este son los métodos originales
# def noticia1(request, idnoticia, nota=None):
#     with open(os.path.join(BASE_DIR, 'djEj1', 'noticias.csv'), newline='') as csvfile:
#         lector = csv.DictReader(csvfile, delimiter=',', quotechar='|')
#         return render_to_response('djEj1/noticia.html', 
#                                   {'titulo': 'Noticia', 
#                                    'noticia': [noticia for noticia in lector if noticia['Id'] == idnoticia][0],
#                                    'nota': nota})

# def noticias1(request):
#     with open(os.path.join(BASE_DIR, 'djEj1', 'noticias.csv'), newline='') as csvfile:
#         lector = csv.DictReader(csvfile, delimiter=',', quotechar='|')
#         return render_to_response('djEj1/noticias.html', 
#                               {'titulo': 'Noticias', 'noticias': lector})

#Este es el método alternativo para el ejercicio cuando leía del CSV
# def noticias2(request):
#     noticias = []
#     with open(os.path.join(BASE_DIR, 'djEj1', 'noticias.csv'), newline='') as csvfile:
#         lector = csv.DictReader(csvfile, delimiter=',', quotechar='|')
#         for fila in lector:
#             noticias.append(fila)
#     return render_to_response('djEj1/noticias.html',
#                               {'titulo': 'Noticias', 'noticias': noticias})

#Este es el método alternativo para el ejercicio pero no funciona porque habría que definir ciertos métodos en el csv.DictReader
# def noticias3(request):
#     with lector_noticias() as lector:
#         return render_to_response('djEj1/noticias.html', 
#                               {'titulo': 'Noticias', 'noticias': lector})