# TP2 SIA - Percpeptron Lineal, No Lineal y Multicapa

### Requisitos

- Python3
- pip3
- [pipenv](https://pypi.org/project/pipenv/)

### Instalación

Parado en la carpeta del tp3 ejecutar

```sh
pipenv install
```

para instalar las dependencias necesarias en el ambiente virtual

## Ejecución

```
pipenv run python main.py [config_file]
```

## Archivos de configuracion
Definimos un archivo de configuración config.json dentro de la carpeta ejercicio2 donde se especifican los parametros:
- perceptron_type: Tipo de perceptron
- apprentice_rate: Tasa de aprendizaje 
- epochs: Cantidad de epocas
- epsilon: Minimo error
- beta: Ajuste de la funcion tanh si se utiliza un perceptron no lineal
- training_percentage: Porcentaje de la data con la que se quiere entrenar 

## Archivo de configuracion Multicapa
exercise: ejercicio a, b o c
epochs: cantidad de epocas
apprentice_rate
error_wanted
with_noise: True o False dependiendo si se quiere usar ruido o no
noise_rate

Lo siguiente se aplica a los 3 puntos (a, b o c)
test: Que ejemplo se quiere testear
output_nodes: La cantidad de nodos salida
hidden_layer_nodes: La cantidad de nodos en la capa intermedia
hidden_layers: La cantidad de capas intermedias
beta: El beta para la funcion de tanh

Correr el archivo main del ejercicio 3 con la configuracion deseada. Se imprimiran los resultados de la capa de salida.
