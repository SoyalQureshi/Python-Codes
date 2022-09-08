# Exercise 2 - Faulty Calculator
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# Design a calculator which will correctly solve all the problems except
# the following ones:
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# Your program should take operator and the two numbers as input from the user
# and then return the result
""""
print("Hey Here is your calculator")
print("Enter the numbers according to the  instructions")
a = int(input("Enter your first number: "))
o = input("Enter the operator: ")
b = int(input("Enter the second number: "))

if (a == 45 and o == "*" and b == 3):
    print("555")
elif a == 56 and o == "+" and b == 9:
    print("77")
elif a == 56 and o == "/" and b == 6:
    print("4")
elif o == "*":
    print(a*b)
elif o == "+":
    print(a+b)
elif o == "/":
    print(a/b)
elif o == "-":
    print(a-b)
else: print("Your syntax may be incorrect")
"""

a = int(input("enter the first number"))
b = int(input("enter the second number"))
o = (input("enter the operator"))

if(a==10 and b==10 and o=="+"):
    print("15")
elif(a==30 and b==30 and o=="*"):
    print("3")
elif(a==55 and b==5 and o=="/"):
    print("4")
elif(o=="+"):
    print(a+b)
elif(o=="*"):
    print(a*b)
elif(o=="/"):
    print("a/b")
else:print("your syntax may be incorrect")
