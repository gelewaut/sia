# 0 espacio
# 1 pared
# 2 caja
# 3 destino
# 4 agente

AGENT = 4
BOX = 2
DESTINY = 3
WALL = 1
SPACE = 0
BOX_ON_DESTINY = 5
AGENT_ON_DESTINY = 6

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

def find_agent(board, size):
    for i in range(size):       
        for j in range(size):   
            if board[i][j] == AGENT or board[i][j] == AGENT_ON_DESTINY:
                return i,j
            
def find_walls(board, size):
    walls = []
    for i in range(1,size-1) :       
        for j in range(1,size-1):   
            if board[i][j] == WALL:
                aux = [i,j]
                walls.append(aux)
    return walls
            

def find_destinies(board, size):
    destinies = []
    for i in range(size):       
        for j in range(size):   
            if board[i][j] == DESTINY or board[i][j] == BOX_ON_DESTINY or board[i][j] == AGENT_ON_DESTINY :
                aux = [i,j]
                destinies.append(aux)
    return destinies

def solution(board, boxes):
    for box in boxes:
        y = box[0]
        x = box[1]
        if board[y][x] == BOX:
            return False
    return True

def can_continue(board, boxes):
    for box in boxes:
        y = box[0]
        x = box[1]
        if board[y][x] == BOX:
            if board[y-1][x] == WALL:
                if board[y][x-1] == WALL or board[y][x+1] == WALL:
                    return False
            if board[y+1][x] == WALL:
                if board[y][x-1] == WALL or board[y][x+1] == WALL:
                    return False
    return True

def find_boxes(board, size):
    boxes = []
    for i in range(size):
        for j in range(size):
            if board[i][j] == BOX or board[i][j] == BOX_ON_DESTINY:
                aux = [i,j]
                boxes.append(aux)
    return boxes
            
def move_agent(board, x, y, direction):
    new = board.copy()
    
    if direction == DOWN:
        if new[y+1][x] == WALL:
            return new,False
        
        elif new[y+1][x] == SPACE:
            new[y+1][x] = AGENT
            if new[y][x] == AGENT_ON_DESTINY:
                new[y][x] = DESTINY
            else:         
                new[y][x] = SPACE

        elif new[y+1][x] == DESTINY:
            new[y+1][x] = AGENT_ON_DESTINY
            if new[y][x] == AGENT_ON_DESTINY:
                new[y][x] = DESTINY
            else:         
                new[y][x] = SPACE
        
        
        elif new[y+1][x] == BOX or new[y+1][x] == BOX_ON_DESTINY:
            if new[y+2][x] == WALL or new[y+2][x] == BOX or new[y+2][x] == BOX_ON_DESTINY:
                return new,False
            
            if new[y+2][x] == SPACE:
                new[y+2][x] = BOX
            elif new[y+2][x] == DESTINY:
                new[y+2][x] = BOX_ON_DESTINY

            if new[y+1][x] == BOX_ON_DESTINY:
                new[y+1][x] = AGENT_ON_DESTINY
                if new[y][x] == AGENT_ON_DESTINY:
                    new[y][x] = DESTINY
                else:         
                    new[y][x] = SPACE
            else:
                new[y+1][x] = AGENT
                if new[y][x] == AGENT_ON_DESTINY:
                    new[y][x] = DESTINY
                else:         
                    new[y][x] = SPACE
        return new,True
            
    elif direction == UP:
        if new[y-1][x] == WALL:
            return new,False
        
        elif new[y-1][x] == SPACE:
            new[y-1][x] = AGENT
            if new[y][x] == AGENT_ON_DESTINY:
                new[y][x] = DESTINY
            else:         
                new[y][x] = SPACE

        elif new[y-1][x] == DESTINY:
            new[y-1][x] = AGENT_ON_DESTINY
            if new[y][x] == AGENT_ON_DESTINY:
                new[y][x] = DESTINY
            else:         
                new[y][x] = SPACE
        
        
        elif new[y-1][x] == BOX or new[y-1][x] == BOX_ON_DESTINY:
            if new[y-2][x] == WALL or new[y-2][x] == BOX or new[y-2][x] == BOX_ON_DESTINY:
                return new,False
            
            if new[y-2][x] == SPACE:
                new[y-2][x] = BOX
            elif new[y-2][x] == DESTINY:
                new[y-2][x] = BOX_ON_DESTINY

            if new[y-1][x] == BOX_ON_DESTINY:
                new[y-1][x] = AGENT_ON_DESTINY
                if new[y][x] == AGENT_ON_DESTINY:
                    new[y][x] = DESTINY
                else:         
                    new[y][x] = SPACE
            else:
                new[y-1][x] = AGENT
                if new[y][x] == AGENT_ON_DESTINY:
                    new[y][x] = DESTINY
                else:         
                    new[y][x] = SPACE
        return new,True



    elif direction == LEFT:
        if new[y][x-1] == WALL:
            return new,False
        
        elif new[y][x-1] == SPACE:
            new[y][x-1] = AGENT
            if new[y][x] == AGENT_ON_DESTINY:
                new[y][x] = DESTINY
            else:         
                new[y][x] = SPACE

        elif new[y][x-1] == DESTINY:
            new[y][x-1] = AGENT_ON_DESTINY
            if new[y][x] == AGENT_ON_DESTINY:
                new[y][x] = DESTINY
            else:         
                new[y][x] = SPACE
        
        
        elif new[y][x-1] == BOX or new[y][x-1] == BOX_ON_DESTINY:
            if new[y][x-2] == WALL or new[y][x-2] == BOX or new[y][x-2] == BOX_ON_DESTINY:
                return new,False
            if new[y][x-2] == SPACE:
                new[y][x-2] = BOX
            elif new[y][x-2] == DESTINY:
                new[y][x-2] = BOX_ON_DESTINY

            if new[y][x-1] == BOX_ON_DESTINY:
                new[y][x-1] = AGENT_ON_DESTINY
                if new[y][x] == AGENT_ON_DESTINY:
                    new[y][x] = DESTINY
                else:         
                    new[y][x] = SPACE
            else:
                new[y][x-1] = AGENT
                if new[y][x] == AGENT_ON_DESTINY:
                    new[y][x] = DESTINY
                else:         
                    new[y][x] = SPACE
        return new,True

    elif direction == RIGHT:
        if new[y][x+1] == WALL:
            return new,False
        
        elif new[y][x+1] == SPACE:
            new[y][x+1] = AGENT
            if new[y][x] == AGENT_ON_DESTINY:
                new[y][x] = DESTINY
            else:         
                new[y][x] = SPACE

        elif new[y][x+1] == DESTINY:
            new[y][x+1] = AGENT_ON_DESTINY
            if new[y][x] == AGENT_ON_DESTINY:
                new[y][x] = DESTINY
            else:         
                new[y][x]= SPACE
        
        
        elif new[y][x+1] == BOX or new[y][x+1] == BOX_ON_DESTINY:
            if new[y][x+2] == WALL or new[y][x+2] == BOX or new[y][x+2] == BOX_ON_DESTINY:
                return new,False

            if new[y][x+2] == SPACE:
                new[y][x+2] = BOX
            elif new[y][x+2] == DESTINY:
                new[y][x+2] = BOX_ON_DESTINY

            if new[y][x+1] == BOX_ON_DESTINY:
                new[y][x+1] = AGENT_ON_DESTINY
                if new[y][x] == AGENT_ON_DESTINY:
                    new[y][x] = DESTINY
                else:         
                    new[y][x] = SPACE
            else:
                new[y][x+1] = AGENT
                if new[y][x] == AGENT_ON_DESTINY:
                    new[y][x] = DESTINY
                else:         
                    new[y][x] = SPACE
        return new,True

    
