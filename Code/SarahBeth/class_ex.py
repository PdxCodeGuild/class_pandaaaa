import math

def distance(p1, p2):
    dx = p1['x'] - p2['x']
    dy = p1['y'] - p2['y']
    return math.sqrt(dx*dx + dy*dy)

p1 = {'x': 5, 'y': 2}
p2 = {'x': 8, 'y': 4}
# print(distance(p1, p2))

b1 = {'x': 1, 'y': 23}
b2 = {'x': 82, 'y': 14}
# print(distance(b1, b2))


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

class BigObject: 


# 
p1 = Point(5, 2) # call the initializer, instantiate the class
p2 = Point(8, 4)

# print(p2)
# print(repr(p2))
p_copy = repr(p2)
print(p_copy)
# print(p1.x) # 5
# print(p1.y) # 2
# print(type(p1)) # Point
# print(p1.distance(p2))

#  # similar to how we can call methods of the string class
# s = 'sdfasdf'
s = str('hello world')
words = s.split(' ')

# print(words)


    