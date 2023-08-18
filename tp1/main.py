# 0 espacio
# 1 pared
# 2 caja
# 3 destino
# 4 agente
import numpy as np
from src.sokoban import move_agent, find_agent
import src.sokoban as sok
from src.algorithms.bfs import sokoban_bfs
from src.algorithms.dfs import sokoban_dfs
from src.node import Node
import time

SIZE = 6

board = np.array([
    [1, 1, 1, 1, 1, 1],
    [1, 0, 3, 0, 0, 1],
    [1, 0, 0, 2, 3, 1],
    [1, 0, 2, 0, 0, 1],
    [1, 0, 4, 0, 0, 1],
    [1, 1, 1, 1, 1, 1]
])

board2 = np.array([
    [1, 1, 1, 1, 1, 1],
    [1, 0, 3, 0, 0, 1],
    [1, 0, 1, 0, 0, 1],
    [1, 0, 2, 0, 0, 1],
    [1, 0, 4, 0, 0, 1],
    [1, 1, 1, 1, 1, 1]
])

if __name__ == "__main__":

    start_time = time.time()
    result = sokoban_dfs(board, SIZE)
    end_time = time.time()
    while result != 0:
        print(result.board)
        result = result.parent
        print("---------------------------------------")
    print("Finished: ",(end_time-start_time))

