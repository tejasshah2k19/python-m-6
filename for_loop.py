#[1 2 3 4 5 6 7 8 9 ]
'''
for i in range(1,51):
    print("i => ",i)
'''

'''
1
12
123
1234
12345 
'''


for i in [1,2,3,4,5]:
    for j in range(1,i+1): # 1 1,2   2  1,3[1,2] 
        print(j,end="")
    print("")

