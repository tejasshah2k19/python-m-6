#no retur no argument 
def add():
    a  = int(input("Enter a number"))
    b = int(input("Enter a number"))
    c = a+b
    print("Addition = ",c)

#no return with argument 
def sub(a,b):
    c = a-b
    print("Subtraction = ",c)

#return with argument 
def mul(a,b):
    print("mul = ",a*b)
    return a*b

#keyword argument 
def printMe(name,city,pincode):
    print("name => ",name)
    print("city => ",city)
    print("Pincode => ",pincode)


# add() # calling 
# sub(30,20)
# ans =  mul(30,20)
# print("mul ans again => ",ans)
# print("done")

printMe("ram","ayodhya",380015)
printMe(pincode=12345,name="laxman",city="Ayodhya")

 