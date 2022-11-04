"""
   #built in function
a=10
b=10
c=sum((a,b))
print(c)
"""
"""
#user define function
def fun1(a,b):
    print("Hello My name is Soyal Qureshi", a+b)

def fun2(a,b):
    average = (a+b)/2
    print(average)
print(fun2(5,7))    
"""

#user define function         {for value store any variable}
def fun1(a,b):
    print("Hello My name is Soyal Qureshi", a+b)

def fun2(a,b):
    average = (a+b)/2
  # print(average)
    return average
s=fun2(5,7)      #{for value store any variable}
print(s)
