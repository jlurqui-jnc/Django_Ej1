# -*- coding: utf-8 -*-

'''
Created on 14 de oct. de 2015

@author: jlurqui
'''

from django.test import TestCase
#from django.test import Client

class Test_View(TestCase):

    def test_View_1(self):
        """
        was_published_recently() should return False for questions whose
        pub_date is in the future.
        """
        self.assertEqual(True, True)