l1 = ["Apple","Banana", "Graps","Mango"]
"""
i=1
for item in l1:
    if i%2 is not 0:
        print(f"Lucky please buy {item}")
    i += 1    
"""

#Enumerate function

for index, item in enumerate(l1):
    if index%2 == 0:
        print(f"Lucky please buy {item}")
