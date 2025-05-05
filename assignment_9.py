from abc import ABC , abstractclassmethod


class shape(ABC):

    @abstractclassmethod
    def area(self):
        pass


class rectangle(shape):

    def __init__(self, height , width):
        self.height = height
        self.width = width

        def area(self):
            return self.height * self.width
        
ground = rectangle(20, 4)
print("Area of the ground is", ground.area())
