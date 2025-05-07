# Assignment:
# Create a class Multiplier with an __init__() to set a factor. Define a __call__() method that multiplies an input by the factor. 
# Test it with callable() and by calling the object like a function.


class Multiplier:
    def __init__(self , factor):
        self.factor = factor

    def __call__(self, value):
        return self.factor * value
    


double_val = Multiplier(5)

print(callable(double_val))

res = double_val(2)

print(res)
        