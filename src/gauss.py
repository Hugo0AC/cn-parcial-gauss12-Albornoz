from conteo import conteo_operaciones
from verificacion import nuevo_estab
from copy import deepcopy


def sustitucion_atras(matriz, vector):
    tam = len(matriz)
    sol = [0] * tam 

    for i in range(tam - 1, -1, -1):
        suma = 0
        for j in range(i + 1, tam):
            suma += matriz[i][j] * sol[j]
        sol[i] = (vector[i] - suma) / matriz[i][i] 

    return sol


def eliminacion_adelante(matriz, vector, columna, conteo, estab): 
    tam = len(matriz)
    pivote = matriz[columna][columna]
    for j in range(columna + 1, tam):
        objetivo = matriz[j][columna]
        multiplicador = objetivo / pivote #Division +1
        conteo["MulDiv"] += 1
        estab["MultMax"] = max(estab["MultMax"], abs(multiplicador))  
        for k in range(columna, tam):
            matriz[j][k] -= multiplicador * matriz[columna][k] #Multiplicacion +1, Resta +1
            conteo["MulDiv"] += 1
            conteo["SumRes"] += 1
            if k > columna:  
                estab["MaxElem"] = max(estab["MaxElem"], abs(matriz[j][k]))  
        vector[j] -= multiplicador * vector[columna] #Multiplicacion +1, Resta +1
        conteo["MulDiv"] += 1
        conteo["SumRes"] += 1


def pivoteo_simple(matriz, vector, i, conteo):
    tam = len(matriz)
    fila_max = i
    for j in range(i + 1, tam):
        conteo["Comparacion"] += 1
        if abs(matriz[j][i]) > abs(matriz[fila_max][i]): #Comparacion +1
            fila_max = j

    if fila_max != i: 
        matriz[i], matriz[fila_max] = matriz[fila_max], matriz[i] #Intercambio +1
        vector[i], vector[fila_max] = vector[fila_max], vector[i] #Intercambio +1
        conteo["Intercambio"] += 2


def pivoteo_escalado(matriz, vector, i, conteo):
    tam = len(matriz)
    fila_max = i
    razon_max = 0
    for j in range(i, tam):
        lista = [abs(x) for x in matriz[j][i:]] 
        escalado = max(lista) 
        razon = abs(matriz[j][i]) / escalado 
        if j > i:
            conteo["Comparacion"] += 1
        if razon > razon_max: #Comparacion +1
            razon_max = razon
            fila_max = j
    if fila_max != i:
        matriz[i], matriz[fila_max] = matriz[fila_max], matriz[i] #Intercambio +1
        vector[i], vector[fila_max] = vector[fila_max], vector[i] #Intercambio +1
        conteo["Intercambio"] += 2


def gaussiana_simple(matriz, vector):
    tam = len(matriz)
    pasos = []
    estab = nuevo_estab(matriz)  
    traza = []
    for i in range(tam - 1):
        conteo_pasos = conteo_operaciones()
        eliminacion_adelante(matriz, vector, i, conteo_pasos, estab)  
        pasos.append(conteo_pasos)
        traza.append((deepcopy(matriz), deepcopy(vector)))

    solucion = sustitucion_atras(matriz, vector)
    return solucion, pasos, estab, traza


def gaussiana_pivoteo_simple(matriz, vector):
    tam = len(matriz)
    pasos = []
    estab = nuevo_estab(matriz) 
    traza = []
    for i in range(tam - 1):
        conteo_pasos = conteo_operaciones()
        pivoteo_simple(matriz, vector, i, conteo_pasos)
        eliminacion_adelante(matriz, vector, i, conteo_pasos, estab)  
        pasos.append(conteo_pasos)
        traza.append((deepcopy(matriz), deepcopy(vector)))
    
    solucion = sustitucion_atras(matriz, vector)
    return solucion, pasos, estab, traza


def gaussiana_pivoteo_escalado(matriz, vector):
    tam = len(matriz)
    pasos = []
    estab = nuevo_estab(matriz)  
    traza = []
    for i in range(tam - 1):
        conteo_pasos = conteo_operaciones()
        pivoteo_escalado(matriz, vector, i, conteo_pasos)
        eliminacion_adelante(matriz, vector, i, conteo_pasos, estab)  
        pasos.append(conteo_pasos)
        traza.append((deepcopy(matriz), deepcopy(vector)))
    solucion = sustitucion_atras(matriz, vector)
    return solucion, pasos, estab, traza