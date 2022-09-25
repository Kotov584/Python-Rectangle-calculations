# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 17:03:14 2022

@author: sotdo
"""


class Rectangle(): 
    def __init__(self, length, width):
        if float(length > 0) and float(width > 0): 
            self.length = length
            self.width  = width
        else:
            return False
        
    def get_area(self):
        return self.width * self.length
    
    def get_perimeter(self):
        return 2 * (self.width + self.length)
    
    def vertical_orientation(self): 
        if self.width > self.length :
            return True
        return False 
    
if __name__ == "__main__": 
    rectangle = Rectangle(123, 123)
    print(rectangle.get_area()) 
    
    
