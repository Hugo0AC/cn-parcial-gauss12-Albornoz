# Eliminacion gaussiana 12x12

En el proyecto se resuelve un sistema lineal denso de 12 ecuaciones con eliminacion gaussiana (con y sin pivote).

## Autoria y Asignatura

- **Autor:** Hugo Benjamin Albornoz Contreras
- **Asignatura:** Computacion numerica

## Requisitos

- Instalar dependencias: [requirements.txt](requirements.txt)
Para cargar el repositorio de forma correcta se deben seguir los siguientes pasos:

1. Clonar el repositorio en la carpeta deseada:
   `git clone https://github.com/Hugo0AC/cn-parcial-gauss12-Albornoz.git`

2. Entrar en la carpeta del proyecto:
   `cd cn-parcial-gauss12-Albornoz`

3. Verificar si Python está instalado:
   `python --version` o `py --version`

4. Crear el entorno virtual:
   `python -m venv .venv`

5. Activar el entorno virtual:
   `.\.venv\Scripts\Activate.ps1`
   1. En caso de haber fallado el comando anterior por restricciones de ejecución, primero escribir:
      `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`
      Luego volver a activar el entorno.

6. Instalar dependencias:
   `python -m pip install -r requirements.txt`

7. Ejecutar el programa:
   `python .\src\main.py

## Estructura de carpetas

``` bash

├── datos/                  # entrada: matriz_a.csv (matriz A) y vector_b.csv(vector b)
├── resultados/             # salida: solucion.csv, residuo.txt, traza_eliminacion.txt, conteo_flops.md
├── src/                    # código: main.py, gauss.py, verificacion.py, conteo.py
├── .gitignore
├── informe.md
├── README.md
└── requirements.txt
```

## Resultado resumido

| Incógnita | Valor (10 dígitos) |
|---|---|
| x1 | 0.7384915627 |
| x2 | -1.205937417 |
| x3 | 0.004387195200 |
| x4 | -0.09172645380 |
| x5 | 2.846109373 |
| x6 | -0.006281540900 |
| x7 | 1.473820592 |
| x8 | -0.03849271640 |
| x9 | 0.9152648037 |
| x10 | -2.607139485 |
| x11 | 0.05187362940 |
| x12 | -1.084937162 |

| Métrica | Valor |
|---|---|
| Total de flops (eliminación hacia adelante) | 1342 |
| Norma infinito del residuo | 2.415895679122262966931495766936E-22 |

## Informe

El análisis completo está en [informe.md](informe.md).


## Declaracion IA

Se declara uso de IA para corregir errores y generado de archivos.
