from src.node import Node, StarNode
import src.sokoban as sok 
import time

# return Bool for success, cost, cant nodes expanded, cant nodes fronteer, final node, time taken 
def sokoban_aStar(heuristic, board, size):
    start_time = time.time()
    Fr = []
    Exp = set()
    n0 = Node(board, 0, 0)
    n0 = StarNode(n0, 0)

    if (sok.can_continue(board, sok.find_boxes(board, size))):
        Fr.append(n0)
    
    while len(Fr) != 0:
        Fr.sort()
        aux = Fr.pop(0)
        aux = aux.getNode()
        if sok.solution(aux.getBoard(), sok.find_boxes(aux.getBoard(), size)):
            end_time = time.time()
            return True, aux.getCost(), len(Exp), len(Fr), aux, (end_time-start_time)
        Exp.add(aux)
        y,x = sok.find_agent(aux.getBoard(), size)
        
        append_fronteer_astar(Fr, Exp, aux, size, x,y, sok.UP, heuristic)
        append_fronteer_astar(Fr, Exp, aux, size, x,y, sok.DOWN, heuristic)
        append_fronteer_astar(Fr, Exp, aux, size, x,y, sok.LEFT, heuristic)
        append_fronteer_astar(Fr, Exp, aux, size, x,y, sok.RIGHT, heuristic)
                        
    end_time = time.time()
    return False, 0, len(Exp), len(Fr), None, (end_time-start_time)

def append_fronteer_astar(fronteer, explored, current_node, size, x, y, direction, heuristic):
    board_aux,movement = sok.move_agent(current_node.getBoard(), x, y, direction)
    if movement and sok.can_continue(board_aux, sok.find_boxes(board_aux, size)):
        node = Node(board_aux, current_node, (current_node.getCost()+1))
        score = heuristic(board_aux, size)
        starNode = StarNode(node, score)
        if node not in explored:
            fronteer.append (starNode)