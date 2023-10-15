#!/usr/bin/env python3

class Shoe:
    def __init__(self,name,model,type):
        self.name = name 
        self.model = model
        self.type = type
        
    def get_name(self):
        print(f"This is a {self.name} shoe")
        
    def get_model(self):
        print(f"The model of this shoe is {self.model}")
        
    def get_type(self):
        print(f"This is a {self.type} type of shoe")

s2 = Shoe("Bola","Joshua","Kunle")
print(s2.get_model())
print(s2.get_name())
print(s2.get_type())