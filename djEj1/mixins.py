# -*- coding: utf-8 -*-

'''
Created on 13 de oct. de 2015

@author: jlurqui
'''

from django.forms.models import modelform_factory

class ModelFormWidgetMixin(object):
    def get_form_class(self):
        return modelform_factory(self.model, fields=self.fields, widgets=self.widgets)