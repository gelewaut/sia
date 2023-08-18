from src.node import Node
import src.sokoban as sok 


def sokoban_dfs(board, size):
    Fr = []
    Exp = set()
    n0 = Node(board, 0, 0)
    if (sok.can_continue(board, sok.find_boxes(board, size))):
        Fr.append(n0)

    while len(Fr) != 0:
        aux = Fr.pop()
        if sok.solution(aux.getBoard(), sok.find_boxes(aux.getBoard(), size)):
            return aux
        Exp.add(aux)
        y,x = sok.find_agent(aux.getBoard(), size)

        append_fronteer_dfs(Fr, Exp, aux, size, x,y, sok.UP)
        append_fronteer_dfs(Fr, Exp, aux, size, x,y, sok.DOWN)
        append_fronteer_dfs(Fr, Exp, aux, size, x,y, sok.LEFT)
        append_fronteer_dfs(Fr, Exp, aux, size, x,y, sok.RIGHT)

    return 0


def append_fronteer_dfs( fronteer, explored,current_node,size,x,y,direction):
    board_aux,movement = sok.move_agent(current_node.getBoard(), x, y, direction)
    if movement and sok.can_continue(board_aux, sok.find_boxes(board_aux, size)):
        node = Node(board_aux, current_node, 0)
        if node not in explored:
            fronteer.append (node)
