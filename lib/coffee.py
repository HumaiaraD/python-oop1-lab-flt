#!/usr/bin/env python3

class Coffee:
    def __init__(self, size, price):        
        size_options = ["Small", "Medium", "Large"]
        if size not in size_options:
            print("size must be Small, Medium, or Large.")
        else:
            self.size = size

        self.price = price

    def tip(self):
        self.price += 1
        print("This coffee is great, here's a tip!")