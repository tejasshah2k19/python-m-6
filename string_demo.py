#string -> collection of characters 
#   single character or more than one character 
#   we can make string by enclosing character(s) in quote , single quoute or double quote 


# data = "royal education"
# data2 = 'royal education'

#strings are immutable in python. 
#self destructive - if we perform any operation on string it will create new memory all the time 
#we can access string characters via index. 
#index always starts with 0 and ends with length-1 

data = "royaleducation"
print(data)
print(data[0]) # r
print(data[1]) # o 
print(data[0:3])  # 0 1 2 
print(data[2:7])  # 2 3 4 5 6  

#we can access string data  in backward index 
print(data[-1]) # n
print(data[-2]) # o
print(data[::]) # full string 
print(data[::-1]) # reverse 

print(data[::2]) # ryldcto 


#operators 

#asterik 
#plus 
str = "royal"

print(str*3)
print(str+str)


#membership operator [ in , not in ]

str ="royal game"

if "game" in str:
    print("game is present") 
else:
    print("not found")

#relational operator 

a = "jay"
b = "viru"


if a == b:
    print("a == b")

if a > b :
    print("a > b ")

if a < b:
    print(" a < b ")




