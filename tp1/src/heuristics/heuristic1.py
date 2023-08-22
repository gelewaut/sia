# Heuristica 1: Calcular la distancia de manhatan entre un agente y la caja mas cercana.
# Es admisible pues como minimo el agente tendra que recorrer la distancia a la caja
# mas cercana, por lo tanto h(n) <= costo de la solucion siempre

from src.node import Node
import src.sokoban as sok 

def heuristic_1(board, size):
    dist = len(board)
    agent = sok.find_agent(board, size)
    for box in sok.find_boxes(board, size):
        aux = abs(box[0] - agent[0]) + abs(box[1] - agent[1])
        if aux < dist:
            dist = aux
    
    return dist
