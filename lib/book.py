#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count
        self.current_page = 1

    def turn_page(self, page_count):
        if not isinstance(page_count, int):
            raise TypeError("page_count must be an integer")
        
        if self.current_page < self.page_count:
            self.current_page += 1
            print("Flipping the page...wow, you read fast!")
        else:
            print("You are already on the last page.")
            
    
        