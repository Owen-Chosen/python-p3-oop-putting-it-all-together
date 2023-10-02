#!/usr/bin/env python3

class Shoe:
    cobble = ""
    def __init__(self, brand, size):
        if(type(size) in (int, float)):
            self.brand = brand
            self.size = size
        else:
            self.brand = brand
            print("size must be an integer")

    def cobble(self):
        

