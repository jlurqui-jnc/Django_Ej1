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

from .views import home, buscanoticias, contacto, inmuebles, noticia, noticias

from .views import ContactoView, HomeView, InmueblesView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
#    url('^$', home, name='home'),
#    url('^home$', home, name='home'),
    url('^$', HomeView.as_view(), name='home'),
    url('^home$', HomeView.as_view(), name='home'),
    url('^contacto$', ContactoView.as_view(), name='contacto'),
    url('^inmuebles$', InmueblesView.as_view(), name='inmuebles'),
    url('^buscanoticias$', buscanoticias, name='buscanoticias'),
    url('^noticias$', noticias, name='noticias'),
    url('^noticias/c(?P<idcategoria>\d+)$', noticias, name='noticias'),
    url('^noticia/(?P<idnoticia>\d+)$', noticia, name='noticia'),
    url('^noticia/(?P<idnoticia>\d+)/(?P<nota>[0-9A-Za-z])$', noticia, name='noticia'),
]


#The () view is overridden by handler400:
handler404 = 'mysite.views.my_custom_page_not_found_view'

#The server_error() view is overridden by handler500:
handler500 = 'mysite.views.my_custom_error_view'

#The permission_denied() view is overridden by handler403:
handler403 = 'mysite.views.my_custom_permission_denied_view'

# The bad_request() view is overridden by handler400:
handler400 = 'mysite.views.my_custom_bad_request_view'