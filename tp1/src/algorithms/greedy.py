import src.heuristics.heuristic1 as h1 
import src.heuristics.heuristic2 as h2
from src.node import Node, GreedyNode
import src.sokoban as sok

def sokoban_greedy(heuristic, board, size):
    Fr = []
    Exp = set()
    n0 = Node(board, 0, 0)
    n0 = GreedyNode(n0, 0)

    if (sok.can_continue(board, sok.find_boxes(board, size))):
        Fr.append(n0)
    
    while len(Fr) != 0:
        Fr.sort()
        aux = Fr.pop(0)
        aux = aux.getNode()
        if sok.solution(aux.getBoard(), sok.find_boxes(aux.getBoard(), size)):
            return aux
        Exp.add(aux)
        y,x = sok.find_agent(aux.getBoard(), size)
        
        append_fronteer_bfs(Fr, Exp, aux, size, x,y, sok.UP, heuristic)
        append_fronteer_bfs(Fr, Exp, aux, size, x,y, sok.DOWN, heuristic)
        append_fronteer_bfs(Fr, Exp, aux, size, x,y, sok.LEFT, heuristic)
        append_fronteer_bfs(Fr, Exp, aux, size, x,y, sok.RIGHT, heuristic)
                        
    return 0    


def append_fronteer_bfs(fronteer, explored, current_node, size, x, y, direction, heuristic):
    board_aux,movement = sok.move_agent(current_node.getBoard(), x, y, direction)
    if movement and sok.can_continue(board_aux, sok.find_boxes(board_aux, size)):
        node = Node(board_aux, current_node, (current_node.getCost()+1))
        score = heuristic(board_aux, size)
        greedyNode = GreedyNode(node, score)
        if node not in explored:
            fronteer.append (greedyNode)
