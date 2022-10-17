list = []  # empty list

print(type(list))

list1 = [11,2,3,4,5,11]
list2 = [1,2,3,"ram","sita",30.20]


print(list)
print(list1)
print(list2)

# list is a dynamic array 
# you can access individual data item using index , start:0,end:size-1 
# you are allowed to add duplicate data 
# its not sorted but its ordered [index]
# list item data are changeable 

print(list1[0])
print(list1[-1]) # last 
print(list1[0:4])
# print(list1[55])

# in 
# not in 

list = [1,2,3,4,5,6]

print(7 in list)
print(7 not in list)


list1 = [1,2,3]
list2=  [1,2,1]
list3 = [1,2,1]


if list1 > list2:
    print(" list1 ")
else:
    print(" list2 ")

if list2 == list3:
    print(" == ")