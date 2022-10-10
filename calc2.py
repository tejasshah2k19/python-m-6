print("Enter two numbers")
a = input()  # scan data from console - str 
a = int(a)
b = int(input()) 


print("1 for Add")
print("2 for Sub")
print("3 for Mul")
print("Enter your choice....")
choice = int(input())  

if (choice == 1): 
    c = a+b #10+20 => 1020 
    print("Addition = ",c)
if choice == 2:
    c = a-b
    print("Subtraction = ",c)
if choice == 3:
    c = a*b 
    print("Mul = ",c)