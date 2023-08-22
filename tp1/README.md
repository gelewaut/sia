# TP1

Para que el proyecto funcione se debe tener instalado python, pip3, pipenv y numpy. 

Configure su tablero en el archivo src.board.py de tal manera que su tablero quede guardado en la variable board y el tamaño del tablero en la variable SIZE.

El tablero debe estar configurado de la siguiente manera: una matriz cuadrada en la que los espacios sean 0, las paredes sean 1, las cajas sean 2, los destinos sean 3 y el agente sea 4.

Para correr el proyecto se debe correr el siguiente comando desde la terminal, estando en la carpeta donde se tiene el proyecto:
pipenv run python main.py

Una vez que se corre este comando se le preguntara al usuario con que algoritmo se quiere resolver el juego, y luego la heuristica que se tiene que aplicar si es necesaria.

Finalmente se imprimira en pantalla los resultados del algoritmo.