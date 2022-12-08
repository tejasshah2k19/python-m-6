#from abc import abstractmethod 

#  class A 
#       @abstracmethod 
#       def add(self):
#           return 

#class level abstraction -> interface [ pure abstract class ]

import  abc 

class Trai:

    def call(self):
        pass
    @abc.abstractmethod
    def recharge(self):
        pass
    def ct(self):
        print("Trai::ct()")    

class Dot:
    def ct(self):
        print("Dot::ct()")    

class Jio(Dot,Trai):
    def call(self):
        print("jio:call Free")

class Vodafone(Trai):
    def call(self):
        print("vodafone:call 1paisa")


j = Jio()
j.call()
j.ct()