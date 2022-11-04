class Employee: 
    no_of_leaves = 8  #class variable

    def __init__(self, aname, asalary, arole):   #constructor(Function)
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}, Salary is {self.salary} and role is {self.role}"
"""
    @classmethod    #change leaves method
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))

    @staticmethod
    def printgood(string):
        print("This is good " + string)
"""

class Programmer(Employee):
    no_of_holiday = 56
    def __init__(self, aname, asalary, arole, alanguages):
        self.name = aname
        self.salary = asalary
        self.role = arole
        self.languages = alanguages


    def printprog(self):
        return f"The Programmer's Name is {self.name}. Salary is {self.salary} and role is {self.role}.The languages are {self.languages}"



harry = Employee("Harry", 255, "Instructor")    #object
rohan = Employee("Rohan", 455, "Student")       #object

shubham = Programmer("Shubham", 555, "Programmer", ["python"])
karan = Programmer("Karan", 777, "Programmer", ["python", "Cpp"])
print(shubham.printdetails())
