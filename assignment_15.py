# Assignment:
# Create four classes:

# A with a method show(),

# B and C that inherit from A and override show(),

# D that inherits from both B and C.

# Create an object of D and call show() to observe MRO.

class A:
    def show(self):
        return "A's show method"
    
class B(A):
    def show(self):
        return "B's show method"

class C(A):
    def show(self):
        return "C's show method"
    

class D(B , C):
    pass


d = D()


print(d.show())


print(D.__mro__)
