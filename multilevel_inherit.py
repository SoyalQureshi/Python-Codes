class dad:
    cricket = 1
    

class son(dad):
    dance = 2
    def isdance(self):
        return f"yes I dance {self.dance} no. of times"
   

class grandson(son):
    dance = 5
    
    def __init__(self, fname,lname):
        self.fname = fname
        self.lname = lname
        
    def fullname(self):
            return f"my name is {self.fname} {self.lname}"

    def isdance(self):
        return f"jackson yeah!" \
               f"yes I dance awesomely {self.dance} no. of times"

dadu = dad()
beta = son()
pota = grandson("ali", "boy")
dad.cricket=5
print(beta.cricket)

print(pota.isdance())
#print(a)
#print(pota.cricket())
print(pota.fullname())
