# TP2 SIA - Algoritmos Genericos

### Requisitos

- Python3
- pip3
- [pipenv](https://pypi.org/project/pipenv/)

### Instalación

Parado en la carpeta del tp2 ejecutar

```sh
pipenv install
```

para instalar las dependencias necesarias en el ambiente virtual

## Ejecución

```
pipenv run python main.py [config_file]
```

## Archivos de configuracion
Definimos un archivo de configuración model.json donde se especifican los hiperparametros:
- Clase de personaje
- N, K, A, B 
- Probabilidad de mutación
- Método de mutación
- Dos métodos de selección
- Método de cruza
- Condición de corte (Para el caso de corte por estructura se tiene que utilizar el archivo structure_model.json)
- Metadata (Para el algoritmo de Boltzmann si se quiere utilizar)


