# TP4 SIA - Aprendizaje No Supervisado

### Requisitos

- Python3
- pip3
- [pipenv](https://pypi.org/project/pipenv/)

### Instalación

Parado en la carpeta del tp4 ejecutar

```sh
pipenv install
```

para instalar las dependencias necesarias en el ambiente virtual

## Ejecución

```
pipenv run python graphics_[modelo].py [config_file]
```

## Archivo de configuracion
Definimos un archivo de configuración config.ini donde se especifican los parametros:
    Kohonen:
        - k: Dimension de la grilla
        - radius: Radio del vecindario (si esta en 0 se tomara k)
        - eta: Tasa de aprendizaje