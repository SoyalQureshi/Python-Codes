"""
print("enter the no.")
num1=input()
print("enter the no.")
num2=input()
try:
    print("the sum of a=b=",int(num1)+int(num2))
except Exception as e:
    print("Error!")

print("this is the exception helding program")
"""

try:
	a = 10/0
	print (a)
except ArithmeticError:
		print ("This statement is raising an arithmetic exception.")
else:
    print ("Success.")
