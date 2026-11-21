import csv

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

def guardar_residuo(corridas, nombre="resultados\\residuo.txt"):  
    with open(nombre, "w", encoding = "utf-8") as archivo:
        for metodo, r, norma in corridas:  
            archivo.write(f"===== {metodo} =====\n")  
            for i in range(len(r)):
                archivo.write(f"r{i + 1} = {r[i]}\n")
            archivo.write(f"Norma infinito = {norma}\n\n")  