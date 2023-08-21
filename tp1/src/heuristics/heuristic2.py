# Heuristica 2: Evaluar cuantas cajas estan conectadas directamente a las metas por caminos despejados, 
# es decir caminos "rectos". Cuantas mas cajas esten cerca de sus metas, mas cerca se estara de la solucion.
# Es admisible pues para llegar a la solucion las cajas siempre van a tener que estar en linea recta con la ubicacion final, 
# por lo tanto cumple con que h(n) <= costo de la solucion.

import src.sokoban as sok 

def heuristic_2(board, size):
    boxes = sok.find_boxes(board, size)
    destinies = sok.find_destinies(board, size)
    walls = sok.find_walls(board, size)
    boxes_in_line = 0
    wall_present = False
    for box in boxes:
        for destiny in destinies:
            wall_present = False
            if (box[0] == destiny[0]):
                if (len(walls) != 0):
                    for wall in walls:
                        if(box[0] == wall[0] and ((wall[1] < destiny[1] and wall[1] > box[1]) or (wall[1] > destiny[1] and wall[1] < box[1]))):
                            wall_present = True 
                            break 
                if wall_present == False:
                    boxes_in_line+=1
                    break                          
            elif (box[1] == destiny[1]):
                if (len(walls) != 0):
                    for wall in walls:
                        if(box[1] == wall[1] and ((wall[0] < destiny[0] and wall[0] > box[0]) or (wall[0] > destiny[0] and wall[0] < box[0]))):
                             wall_present = True
                             break
                if wall_present == False:
                    boxes_in_line+=1
                    break
            
    return boxes_in_line
            
                