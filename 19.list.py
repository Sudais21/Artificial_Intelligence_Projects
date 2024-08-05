
std=["Ali",10,"BCS",3.5]
print(std[0])
print(std[0:2])
print(std[1:3])
'''
'''
list=[]
flag=True
while flag:
    n=input("Enter any number:")
    if n=='N':
        flag=False
    else:
        list.append(int(n))

print(len(list))
print(min(list))
print(max(list))
print(sum(list))
# Average
print(sum(list)/len(list))

import random
list=[10,15,8,6,20,30]
for i in list:
    print(i)
# it will check this is present or not
print(15 in list)
print(25 in list)

# shuffle function is used to shuffle the list randomly
random.shuffle(list)
for i in list:
    print(i)

