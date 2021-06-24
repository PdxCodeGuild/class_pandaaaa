#Zach Watts
#Class Practice

import math

class Point:
    def __init__(self, x, y): # this is the initializer
        self.x = x # these are member variables
        self.y = y
    def __str__(self): # specify a str conversion
        return 'point is: ['+str(self.x)+','+str(self.y)+']'  
    def __repr__(self):
        return f'Point({self.x},{self.y})'
    def distance(self, p): # method, or 'member function'
        dx = self.x - p.x
        dy = self.y - p.y
        return math.sqrt(dx*dx + dy*dy)