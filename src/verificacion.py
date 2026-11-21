import csv
from copy import deepcopy  
from decimal import getcontext  

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