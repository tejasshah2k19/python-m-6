str = "royal"
str = str.capitalize() #Royal 
print(str)

str = "royal education"
str = str.capitalize()
print(str)
str = str.title()
print(str)

str = "jony jony yes papa"
ans = str.count("jony")
print("jony present ",ans," time(s) ");

str = "jony jony yes papa"
str.count("jony",4,10)


#email -> tejas@royaledu.in 
#  XXXXX@royaledu.in 

str = "tejas@royaledu.in"
if str.endswith("@royaledu.in") : 
    print("Valid")
else:
    print("InValid")

#find - index 
#find and index both are same 
#index() will raise an exception if your substring not present 
str = "jony jony yes papa"

if "papa" in str:
    print("papa is present")

ans = str.find("papa")
print("papa located at => ",ans)

ans = str.find("baba")
print("baba located at => ",ans) # -1 

ans = str.index("papa") # 14 
# ans = str.index("baba") # Exception 

# upper()
# lower() 

str = "9510141151"
#isdigit()
#isalpha()
#isalnum()
#islower()
#isspace()

str = "jony jony yes papa"
str = str.replace("jony","tony")
print(str)

str = "jony jony yes papa"
str = str.replace("jony","tony",1)
print(str)
