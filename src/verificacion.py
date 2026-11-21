import csv
from decimal import Decimal, getcontext

def nuevo_estab(matriz):  
    inicial = max(abs(x) for fila in matriz for x in fila)  
    return {"MultMax": 0.0, "MaxInicial": inicial, "MaxElem": inicial}  

def resultados(solucion, nombre="resultados\\solucion.csv"):
    with open(nombre, "w", newline="", encoding="utf-8") as archivo:
        w = csv.writer(archivo)
        w.writerow(["incognita", "valor"])
        for i in range(len(solucion)):
            w.writerow([f"x{i + 1}", solucion[i]])