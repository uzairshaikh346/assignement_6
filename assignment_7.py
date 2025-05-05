class Employee:
    def __init__(self,name,salary,ssn):
        self.name = name
        self._salary = salary
        self.__ssn = ssn

emp1 = Employee("uzair",40000, 123-123-123)

print(f"Name : {emp1.name}")

print(f"Salary : {emp1._salary}")


try:
    print(f"snn : {emp1.__ssn}")
except AttributeError:
    print("Cannot access __ssn directly (private variable)")

        