import src.sokoban as sok 

def heuristic_3(board, size):
    dist = len(board)
    agent = sok.find_agent(board, size)
    for box in sok.find_boxes(board, size):
        aux = abs(box[0] - agent[0]) + abs(box[1] - agent[1])
        if aux < dist:
            dist = aux
    
    return dist