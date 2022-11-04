"""
class Student:
    pass

soyal=Student()
soyal.std="MCA"
soyal.subject= ["java", "python", "DSA"]
soyal.age=22
soyal.city="sikar"

Ali=Student()
Ali.std="BCA"
Ali.age=20
Ali.city="jaipur"

print(soyal.std, soyal.age, soyal.city, soyal.subject)
print(Ali.std, Ali.age, Ali.city)
"""

"""
class Student:
    holiday=2   #access by any object(propety of class){share}
    pass

soyal=Student()
soyal.std="MCA"
soyal.subject= ["java", "python", "DSA"]
soyal.age=22
soyal.city="sikar"

Ali=Student()
Ali.std="BCA"
Ali.age=20
Ali.city="jaipur"

print(soyal.__dict__)  #print the all values of soyal in dictionary form
#print(Student.__dict__)

print(Ali.holiday)
Student.holiday=3  #change value by only class name
print(Ali.holiday)
"""

class Phone:
    def set_color(self,color):
        self.color=color
        print(self.color)
    
    def set_cost(self,cost):
        self.cost=cost
        print(self.cost)
        
    # def show_color(self):
    #     print(self.color)
        
    # def show_cost(self):
        # print(self.cost)
    
    def make_call(self):
        print("I'm making call")
    def play_game(self):
        print("I'm playing game")
        
p1=Phone()

p1.set_color("Red")
p1.set_cost(10000)
# p1.show_color()
# p1.show_cost()

p1.make_call()
p1.play_game()