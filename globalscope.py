"""
g = 10  #global variable
def function(n):
    print(n, "soyal qureshi")
    #g=9    #local variable
    global g    #it means allow to add the value in global variable.
    g = g+40
    print(g)    

function("This is me :")
"""

x = 89
def soyal():
    x = 20
    def ali():
        global x
        x = 88
    #print("befire calling ali()", x)
    ali()
    print("after calling ali()", x)

soyal() 
print(x)
