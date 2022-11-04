class Employee: 
    no_of_leaves = 8  #class variable

    def __init__(self, aname, asalary, arole):   #constructor(Function)
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}, Salary is {self.salary} and role is {self.role}"

class Player:
    no_of_games=5

    def __init__(self, name, game):
        self.name = name
        self.game = game

    def printdet(self):
        return f"The name is {self.name}, game is {self.game}"

class Coolprogrammer(Employee, Player):  #this order is importent--
    language = "python"
    def printlanguage(self):
        print(self.language)

harry = Employee("Harry", 255, "Instructor")    #object
rohan = Employee("Rohan", 455, "Student")       #object

ali = Player("Ali",["Cricket"])
x=ali.printdet()
print(x)


soyal = Coolprogrammer("Soyal", 1000, "Coolprogrammer")
det=soyal.printdetails()
soyal.printlanguage()
print(det)

