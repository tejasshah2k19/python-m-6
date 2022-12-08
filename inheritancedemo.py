class Parent:
    def add(self):
        print("Parent::add()")

class Child(Parent):
    def sub(self):
        print("Child::sub()")
    def add(self):
        print("Child::add()")

p = Parent()
c = Child() 

p.add()  
c.sub()
c.add()





