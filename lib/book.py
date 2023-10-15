#!/usr/bin/env python3

class Book:
    def __init__(self,name,types):
        self.name = name 
        self.types = types 
        
    def get_name(self):
        print(f"This is {self.name} book")
        return self.name
    
    def get_type(self):
        print(f"This is {self.types} type of book")
        return self.types
    

s1 = Book("Biology","2D")
s1.get_name()
s1.get_type()

    
    
        