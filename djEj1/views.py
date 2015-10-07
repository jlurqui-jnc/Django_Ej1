# -*- coding: utf-8 -*-

'''
Created on 15 de sept. de 2015

@author: jlurqui
'''

from django.shortcuts import render_to_response
from django.db.models import Q
from django.views.generic import TemplateView, ListView, DetailView, CreateView

from djEj1.models.categoria import Categoria
from djEj1.models.noticia import Noticia

def categorias():
    return (categoria for categoria in Categoria.objects.all() if Noticia.objects.filter(categoria=categoria.id).exists())
     
def noticia(request, idnoticia, nota=None):
    return render_to_response('djEj1/noticia.html', 
                               {'noticia': Noticia.objects.get(id=idnoticia),
                                'nota': nota,
                                'categorias' : categorias()})

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

class NoticiaView(DetailView):
    model = Noticia
    template_name = 'djEj1/noticia.html'
 
    def get_context_data(self, **kwargs):
        # Conseguimos el contexto desde la implementación de la clase base
        context = super(NoticiaView, self).get_context_data(**kwargs)

        # Añadimos al contexto los elementos necesarios
        context['categorias'] = categorias()
        context['nota'] = self.kwargs.get('nota', None)
        
        return context
     
class NoticiasView(ListView):
    #context_object_name = "noticias_list"
    model = Noticia
    ordering  = 'titulo' 
    paginate_by = 2
    template_name = 'djEj1/noticias.html'
        
    def get_context_data(self, **kwargs):
        # Conseguimos el contexto desde la implementación de la clase base
        context = super(NoticiasView, self).get_context_data(**kwargs)

        # Añadimos al contexto los elementos necesarios
        context['categorias'] = categorias()
        
        return context

    def get_queryset(self):
        busqueda = self.request.GET.get('busqueda')
        idcategoria = self.kwargs.get('idcategoria', None)

        if (idcategoria != None):
            lista_noticias = Noticia.objects.filter(categoria=idcategoria)
        else:
            lista_noticias = Noticia.objects.all()        
         
        if (busqueda != None):
            return lista_noticias.filter(Q(titulo__icontains=busqueda) | Q(texto__icontains=busqueda) | Q(categoria__nombre__icontains=busqueda))
        else:    
            return lista_noticias
        
class CreaNoticiasView(CreateView):
    model = Noticia
    fields = ['fecha', 'categoria', 'titulo', 'texto']
    success_url = 'noticias'
    template_name = 'djEj1/creanoticia.html'
    
#     def get_context_data(self, **kwargs):
#         # Conseguimos el contexto desde la implementación de la clase base
#         context = super(CreaNoticiasView, self).get_context_data(**kwargs)
# 
#         # Añadimos al contexto los elementos necesarios
#         context['categorias'] = categorias()    