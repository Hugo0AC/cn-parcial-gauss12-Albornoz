def nuevo_estab(matriz):  
    inicial = max(abs(x) for fila in matriz for x in fila)  
    return {"MultMax": 0.0, "MaxInicial": inicial, "MaxElem": inicial}  