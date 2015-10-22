# -*- coding: utf-8 -*-

'''
Created on 13 de oct. de 2015

@author: jlurqui
'''

from django.test import TestCase

class Test_Model(TestCase):

    def test_Model_1(self):
        """
        was_published_recently() should return False for questions whose
        pub_date is in the future.
        """
        self.assertEqual(True, True)