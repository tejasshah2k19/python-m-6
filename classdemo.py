class Person:
    name = ""  #instance variable 

    def __init__(self,name,age):
        self.name = name 
        self.age = age
    #instance method
    def display(self):
        print(self.name)
        print(self.age)
    # default argument must start from right side and ends with left side with continue default args 
    def addAge(self,amount=5):
        self.age = self.age + amount 
    
    #due to c its invalid 
    # def invalidDefArgs(self,a,b=30,c,d=20,e=10):
    #     pass
 
#class -> state + behaaviour [ data memeber + member function ] [variable + methods ]



#object 

p = Person("ram",20)
q = Person("sita",20)

p.display()
q.display()

p.addAge() # no 
p.display()

q.addAge(10) # yes 
q.display()