# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 18:50:16 2022

@author: pclab
"""

import unittest
from code import Rectangle


class TestValues(unittest.TestCase):

    def setUp(self):
        self.rectangle = Rectangle(2, 2) 
         
    def test_get_area(self):
        self.assertEqual(self.rectangle.get_area(), 4, 'Area is not correct') 
         
    def test_get_perimeter(self):
        self.assertEqual(self.rectangle.get_perimeter(), 8, 'Perimeter is not correct') 
    
    def test_vertical_orientation(self):
        self.assertGreater(2, 2, 'Width is lower than length')
#
if __name__ == '__main__':
    unittest.main() 