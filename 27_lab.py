class PriorityQueue:
    def __init__(self):
        self.nodes = {}

    def push(self, node):
        if node.state not in self.nodes.keys():
            self.nodes[node.state] = node

    def pop(self):

        # Find Key with minmum path cost
        lst = list(self.nodes.keys())
        minNode = self.nodes[lst[0]]
        for k, n in self.nodes.items():
            if minNode.path_cost > n.path_cost:
                minNode = n
        del self.nodes[minNode.state]
        return minNode

    def IsEmpty(self):
        return not self.nodes

    def contains(self, node):
        return node.state in self.nodes.keys()

    def replace(self, node):
        if node.state in self.nodes.keys() and self.nodes[node.state].path_cost > node.path_cost:
            self.nodes[node.state] = node

    def __str__(self):
        str1 = ' '.join(str(e) for e in self.nodes.keys())
        return str1


# end of class--------------------------------------------------------------------------------
class Problem:
    def __init__(self, init_state, goal_state, map):
        self.initial_state = init_state;
        self.goal_state = goal_state;
        self.state_space = map;

    # End of def __init__(self, init_state, goal_state):

    def Actions(self, state):
        lst = self.state_space[state].keys()
        return lst

    # End of def Actions(self, state):

    def Result(self, state, action):
        return self.state_space[state][action][0]

    # End of def Result(self, state, action):

    def Goal_test(self, state):
        return state == self.goal_state

    # End of def Goal_test(self, state):

    def Cost(self, state, action):
        return self.state_space[state][action][1]
    # End of Path_cost(self, state, action):


# End of class Problem:______________________________________________________________________________
class Node:
    def __init__(self, state, parent=None, action=None, path_cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost

    def __repr__(self):
        return "<Node {} {}>".format(self.state, self.path_cost)

    def __lt__(self, node):
        return self.state < node.state

    def __eq__(self, other):
        return isinstance(other, Node) and self.state == other.state


# End of class Node________________________________________________________________________________

def next_state(args):
    pass


def child_node(problem, parent, action, ):
    next_state = problem.Result(parent.state, action)
    '''step_cost = problem.Cost(parent.state, action)'''
    step_cost = hn[next_state]
    next_node = Node(next_state, parent, action, step_cost)
    return next_node


# End of def child_node(problem,parent, action):

def solution(node):
    print("Solution")
    path_back = []
    while node:
        path_back.append(node)
        node = node.parent
    # End of while
    for n in reversed(path_back):
        print(n)
    # End of for


# End of def solution(node):______________________________________________________________________________
def GBS(problem):
    node = Node(problem.initial_state)
    frontier = PriorityQueue()
    frontier.push(node)
    explored = []
    while True:
        if frontier.IsEmpty(): return print('Failure')
        node = frontier.pop()
        # print(node) uncomment to understand working of algorithm
        if problem.Goal_test(node.state): return solution(node)
        explored.append(node.state)
        for action in problem.Actions(node.state):
            child = child_node(problem, node, action)
            if child.state not in explored and not frontier.contains(child):
                frontier.push(child)
            elif frontier.contains(child):
                frontier.replace(child)


# _____________ Program main part_________________________________________________________________
map = {};
map['Arad'] = {'R1': ['Zerind', 75], 'R2': ['Sibiu', 140], 'R3': ['Timisoara', 118]};
map['Zerind'] = {'R1': ['Oradea', 71], 'R2': ['Arad', 75]};
map['Oradea'] = {'R1': ['Sibiu', 152], 'R2': ['Zerind', 71]};
map['Timisoara'] = {'R1': ['Lugoj', 111], 'R2': ['Arad', 118]};
map['Lugoj'] = {'R1': ['Timisoara', 111], 'R2': ['Mehandia', 70]};
map['Drobeta'] = {'R1': ['Mehandia', 75], 'R2': ['Craiova', 120]};
map['Craiova'] = {'R1': ['Drobeta', 120], 'R2': ['Rimnicu Vilcea', 146], 'R3': ['Pitesti', 138]};
map['Rimnicu Vilcea'] = {'R1': ['Sibiu', 80], 'R2': ['Pitesti', 97], 'R3': ['Craiova', 146]};
map['Sibiu'] = {'R1': ['Arad', 140], 'R2': ['Fagaras', 99], 'R3': ['Oradea', 151], 'R4': ['Rimnicu Vilcea', 80]};
map['Fagaras'] = {'R1': ['Sibiu', 99], 'R2': ['Bucharest', 221]};
map['Pitesti'] = {'R1': ['Rimnicu Vilcea', 97], 'R2': ['Craiova', 138], 'R3': ['Bucharest', 101]};
map['Bucharest'] = {'R1': ['Fagaras', 221], 'R2': ['Pitesti', 101], 'R3': ['Giurgiu', 90], 'R4': ['Urziceni', 85]};
map['Giurgiu'] = {'R1': ['Bucharest', 90]};
map['Urziceni'] = {'R1': ['Bucharest', 85], 'R2': ['Valsui', 142], 'R3': ['Hirsova', 98]};
map['Hirsova'] = {'R1': ['Eforie', 86], 'R2': ['Urziceni', 98]};
map['Eforie'] = {'R1': ['Hirsova', 86]};
map['Valsui'] = {'R1': ['Urziceni', 142], 'R2': ['Iasi', 87]};
map['Iasi'] = {'R1': ['Valsui', 92], 'R2': ['Neamt', 87]};
map['Neamt'] = {'R1': ['Iasi', 87]};
map['Mehandia'] = {'R1': ['Lugoj', 70], 'R2': ['Drobeta', 75]}
hn = {}
hn['Arad'] = 366,
hn['Zerind'] = 374,
hn['Oradea'] = 380,
hn['Timisoara'] = 329,
hn['Lugoj'] = 244,
hn['Drobeta'] = 242,
hn['Craiova'] = 160,
hn['Rimnicu Vilcea'] = 193,
hn['Sibiu'] = 253,
hn['Fagaras'] = 176,
hn['Pitesti'] = 100,
hn['Bucharest'] = 0,
hn['Giurgiu'] = 77,
hn['Urziceni'] = 80,
hn['Hirsova'] = 151,
hn['Eforie'] = 161,
hn['Valsui'] = 199,
hn['Iasi'] = 226,
hn['Neamt'] = 234,
hn['Mehandia'] = 241,
problem = Problem('Iasi', 'Eforie', map)
GBS(problem)
