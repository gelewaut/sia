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
from src.algorithms.greedy import sokoban_greedy
from src.algorithms.aStar import sokoban_aStar
from src.node import Node
import time
from src.heuristics.heuristic1 import find_closest_box_bfs
from src.heuristics.heuristic2 import heuristic_2

SIZE = 6

SIZE_SOKO1 = 15
soko1 = np.array([
    [0,0,0,0,0,0,1,1,1,0,0,0,0,0,0],
    [0,0,0,0,0,0,1,3,1,0,0,0,0,0,0],
    [0,0,1,1,1,1,1,3,1,1,1,1,1,0,0],
    [0,1,1,0,0,0,0,0,0,0,0,0,1,1,0],
    [1,1,0,0,1,0,1,0,1,0,1,0,0,1,1],
    [1,0,0,1,1,0,0,0,0,0,1,1,0,0,1],
    [1,0,1,1,0,0,1,0,1,0,0,1,1,0,1],
    [1,0,0,0,0,0,2,4,2,0,0,0,0,0,1],
    [1,1,1,1,0,0,1,1,1,0,0,1,1,1,1],
    [0,0,0,1,1,1,1,0,1,1,1,1,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
])

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


    # start_time = time.time()
    # result_heuristic = find_closest_box_bfs(board, SIZE)
    # print(result_heuristic)
    # result = sokoban_greedy(find_closest_box_bfs, board, SIZE)
    # result = sokoban_aStar(find_closest_box_bfs, board, SIZE)
    # end_time = time.time()
    # while result != 0:
    #     print(result.board)
    #     result = result.parent
    #     print("---------------------------------------")
    # print("Finished: ",(end_time-start_time))

    board_try = soko1
    size = SIZE_SOKO1

    finished, cost, expanded, fronteer, solution, time_taken = sokoban_bfs(board_try, size)
    print(finished, cost, expanded, fronteer, time_taken)
    # finished, cost, expanded, fronteer, solution, time_taken = sokoban_dfs(board_try, size)
    # print(finished, cost, expanded, fronteer, time_taken)
    # finished, cost, expanded, fronteer, solution, time_taken = sokoban_greedy(find_closest_box_bfs, board_try, size)
    # print(finished, cost, expanded, fronteer, time_taken)
    # finished, cost, expanded, fronteer, solution, time_taken = sokoban_greedy(heuristic_2, board_try, size)
    # print(finished, cost, expanded, fronteer, time_taken)
    # finished, cost, expanded, fronteer, solution, time_taken = sokoban_aStar(find_closest_box_bfs, board_try, size)
    # print(finished, cost, expanded, fronteer, time_taken)
    # finished, cost, expanded, fronteer, solution, time_taken = sokoban_aStar(heuristic_2, board_try, size)
    # print(finished, cost, expanded, fronteer, time_taken)


