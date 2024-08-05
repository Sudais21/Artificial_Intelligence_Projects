import copy
class Problem(object):
    def __init__(self, initial, goal):
        self.goal = goal
        self.initial = initial
    # ______________________________________________________________________________


class Node:
    def __init__(self, state, goal=None):
        self.state = state
        self.goal = goal
        self.value = self.h1()
        self.successors = []

    def __repr__(self):
        return "<State={0} f={1} >".format(self.state, self.value)

    def __lt__(self, node):
        return self.value < node.value

    def childs(self):
        moves = ((1, 3), (0, 2, 4), (1, 5), (0, 4, 6), (1, 3, 5, 7), (2, 4, 8), (3, 7), (4, 6, 8), (7, 5))
        blank = self.state.index(0)
        for p in moves[blank]:
            child = copy.deepcopy(self.state)
            child[blank] = child[p]
            child[p] = 0
            node = Node(child, self.goal)
            # print(node)
            self.successors.append(node)

    def Best(self):
        self.childs()
        best = self.successors[0]
        for node in self.successors:
            if node.value < best.value:
                best = node
        return best

    def h1(self):
        count = 0
        for x, y in zip(self.state, self.goal):
            if y > 0 and x != y: count += 1
        return count

    def __eq__(self, other):
        return isinstance(other, Node) and self.value == other.value


# ______________________________________________________________________________
def HILL_CLIMBING(problem):
    current = Node(problem.initial, problem.goal)
    while True:
        neighbor = current.Best()
        print("Best", current)
        if current.value < neighbor.value:
            return current
        current = neighbor
    # ______________________________________________________________________________


# Program main part
initial = [8, 2, 5, 3, 6, 1, 7, 4, 0]
goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]
problem = Problem(initial, goal)
current = Node(problem.initial, problem.goal)
solution = HILL_CLIMBING(problem)
print("Solution", solution)

