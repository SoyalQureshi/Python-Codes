class Student:

    def __init__(self,name,age,rollno,city):
        self.name = name
        self.age = age
        self.rollno = rollno
        self.city = city

    def student_details(self):
        print("Name of student is :", self.name)
        print("Age of student is :", self.age)
        print("Rollno of student is :", self.rollno)
        print("city of student is :", self.city)

s1=Student("Soyal",22,620,"Jaipur")
s2=Student("khan",20,621,"Goa")

s1.student_details()
s2.student_details()
