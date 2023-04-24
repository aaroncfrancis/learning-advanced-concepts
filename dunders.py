"""Simple example for my own reference for magic methods & dunders"""

class Person:

    def __init__(self, name, age):
        self.name = name 
        self.age = age

    def __del__ (self):
        print("Object is deconstructing")
  
p1 = Person('Aaron', 25)

class Vector: 

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __str__(self):
        return f"X: {self.x}. Y: {self.y}"
    
    # def __repr__(self):
    #     return f"X: {self.x}. Y: {self.y}"
    
v1 = Vector(12,15)
v2 = Vector(10,10)
v3 = v1 + v2

# print(v3.x,',',v3.y)  

"""If we use the string or represent dunders and use an f string we can clean it up"""
print(v3)

