"""
print("How Many Row You Want To Print")
one= int(input())
print("Type 1 Or 0")
two = int(input())
new =bool(two)
if new == True:
    for i in range(1,one+1):
        for j in range(1,i+1):
            print("*",end=" ")
        print()
elif new ==False:
    for i in range(one,0,-1):
        for j in range(1,i+1):
            print("*", end="")
        print()
"""

"""
        #exercise
print("How many row you want to print")
first = int(input())
print("Type 1 or 0")
second = int(input())
new = bool(second)
if new == True:
    for i in range(1,first+1):
        for j in range(1,i+1):
            print("*", end="")
        print()

elif new == False:
    for i in range(first,0,-1):
        for j in range(1,i+1):
            print("*",end="")
        print()
"""

print("How many orw you want to print")
a = int(input())
print("Type 1 or 0")
b = int(input())
new = bool(b)
if new == True:
    for i in range(1,a+1):
        for j in range(1,i+1):
            print("*", end=" ")
        print()
elif new == False:
    for i in range(a,0,-1):
        for j in range(1,i+1):
            print("*", end=" ")
        print()



































