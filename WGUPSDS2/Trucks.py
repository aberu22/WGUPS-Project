import datetime

class Truck:
    # Class variable to keep track of the next available truck ID
 

    def __init__(self, address, Maxpackages, departure_time, weight, mph, packages, speed):
        
 
        self.address = address
        self.Maxpackages= Maxpackages
        self.departure_time = departure_time 
        self.weight = None
        self.mph = mph
        self.packages = packages
        self.speed = speed
        self.time = departure_time

    def __str__(self):
        return f"{self.address}, {self.Maxpackages}, {self.departure_time}, {self.weight}, {self.mph}, {self.packages}, {self.speed}"
