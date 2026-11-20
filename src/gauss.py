def eliminacion_adelante(matriz, vector):
    tam = len(matriz)

    for i in range(tam - 1):
        pivote = matriz[i][i]
        for j in range(i + 1, tam):
            objetivo = matriz[j][i]
            multiplicador = objetivo / pivote
            for k in range(i, tam):
                matriz[j][k] -= multiplicador * matriz[i][k]
            vector[j] -= multiplicador * vector[i]

def sustitucion_atras(matriz, vector):
    tam = len(matriz)
    sol = [0] * tam

    for i in range(tam - 1, -1, -1):
        suma = 0
        for j in range(i + 1, tam):
            suma += matriz[i][j] * sol[j]
        sol[i] = (vector[i] - suma) / matriz[i][i]

    return sol

def eliminacion_columna(matriz, vector, columna): #Eliminacion hacia adelante
    tam = len(matriz)
    pivote = matriz[columna][columna]

    for j in range(columna + 1, tam):
        objetivo = matriz[j][columna]
        multiplicador = objetivo / pivote
        for k in range(columna, tam):
            matriz[j][k] -= multiplicador * matriz[columna][k]
        vector[j] -= multiplicador * vector[columna]

def pivoteo_simple(matriz, vector, i):
    tam = len(matriz)
    fila_max = i
    for j in range(i + 1, tam):
        if abs(matriz[j][i]) > abs(matriz[fila_max][i]):
            fila_max = j
    if fila_max != i:
        matriz[i], matriz[fila_max] = matriz[fila_max], matriz[i]
        vector[i], vector[fila_max] = vector[fila_max], vector[i]


def pivoteo_escalado(matriz, vector, i):
    tam = len(matriz)
    fila_max = i
    razon_max = 0
    for j in range(i, tam):
        escalado = max(abs(x) for x in matriz[j][i:])
        razon = abs(matriz[j][i]) / escalado
        if razon > razon_max:
            razon_max = razon
            fila_max = j
    if fila_max != i:
        matriz[i], matriz[fila_max] = matriz[fila_max], matriz[i]
        vector[i], vector[fila_max] = vector[fila_max], vector[i]

def gaussiana_simple(matriz, vector):
    eliminacion_adelante(matriz, vector)
    solucion = sustitucion_atras(matriz, vector)
    return solucion

def gaussiana_pivoteo_simple(matriz, vector):
    tam = len(matriz)
    for i in range(tam - 1):
        pivoteo_simple(matriz, vector, i)
        eliminacion_columna(matriz, vector, i)
    solucion = sustitucion_atras(matriz, vector)
    return solucion

def gaussiana_pivoteo_escalado(matriz, vector):
    tam = len(matriz)
    for i in range(tam - 1):
        pivoteo_escalado(matriz, vector, i)
        eliminacion_columna(matriz, vector, i)
    solucion = sustitucion_atras(matriz, vector)
    return solucion

def mostrar_matriz(matriz, vector, solucion):
    for i in range(len(matriz)):
        print(matriz[i], " - ", vector[i])
    print("Solucion:", solucion)


if __name__ == "__main__":
    a = [
        [4,  2, -1,  1],
        [2,  5,  1, -2],
        [1, -1,  6,  2],
        [3,  1,  2,  7]
    ]

    b = [12, 3, 31, 36]

    solucion = gaussiana_simple(a, b)
    mostrar_matriz(a, b, solucion)
