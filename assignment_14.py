# Assignment:
# Create a class Department and a class Employee. Use aggregation by having a Department object store
#  a reference to an Employee object that exists independently of it.


class Employee:

    def __init__(self , name , empID):
        self.name = name
        self.empID = empID


    def get_detail(self):
        return f"Employee name {self.name} and employee ID is {self.empID}"
    

class Department:

    def __init__(self , name , emp):
        self.name = name
        self.emp = emp

    def show_department_info(self):
        return f"Department name : {self.name}: {self.emp.get_detail()}"
    

employee1 = Employee("uzair" , 5)

dep_info = Department("web dev" , employee1)


print(dep_info.show_department_info())