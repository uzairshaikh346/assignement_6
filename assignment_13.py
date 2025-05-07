# Assignment:
# Create a class Engine and a class Car. Use composition by passing an Engine object to the Car class during initialization.
#  Access a method of the Engine class via the Car class.


class Engine:

    def start(self):
        return "engine started..."
    
class Car:

    def __init__(self , engine):
        self.engine = engine

    def car_start(self):
        return self.engine.start()
    
my_engine = Engine()


my_car = Car(my_engine)

print(my_car.car_start())