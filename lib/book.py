#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        if(type(page_count) in (int,float)):
            self.title = title
            self.page_count = page_count
        else:
            self.title = title
            print("page_count must be an integer")
            

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
