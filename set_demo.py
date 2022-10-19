s = {1,2,3,4,1,2,3}
print(s)
# print(s[0])

print(len(s))

s.add(5)
print(s)
s.discard(3)
# s.remove(3) #pop()
print(s)
s.clear()
print(s)


a= {1,2,3,4}
b ={1,2,3,5}

ab = a.union(b)
abc = a.intersection(b)
amb = a.difference(b)

#a.difference_update(b) # a = a-b 
print(a)
print(b)
print(ab)
print(abc)
print(amb)

# 5 Lac
# 7 Lac 
# 10 Lac 


x = {1,2,3,4}
y = {1,2}

print(x.issuperset(y))
print(y.issubset(x))


#json