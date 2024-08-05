list=[]
for i in range(1000,2001):
    list.append(i)
print(list)

lst=[]
lst=[i for i in range(1000,2001)]
print(lst)

lst2=[i*2 for i in range(10,20)]
print(lst2.pop()) # it will remove the last element
print(lst2.pop(3)) # it will remove the third index
print(lst2.remove(20)) # it will remove 20 from the list
print(lst2)

#print(lst.index(24)) # it will return element on 24 index

def HammingDistance(goal,state):
    h1=0
    for i in range(len(goal)):
        if goal[i]!="-" and goal[i]!=state[i]:
            h1 +=1
    return h1
# end of function
state=[3,2,1,4,5,6,7,8,"-"]
goal=[1,2,3,4,5,6,7,8,"-"]
print(HammingDistance(goal,state))

def ManhattanDistance(goal,state):
    h2=0
    for i in range(len(goal)):
        if goal[i]!="-" and goal[i]!=state[i]:
            l1=i
            l2=state.index(goal[i])

            x1=l1//len(goal)
            y1=l1%len(goal)

            x2=l2//len(goal)
            y2=l2%len(goal)

            h2+=abs(x2-x1)+abs(y2-y1)

    return h2
# end of function
state=[3,2,1,4,5,6,7,"-",8]
goal=[1,2,3,4,5,6,7,8,"-"]
print(HammingDistance(goal,state))

# Dictionary
d1={'Name':'Sudais','Class':'BSE','Age':20}
for key in d1:
    print(key)

print(d1.keys())
print(d1.values())
print(d1.items())

map={'PER':{'DRW':48,'ADL':32},
     'ADL':{'PER':32,'ASP':24,'MEL':18},
     'DRW':{'PER':48,'ASP':15},
     'ASP':{'ADL':24,'DRW':15,'BNE':30,'MEL':40},
     'BNE':{'ASP':30,'SYD':31},
     'SYD':{'BNE':31,'MEL':15},
     "MEL":{'SYD':15,'ASP':40,'ADL':18} }
print(map)
print(map.keys())
print(map.values())
#print(map.values().keys())
print(len(map))


'''
for key,value in map.items():
    print(key,value)
    '''









