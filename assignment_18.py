# Assignment:
# Create a class Product with a private attribute _price.
#  Use @property to get the price, @price.setter to update it, and @price.deleter to delete it.

class Product:
    def __init__(self,price):
        self._price = price


    @property
    def price(self):
        return self._price
    

    @price.setter
    def price(self,value):
        self._price = value


    @price.deleter
    def price(self):
        del self._price




product1 = Product(50)
print(product1.price)
product1.set_price = 40
print(product1.price)
del product1.price