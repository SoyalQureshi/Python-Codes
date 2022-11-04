# Calculator

first = int(input("enter first number : "))
op = input("enter operator (+,-,*,/,%) : ")
second = int(input("enter second number : "))

if op == '+':
    print(first + second)
elif op == '-':
    print(first - second) 
elif op == '*':
    print(first * second) 
elif op == '/':
    print(first / second) 
elif op == '%':
    print(first % second) 

else:
    print("Invelid operation...")
