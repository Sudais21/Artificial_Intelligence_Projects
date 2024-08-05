
# Question 1
def Count(string,c):
    count=0
    for i in string:
        if i==c:
            count=count+1
    print(c, "Occurs",  count, "times")
    return count
# end of function
string=input("Enter a String:")
c=input("Enter number to check frequency:")
print(Count(string,c))






# Question 2
import statistics
data=eval(input("Enter Numbers: "))
def mean(data):
     return statistics.mean(data)

print("The mean is: ",mean(data))

def Sdeviation(data):
     return statistics.stdev(data)

print("The standard deviation is: ",Sdeviation(data))




# Question 3
# Conversion table of remainders to
# hexadecimal equivalent
conversion_table = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4',
                    5: '5', 6: '6', 7: '7',
                    8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C',
                    13: 'D', 14: 'E', 15: 'F'}
# function which converts decimal value
# to hexadecimal value
def decimalToHexadecimal(decimal):
     hexadecimal = ''
     while (decimal > 0):
          remainder = decimal % 16
          hexadecimal = conversion_table[remainder] + hexadecimal
          decimal = decimal // 16
     return hexadecimal

decimal_number=int(input("Enter Decimal number: "))
print("The hexadecimal form of", decimal_number,
      "is", decimalToHexadecimal(decimal_number))
'''
'''
# Question 4
table = {'0': 0, '1': 1, '2': 2, '3': 3,
              '4': 4, '5': 5, '6': 6, '7': 7,
              '8': 8, '9': 9, 'A': 10, 'B': 11,
              'C': 12, 'D': 13, 'E': 14, 'F': 15}
def hexToDecimal(hexString):
     res = 0
     # computing max power value
     size = len(hexString) - 1
     for num in hexString:
          res = res + table[num] * 16 ** size
          size = size - 1
     return res
hexString = input("Enter Hexadecimal Number: ").strip().upper()
print(hexToDecimal(hexString))
'''

'''
# Question 5
import time
class Stopwatch:
     # initialize the private fields of Stopwatch
     def __init__(self):
          self.startTime=time.time()
          self.endTime=None

      # method to get the startTime
     def getStartTime(self):
          return self.startTime

      # method to get the endTime
     def getEndTime(self):
          return self.endTime

     # method to start the stopwatch
     def start(self):
          self.startTime=time.time()

     # method to stop the stopwatch
     def stop(self):
          self.endTime=time.time()

     # method to get the elapsedTime
     def getElapsedTime(self):
          elapsedTime=None
          if(self.endTime!=None):
               elapsedTime=(self.endTime-self.startTime)*1000
          return elapsedTime

# method to test the class
timer=Stopwatch()
timer.start()
sum=0
for i in range (1,1000001):
     sum=sum+i
timer.stop()

print("Execution Time : "+str(timer.getElapsedTime())+ " milliseconds")
'''

'''
# Quesition 6
def successor(goal,state):
     h2=0
     for i in range (len(goal)):
          if goal[i]!="-" and goal[i]!=state[i]:
               l1=i
               l2=state.index(goal[i])
          x1=l1//len(goal)
          y1=l1%len(goal)
          x2=l2//len(goal)
          y2=l2%len(goal)
     h2+=abs(x2-x1)+abs(y2-y1)
     return h2
state=[8,7,5,1,6,2,4,3,"-"]
goal=[1,2,3,4,5,6,7,8,"-"]
print(successor(goal,state))
'''
'''
# Question 7
class Account:
    def __init__(self,a,b,c):
        self.id=a
        self.balance=b
        self.annualInterestRate=c
    def getId(self):
        return self.id

    def setId(self,m):
        self.id=m

    def getBalance(self):
        return self.balance

    def setBalance(self,n):
       self.balance=n

    def get_AnnualInterestRate(self):
        return self.annualInterestRate

    def set_AnnualInterestRate(self,v):
        self.annualInterestRate=v

    def get_MonthlyInterestRate(self):
        return (self.annualInterestRate/100)/12

    def get_MonthlyInterest(self):
        return self.balance*self.get_MonthlyInterestRate()

    def setwithdraw(self,amount):
        self.balance-=amount
    def getWithdraw(self):
        return self.balance

    def setdeposit(self,amount):
        self.balance+=amount

    def getDeposit(self):
        return self.balance

acc=Account(1122,20000,4.5)
print("Id: ",acc.getId())
print("Balance: ",acc.getBalance())
print("AnnualInterestRate: ",acc.get_AnnualInterestRate())
print("MonthlyAnnualInterestRate: ",acc.get_MonthlyInterestRate())
print("MonthlyInterest: ",acc.get_MonthlyInterest())
acc.setwithdraw(2500)
print("Balance After Withdraw: ",acc.getWithdraw())
acc.setdeposit(3000)
print("Balance After Deposit: ",acc.getDeposit())

'''
'''
# Question 8
import math
class Vector:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def __abs__(self):
        return math.sqrt(self.x**2+ self.y**2 + self.z**2)

    def __add__(self, vectorB):
        return self.x + vectorB.x, self.y + vectorB.y,self.z+vectorB.z

    def __sub__(self, vectorB):
        return self.x - vectorB.x, self.y - vectorB.y,self.z - vectorB.z

    def __mul__(self, vectorB):
        return self.x * vectorB.x + self.y * vectorB.y,self.z * vectorB.z

u=Vector(4,2,7)
v=Vector(5,1,3)
print(u+v)
print(u-v)
print(abs(u))
print(abs(v))
print(u==v)


# Question 9
map={'oradea':{'zerind':71,'sibiu':151},
     'zerind':{'oradea':71,'arad':75},
     'arad':{'zerind':75,'sibiu':140,'timisora':118},
     'sibiu':{'oradea':151,'arad':140,'rimnicu':80,'fagaras':99},
     'timisora':{'arad':118,'lugoj':111},
     'lugoj':{'mehadia':70,'timisora':111},
     'mehadia':{'lugoj':70,'drobeta':75},
     'drobeta':{'mehadia':75,'craiova':120},
     'craiova':{'drobeta':120,'pitesti':138,'rimnicu':146},
     'pitesti':{'rimnicu':97,'bucharest':101},
     'rimnicu':{'sibiu':80,'pitesti':97},
     'fagaras':{'sibiu':99,'bucharest':211},
     'bucharest':{'giurgiu':90,'pitesti':101,'fagaras':211,'urziceni':85},
     'giurgiu':{'bucharest':90},
     'urziceni':{'bucharest':85,'hirsova':98,'vaslui':142},
     'hirsova':{'urziceni':98,'eforie':86},
     'eforie':{'hirsova':86},
     'vaslui':{'urziceni':142,'iasi':92},
     'iasi':{'valsi':92,'neamt':87},
     'neamt':{'iasi':87}
     }
def cities(map):
    return map.keys()
print(cities(map))

def routes(map):
    return len(map)
print(routes(map))

def ConnectedCities(map,city):
     return map[city].keys()
city=input("Enter City: ")
print(ConnectedCities(map,city))


# Question 6
def get_successors(self, state):
    successors = []
    m_time = 1
    neighbour_list = self.get_valid_neighbours(state.position)
    for neighbour in neighbour_list:
        start_t = state.time + m_time
        end_t = state.interval[1] + m_time
        for i in self.sipp_graph[neighbour].interval_list:
            if i[0] > end_t or i[1] < start_t:
                continue
            time = max(start_t, i[0])
            s = state(neighbour, time, i)
            successors.append(s)
    return successors




















