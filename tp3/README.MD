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


