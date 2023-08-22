# 0 espacio
# 1 pared
# 2 caja
# 3 destino
# 4 agente
from src.algorithms.bfs import sokoban_bfs
from src.algorithms.dfs import sokoban_dfs
from src.algorithms.greedy import sokoban_greedy
from src.algorithms.aStar import sokoban_aStar
from src.heuristics.heuristic1 import heuristic_1
from src.heuristics.heuristic2 import heuristic_2
from src.board import board, SIZE

if __name__ == "__main__":

    board_try = board
    size = SIZE
    
    heuristics = [heuristic_1,heuristic_2]
  
    ALGORYTHM = int(input("\nSeleccione que algoritmo quieres que te lo resuelva\n\t1. A*.\n\t2. BFS.\n\t3. DFS.\n\t4. Greedy.\nAlgoritmo: "))
    while ALGORYTHM != 1 and ALGORYTHM != 2 and ALGORYTHM != 3 and ALGORYTHM != 4:
        ALGORYTHM = int(input("El numero ingresado es incorrecto, por favor ingrese un numero del 1 al 4: "))

    HEURISTIC = 0
    if(ALGORYTHM == 1 or ALGORYTHM == 4):
        HEURISTIC = int(input("\nSeleccione que heuristica quieres utilizar\n\t1. Calcular la distancia de manhatan entre un agente y la caja mas cercana.\n\t2. Evaluar cuantas cajas estan conectadas directamente a las metas por caminos despejados, es decir caminos \"rectos\".\nHeuristica: "))
        while HEURISTIC != 1 and HEURISTIC != 2 :
            HEURISTIC = int(input("El numero ingresado es incorrecto, por favor ingrese un numero del 1 al 2: "))

    
    if ALGORYTHM == 1:
        finished, cost, expanded, fronteer, solution, time_taken = sokoban_bfs(board_try, size)
    elif ALGORYTHM == 2:
        finished, cost, expanded, fronteer, solution, time_taken = sokoban_dfs(board_try, size)
    elif ALGORYTHM == 3: 
        finished, cost, expanded, fronteer, solution, time_taken = sokoban_greedy(heuristics[HEURISTIC - 1], board_try, size)
    elif ALGORYTHM == 4:
        finished, cost, expanded, fronteer, solution, time_taken = sokoban_aStar(heuristics[HEURISTIC - 1], board_try, size)
        
    print("\n-------------------\n")
    print("Termino el juego: ",finished, "\nCosto del algoritmo: ",cost,"\nNodos expandidos: ",expanded, "\nNodos Frontera: ", fronteer, "\nTiempo Requerido: ", time_taken)
    


