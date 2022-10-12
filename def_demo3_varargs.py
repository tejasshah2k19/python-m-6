#varargs 
#varaible length arguments 

# def add(a,b):
# def add(a,b,c):
# def add(a,b,c,d):

def add(*n):
    sum = 0 
    for x in n:
        sum = sum + x 
    print("Add = ",sum)
 



add(1,2,3) #6
add(1,2) #3
add(1,2,3,4,5,6) #21
add() #  
