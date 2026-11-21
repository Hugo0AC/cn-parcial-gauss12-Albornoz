import csv

def nuevo_estab(matriz):  
    inicial = max(abs(x) for fila in matriz for x in fila)  
    return {"MultMax": 0.0, "MaxInicial": inicial, "MaxElem": inicial}  

def resultados(solucion, nombre = "resultados\\solucion.csv"):
    with open(nombre, "w", newline = "", encoding = "utf-8") as archivo:
        w = csv.writer(archivo)
        w.writerow(["incognita", "valor"])
        for i in range(len(solucion)):
            w.writerow([f"x{i + 1}", solucion[i]])

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

def guardar_residuo(r, norma, nombre="resultados\\residuo.txt"):
    with open(nombre, "w", encoding = "utf-8") as archivo:
        for i in range(len(r)):
            archivo.write(f"r{i + 1} = {r[i]}\n")
        archivo.write(f"Norma infinito = {norma}\n")