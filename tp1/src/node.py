from functools import total_ordering

class Node(object):
    def __init__(self, board, parent, cost):
        self.board = board
        self.parent = parent
        self.cost = cost 

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return (self.board == other.board).all()

    def __hash__(self):
        return hash(str(self.board))
    
    def getParent(self):
        return self.parent
    
    def getBoard(self):
        return self.board

    def getCost(self):
        return self.cost

@total_ordering
class GreedyNode(object):
    def __init__(self, node, heuristic):
        self.node = node
        self.heuristic = heuristic

    def __eq__(self, other):
        return self.heuristic == other.heuristic
    
    def __lt__(self, other):
        return self.heuristic < other.heuristic

    def getNode(self):
        return self.node

@total_ordering
class StarNode(object):
    def __init__(self, node, heuristic):
        self.node = node
        self.heuristic = heuristic

    def __eq__(self, other):
        self_fn = self.heuristic + self.node.getCost()
        other_fn = other.heuristic + other.node.getCost()
        if self_fn == other_fn:
            return self.heuristic == other.heuristic
        return False
    
    def __lt__(self, other):
        self_fn = self.heuristic + self.node.getCost()
        other_fn = other.heuristic + other.node.getCost()
        if self_fn == other_fn:
            return self.heuristic < other.heuristic
        return self_fn < other_fn

    def getNode(self):
        return self.node