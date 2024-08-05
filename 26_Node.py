class Node:
    def __init__(self,state,parent=None,action=None,path_cost=0):
        self.state=state
        self.parent=parent
        self.action=action
        self.path_cost=path_cost

    def __repr__(self):
        return "Node {} {}".format(self.state,self.path_cost)

    def __eq__(self, other):
        # checking other is of Same class
        return isinstance(other,Node) and \
               self.state==other.state and \
               self.parent==other.parent and \
               self.action==other.action and \
               self.path_cost==other.path_cost

    # check lower path Cost
    def __lt__(self, other):
        return isinstance(other, Node) and self.path_cost < other.path_cost
# end of class

n1=Node('Attock')
n2=Node('Islamabad',n1,'r1',5)
n3=Node('Islamabad',n1,'r1',5)
print(n1)
print(n2)
print(n1==n2)
print(n2==n3)
print(n1<n2)
print(n2<n3)

'''
map={'Attock':{'r1':'Rawalpindi','r2':'Nowshera'},
     'Nowshera':{'r1':'Attock','r2':"Rawalpindi"},
     'Rawalpindi':{'r1':'Attock','r2':'Nowshera','r3':'Islamabad'},
     'Islamabad':{'r1':'Rawalpindi'}
     }
'''
class Problem:
    def __init__(self,initial,goal,map):
       self.initial_state=initial
       self.goal_state=goal
       self.state_space=map

    def Actions(self,state):
        return self.state_space[state].keys()

    def Result(self,state,action):
        return self.state_space[state][action][0]

    def cost(self,state,action):
        return self.state_space[state][action][1]

    def Goal_test(self,state):
        return self.goal_state==state

# end of class
def child_Node(problem,parent,action):
    next_state=problem.Result(parent,action)
    next_cost=problem.cost(parent,action)
    next_node=Node(next_state,parent,action,parent.path_cost+int(next_cost))
    return next_node
# end of function

def Solution(node):
    path=[]
    while node:
        path.append(node)
        node=node.parent
    for n in reversed(path):
        print(n)
# end of function

from collections import deque
def BFS(problem):
    node=Node(problem.initial_state)
    if problem.Goal_test(node):
        return Solution(node)
    front=deque()
    explored=[]
    while True:
        if not front:
            return print("Failure")
        node=front.popright()
        explored.append(node.state)
        for action in problem.Actions(node.state):
            child=child_Node(problem,node,action)
            if child.state not in explored and child not in front:
                if problem.Goal_test(child):
                    return Solution(child)
                front.append(child)


map={ }
map['A']={'r1':['R',70],'r2':['N',30]}
map['N']={'r2':['A',30],'r3':['R',100],'r4':['P',40]}
map['P']={'r4':['N',40]}
map['I']={'r5':['R',10]}
map['R']={'r1':['A',70],'r3':['N',100],'r5':['I',10]}

p=Problem('N','I',map)
print(p.Actions('N'))
print(p.Result('A','r1'))
print(p.cost('A','r1'))
print(p.Goal_test('N'))
print(p.Goal_test('I'))

BFS(p)


