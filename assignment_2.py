# Assignment:
# Create a class Counter that keeps track of how many objects have been created.
# Use a class variable and a class method with cls to manage and display the count.


class counter:
    count = 0

    def __init__(self):
        counter.count +=1


    @classmethod
    def showContent(cls):
        print(f"count is {cls.count}")


obj1 = counter()
obj2 = counter()

counter.showContent()