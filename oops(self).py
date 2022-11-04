class Student:
    no_of_leaves=5

    def printdetails(self):
        return f"Age is {self.age}, Std is {self.std} and City is {self.city}"

soyal=Student()
soyal.std="MCA"
soyal.subject= ["java", "python", "DSA"]
soyal.age=22
soyal.city="sikar"

Ali=Student()
Ali.std="BCA"
Ali.age=20
Ali.city="jaipur"

print(soyal.printdetails())
