import csv
from copy import deepcopy  
from decimal import getcontext  
import numpy as np  

def nuevo_estab(matriz):  
    inicial = max(abs(x) for fila in matriz for x in fila)  
    return {"MultMax": 0.0, "MaxInicial": inicial, "MaxElem": inicial}  

def resultados(soluciones, nombre = "resultados\\solucion.csv"): 
    with open(nombre, "w", newline = "", encoding = "utf-8") as archivo:
        w = csv.writer(archivo)
        w.writerow(["incognita"] + [metodo for metodo, sol in soluciones])  
        for i in range(len(soluciones[0][1])):  
            w.writerow([f"x{i + 1}"] + [sol[i] for metodo, sol in soluciones])  

def residuo(matriz, vector, solucion):
    tam = len(matriz)
    r = []
    for i in range(tam):
        suma = 0
        for j in range(tam):
            suma +=matriz[i][j] * solucion[j]
        r.append(vector[i] - suma)
    return r

def norma_infinito(r):
    mayor = 0
    for valor in r:
        if abs(valor) > mayor:
            mayor = abs(valor)
    return mayor

def residuo_ext(matriz, vector, x): 
    getcontext().prec = 60
    r = residuo(matriz, vector, x)
    getcontext().prec = 28
    return r

def guardar_residuo(corridas, nombre="resultados\\residuo.txt"):
    with open(nombre, "w", encoding = "utf-8") as archivo:
        for metodo, r, norma, r_ref, norma_ref in corridas:  
            archivo.write(f"===== {metodo} =====\n")
            archivo.write("Residuo sin refinar\n")
            for i in range(len(r)):
                archivo.write(f"r{i + 1} = {r[i]}\n")
            archivo.write(f"Norma infinito = {norma}\n\n")
            archivo.write("Residuo refinado (una pasada)\n")  
            for i in range(len(r_ref)):
                archivo.write(f"r{i + 1} = {r_ref[i]}\n")
            archivo.write(f"Norma infinito = {norma_ref}\n\n")  

def refinar(matriz, vector, solucion, metodo):  
    tam = len(matriz)
    x = solucion[:]
    getcontext().prec = 60  #precision para calcular r
    r = residuo(matriz, vector, x)
    norma_antes = norma_infinito(r)
    getcontext().prec = 28  #precision normal
    d, pasos, estab, traza = metodo(deepcopy(matriz), deepcopy(r))  #resuelve A*d = r
    for i in range(tam):
        x[i] = x[i] + d[i]
    getcontext().prec = 60
    r_ref = residuo(matriz, vector, x)
    norma_despues = norma_infinito(r_ref)
    getcontext().prec = 28
    return x, r_ref, [norma_antes, norma_despues]


def digitos_iguales(valor, referencia):  
    a = format(abs(valor), "f").replace(".", "").lstrip("0")
    b = format(abs(referencia), "f").replace(".", "").lstrip("0")
    cuenta = 0
    for x, y in zip(a, b):
        if x != y:
            break
        cuenta += 1
    return cuenta

def resultados(corridas, nombre = "resultados\\solucion.csv"):  
    with open(nombre, "w", newline = "", encoding = "utf-8") as archivo:
        w = csv.writer(archivo)
        fila = ["incognita"]
        for metodo, sol, sol_ref, referencia in corridas:
            fila += [f"{metodo} sin refinar", "digitos correctos", f"{metodo} refinada", "digitos correctos refinada"]
        w.writerow(fila)
        for i in range(len(corridas[0][1])):
            fila = [f"x{i + 1}"]
            for metodo, sol, sol_ref, referencia in corridas:
                fila += [sol[i], digitos_iguales(sol[i], referencia[i]),
                         sol_ref[i], digitos_iguales(sol_ref[i], referencia[i])]
            w.writerow(fila)

def control_biblioteca(matriz, vector, soluciones, nombre = "resultados\\residuo.txt"): 
    A = np.array([[float(v) for v in fila] for fila in matriz])
    b = np.array([float(v) for v in vector])
    x_np = np.linalg.solve(A, b)
    with open(nombre, "a", encoding = "utf-8") as archivo:  
        archivo.write("===== Control con biblioteca (numpy.linalg.solve) =====\n")
        for metodo, sol in soluciones:
            mayor = 0
            for i in range(len(sol)):
                dif = abs(float(sol[i]) - x_np[i])
                if dif > mayor:
                    mayor = dif
            archivo.write(f"{metodo}: diferencia maxima con numpy = {mayor}\n")