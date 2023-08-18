# Heuristica 1: Calcular la distancia minima entre un agente y la caja mas cercana.
# Es admisible pues como minimo el agente tendra que recorrer la distancia a la caja
# mas cercana, por lo tanto h(n) <= costo de la solucion siempre

from src.node import Node
import src.sokoban as sok 

def find_closest_box_bfs(board, size):
    distance = 0
    Fr = []
    Exp = set()
    n0 = Node(board, 0, 0)
    if (sok.can_continue(board, sok.find_boxes(board, size))):
        Fr.append(n0)
    board_aux = board

    while len(Fr) != 0:
        aux = Fr.pop(0)
        if agent_next_to_box(aux.getBoard(), sok.find_agent(aux.getBoard(), size)):
            distance += 1
            return distance
        y,x = sok.find_agent(aux.getBoard(), size)

        append_fronteer_bfs(Fr, Exp, aux, size, x,y, sok.UP)
        append_fronteer_bfs(Fr, Exp, aux, size, x,y, sok.DOWN)
        append_fronteer_bfs(Fr, Exp, aux, size, x,y, sok.LEFT)
        append_fronteer_bfs(Fr, Exp, aux, size, x,y, sok.RIGHT)
                        
    return 0

def append_fronteer_bfs(fronteer, explored, current_node, size, x, y, direction):
    board_aux,movement = sok.move_agent(current_node.getBoard(), x, y, direction)
    if movement and sok.can_continue(board_aux, sok.find_boxes(board_aux, size)):
        distance += 1
        node = Node(board_aux, current_node, 0)
        if node not in explored:
            fronteer.append (node)
            

def agent_next_to_box(agent, board):
    x = agent[1]
    y = agent[0]
    if board[y+1][x] == sok.BOX or board[y-1][x] == sok.BOX or board[y][x+1] == sok.BOX or board[y][x-1] == sok.BOX:
        return True
    return False






