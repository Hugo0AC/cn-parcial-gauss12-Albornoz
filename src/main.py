import csv
from copy import deepcopy  #CAMBIO
from decimal import Decimal, getcontext

from gauss import gaussiana_simple, gaussiana_pivoteo_simple, gaussiana_pivoteo_escalado
#Devuelven: solucion, pasos, estabilidad, traza

from verificacion import resultados, residuo, norma_infinito, guardar_residuo
from conteo import guardar_conteo


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

def formato(numero):
    if abs(numero) < Decimal("1E-20"):   
        return "0"
    return f"{numero:.10e}"


def guardar_traza(corridas, nombre = "resultados\\traza_eliminacion.txt"):  
    with open(nombre, "w", encoding = "utf-8") as archivo:
        for metodo, trazas in corridas:  
            archivo.write(f"===== {metodo} =====\n\n")  
            for k in range(len(trazas)):
                matriz, vector = trazas[k]
                archivo.write(f"Paso {k + 1}\n")
                for i in range(len(matriz)):
                    fila = "  ".join(formato(x) for x in matriz[i])
                    archivo.write(f"{fila}  |  {formato(vector[i])}\n")
                archivo.write("\n")


if __name__ == "__main__":
    ruta_matriz = "datos\\matriz_a.csv"
    ruta_vector = "datos\\vector_b.csv"
    matriz = obtener_matriz(ruta_matriz)
    vector = obtener_vector(ruta_vector)

    metodos = [("Sin pivoteo", gaussiana_simple),  
            ("Pivoteo escalado", gaussiana_pivoteo_escalado)]  

    soluciones = []  
    residuos = []  
    conteos = []  
    trazas = []  

    for nombre, metodo in metodos:  
        solucion, pasos, estab, traza = metodo(deepcopy(matriz), deepcopy(vector)) 

        getcontext().prec = 60 #precision para calular r
        r = residuo(matriz, vector, solucion) 
        norma = norma_infinito(r)
        getcontext().prec = 28  #prfecision normal

        soluciones.append((nombre, solucion))  
        residuos.append((nombre, r, norma))  
        conteos.append((nombre, pasos))  
        trazas.append((nombre, traza))  

    resultados(soluciones)  
    guardar_residuo(residuos)  
    guardar_traza(trazas)  
    guardar_conteo(conteos)  