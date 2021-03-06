# -*- coding: utf-8 -*-

'''
Created on 15 de sept. de 2015

@author: jlurqui
'''

#from django.shortcuts import render
#from django.shortcuts import render_to_response

from datetime import date

from django.core.urlresolvers import reverse
from django.db.models import Q
from django.forms.widgets import HiddenInput
from django.http.response import HttpResponseRedirect
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView

from djEj1.forms.comentarioForm import ComentarioForm
from djEj1.mixins import CategoriasMixin
from djEj1.mixins import ModelFormWidgetMixin
from djEj1.models.comentario import Comentario
from djEj1.models.noticia import Noticia

from django.contrib import messages

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


class NoticiaView(CategoriasMixin, DetailView):
    model = Noticia
    template_name = 'djEj1/noticia.html'
    titulo = 'Noticia'    
 
    def get_context_data(self, **kwargs):
        # Conseguimos el contexto desde la implementación de la clase base
        context = super(NoticiaView, self).get_context_data(**kwargs)

        # Añadimos al contexto los elementos necesarios
        context['categorias'] = self.categorias()
        #context['form'] = ComentarioForm(initial={'fecha': date.today(), 'noticia': self.object.pk, 'usuario': Usuario.objects.get(pk=1)})
        context['titulo'] = self.titulo
        
        return context
    
    def post(self, *args, **kwargs):
        return self.get(*args, **kwargs)
     

class NoticiasView(CategoriasMixin, ListView):
    #context_object_name = "noticias_list"
    model = Noticia
    ordering  = 'titulo' 
    paginate_by = 2
    template_name = 'djEj1/noticias.html'
    titulo = 'Noticias'
            
    def get_context_data(self, **kwargs):
        # Conseguimos el contexto desde la implementación de la clase base
        context = super(NoticiasView, self).get_context_data(**kwargs)

        # Añadimos al contexto los elementos necesarios
        context['categorias'] = self.categorias()
        context['titulo'] = self.titulo
        
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
        

class CreaNoticiaView(CategoriasMixin, CreateView):
    model = Noticia
    fields = ['fecha', 'categoria', 'titulo', 'texto']
    success_url = 'noticias'
    template_name = 'djEj1/creanoticia.html'
    
            
    def get_context_data(self, **kwargs):
        # Conseguimos el contexto desde la implementación de la clase base
        context = super(CreaNoticiaView, self).get_context_data(**kwargs)

        # Añadimos al contexto los elementos necesarios
        context['categorias'] = self.categorias()
        
        return context

    
class CreaComentarioView(CategoriasMixin, View):
    
    def post(self, request, *args, **kwargs):

        idnoticia = self.kwargs.get('idnoticia', None)
        
        if not idnoticia is None:
                    
            form = ComentarioForm(request.POST)
            
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('noticia', args={idnoticia}))
            else:
                return HttpResponseRedirect(reverse('noticia', {'noticia': Noticia.objects.get(pk=idnoticia), 
                                                                'comentarioForm': form, 'categorias': CategoriasMixin.categorias()}))
                #return render(request, 'djEj1/noticia.html', {'noticia': Noticia.objects.get(pk=idnoticia), 'comentarioForm': form, 'categorias': CategoriasMixin.categorias()})

        return HttpResponseRedirect(reverse('noticias'))
    

class CreaComentarioCreateView(ModelFormWidgetMixin, CategoriasMixin, CreateView):
    
    model = Comentario
    fields = ['fecha', 'texto', 'noticia', 'usuario']
    template_name = 'djEj1/noticia.html'
    titulo = 'Noticia'
    widgets = {
        'noticia': HiddenInput(),
        'fecha': HiddenInput(),  
    }
    
    def get_context_data(self, **kwargs):
        
        idnoticia = self.kwargs.get('pk', None)
        
        # Conseguimos el contexto desde la implementación de la clase base
        context = super(CreaComentarioCreateView, self).get_context_data(**kwargs)

        # Añadimos al contexto los elementos necesarios
        context['categorias'] = self.categorias()
        context['noticia'] = Noticia.objects.get(pk=idnoticia)
        context['titulo'] = self.titulo        
        
        return context

    def get_initial(self):

        super(CreaComentarioCreateView, self).get_initial()

        #self.initial = {'fecha' : date.today(), 'noticia' : Noticia.objects.get(pk=self.kwargs.get('pk', None))}
        self.initial = {'fecha' : date.today(), 'noticia' : self.kwargs.get('pk', None)}

        return self.initial

    def form_valid(self, form):
        
        form.save()

        messages.add_message(self.request, messages.INFO, 'Comentario guardado')
        
        return HttpResponseRedirect(reverse('noticia', args={form.cleaned_data['noticia'].id}))
    

class CreaComentarioViewAjax(ModelFormWidgetMixin, CategoriasMixin, CreateView):
    
    model = Comentario
    fields = ['fecha', 'texto', 'noticia', 'usuario']
    template_name = 'djEj1/noticia_ajax.html'
    titulo = 'Noticia'
    widgets = {
        'noticia': HiddenInput(),
        'fecha': HiddenInput(),  
    }

    def post(self, request, *args, **kwargs):

        idnoticia = self.kwargs.get('idnoticia', None)
        
        if not idnoticia is None:
                    
            form = ComentarioForm(request.POST)
            
            if form.is_valid():
                form.save()
            else:
                messages.add_message(self.request, messages.INFO, 'Comentario erróneo, no fue guardado')
        
        return HttpResponseRedirect(reverse('noticia', args={idnoticia}))
                
    def get_context_data(self, **kwargs):
        
        idnoticia = self.kwargs.get('pk', None)
        
        # Conseguimos el contexto desde la implementación de la clase base
        context = super(CreaComentarioViewAjax, self).get_context_data(**kwargs)

        # Añadimos al contexto los elementos necesarios
        context['categorias'] = self.categorias()
        context['noticia'] = Noticia.objects.get(pk=idnoticia)
        context['titulo'] = self.titulo        
        
        return context

    def get_initial(self):

        super(CreaComentarioViewAjax, self).get_initial()

        self.initial = {'fecha' : date.today(), 'noticia' : self.kwargs.get('pk', None)}

        return self.initial

    def form_valid(self, form):
        
        form.save()

        messages.add_message(self.request, messages.INFO, 'Comentario guardado')
        
        return HttpResponseRedirect(reverse('noticia', args={form.cleaned_data['noticia'].id}))