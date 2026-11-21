import csv
from decimal import Decimal, getcontext

from gauss import gaussiana_simple, gaussiana_pivoteo_simple, gaussiana_pivoteo_escalado
#Devuelven: solucion, pasos, estabilidad

from verificacion import resultados


def obtener_matriz(ruta_archivo):
    matriz = []
    with open(ruta_archivo, 'r', encoding = "utf-8") as archivo:
        lector = csv.reader(archivo)
        for fila in lector:
            matriz.append([Decimal(x) for x in fila])
    return matriz

def obtener_vector(ruta_archivo):
    vector = []
    with open(ruta_archivo, 'r', encoding = "utf-8") as archivo:
        lector = csv.reader(archivo)
        for fila in lector:
            vector.append(Decimal(fila[0]))
    return vector


if __name__ == "__main__":
    ruta_matriz = "datos\\matriz_a.csv"
    ruta_vector = "datos\\vector_b.csv"
    matriz = obtener_matriz(ruta_matriz)
    vector = obtener_vector(ruta_vector)

    solucion, pasos, estab = gaussiana_simple(matriz, vector)

    resultados(solucion)