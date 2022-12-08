class Base:
    def __init__(self):
        self.x = 10
        self.__y = 20   # __ underscore two times -> private 

class Derived(Base): 
    def printData(self):
        print(self.x)
        #print(self.__y)



c = Derived()
c.printData()