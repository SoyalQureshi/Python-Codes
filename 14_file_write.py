"""
      #Write mode 
f = open("soy.txt", "w")
char = f.write("I am a problem solver and I am people's person\n")
print(char)   #print total character
f.close()
"""

"""
        #Append mode(jodna)
f = open("soy.txt", "a")
char = f.write("I am a problem solver and I am people's person\n")
print(char)   #print total character
f.close()
"""


        #'r+' read & write mode
f = open("soy.txt", "r+")
print(f.read())
f.write("thank you")
