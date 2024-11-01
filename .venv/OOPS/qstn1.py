#  Define a employee class with attributes role, dept, sal . This class also has a showDetails() method.
# create a Engineer class that inherits properties of employee and has attributes name and age.

class Employee():
    def __init__(self, role, dept, sal):
        self.role = role
        self.dept = dept
        self.sal = sal

    def showDetails(self):
        print("role is:", self.role)
        print("dept is:", self.dept)
        print("sal is:", self.sal)
        

class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Tester", "IT", 65000)

eng1 = Engineer("Rakesh", 29)
eng1.showDetails()