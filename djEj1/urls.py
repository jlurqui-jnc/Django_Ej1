"""djEj1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

from .views import ContactoView, HomeView, InmueblesView, NoticiaView, NoticiasView, CreaNoticiaView, CreaComentarioView, CreaComentarioCreateView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url('^$', HomeView.as_view(), name='home'),
    url('^home$', HomeView.as_view(), name='homehome'),
    url('^contacto$', ContactoView.as_view(), name='contacto'),
    url('^inmuebles$', InmueblesView.as_view(), name='inmuebles'),
    
    #Noticias
    url('^buscanoticias$', NoticiasView.as_view(), name='buscanoticias'),
    url('^creacomentario/(?P<idnoticia>\d+)$$', CreaComentarioView.as_view(), name='creacomentario'),
    url('^creanoticia$', CreaNoticiaView.as_view(), name='creanoticia'),
    url('^noticias$', NoticiasView.as_view(), name='noticias'),
    url('^noticias/c(?P<idcategoria>\d+)$', NoticiasView.as_view(), name='noticiascat'),
    #url('^noticia/(?P<pk>\d+)$', NoticiaView.as_view(), name='noticia'),
    url('^noticia/(?P<pk>\d+)$', CreaComentarioCreateView.as_view(), name='noticia'),    
]

#The () view is overridden by handler400:
handler404 = 'mysite.views.my_custom_page_not_found_view'

#The server_error() view is overridden by handler500:
handler500 = 'mysite.views.my_custom_error_view'

#The permission_denied() view is overridden by handler403:
handler403 = 'mysite.views.my_custom_permission_denied_view'

# The bad_request() view is overridden by handler400:
handler400 = 'mysite.views.my_custom_bad_request_view'