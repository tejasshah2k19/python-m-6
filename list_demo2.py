list = [1,2,3,4,5]

print(list)
print(len(list)) # len general function 

# list2 = list()

list.append(6)
print(list)

list.insert(0,-1)
print(list)

#modify 
list[0] = 100
print(list)


list1 = [11,22,33]
list2 = [10,20,30]

print(list1+list2)
print(list1)
print(list2)

list1.extend(list2)
print(list1)

list = ["ram","shyam","sita"]

print(list)
list.remove("shyam")
print(list)

list.pop(0)
print(list)

list = ["ram","shyam","sita"]
print(list)
list.pop() # remove top element - last element 
print(list)

#del list  # general 
list.clear()
print(list)


list = [10,20,30,40]
for data in list:
    print(data)
print("----------------------------------")
for i in range(0,len(list)):
    print(list[i])

"""
list = []
for i in range(1,6):
    print("enter number")
    num = int(input())
    list.append(num)

print(list)
"""


list = ["sita","ram","shyam"]
print(list)
list.sort()
print(list)

list = ["sita","ram","shyam"]
print(list)
list.sort(reverse=True)
print(list)

"""
#custom sort 

def mysort(item):
    

list = [1,2,3,4,5]
list.sort(key=mysort)
"""

#lambda 



#count() 
#index() -> list.index(7) -> index 

