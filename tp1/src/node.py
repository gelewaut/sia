class Node(object):
    def __init__(self, board, parent, cost):
        self.board = board
        self.parent = parent
        self.cost = cost 
        self.heuristic = 0

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return (self.board == other.board).all() and self.cost == other.cost

    def __hash__(self):
        if self.cost == 0:
            return hash(str(self.board))
        return hash(str(self.board)+str(self.cost))
    
    def getParent(self):
        return self.parent
    
    def getBoard(self):
        return self.board

    def getCost(self):
        return self.cost
    
    def setHeuristic(self,n):
        self.heuristic=n
        
    def getHeuristic(self):
        return self.heuristic
