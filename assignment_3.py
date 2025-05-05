# Assignment:
# Create a class Car with a public variable brand and a public method start(). 
# Instantiate the class and access both from outside the class.

class car:
    def __init__(self , name):
        self.name = name

    def start(self):
        print(f"{self.name} is starting...")

car1 = car("civic")

car1.start()


