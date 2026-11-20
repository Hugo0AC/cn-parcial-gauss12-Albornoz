from conteo import conteo_operaciones
from verificacion import nuevo_estab


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
    for i in range(tam - 1):
        conteo_pasos = conteo_operaciones()
        eliminacion_adelante(matriz, vector, i, conteo_pasos, estab)  
        pasos.append(conteo_pasos)

    solucion = sustitucion_atras(matriz, vector)
    return solucion, pasos, estab  


def gaussiana_pivoteo_simple(matriz, vector):
    tam = len(matriz)
    pasos = []
    estab = nuevo_estab(matriz) 
    for i in range(tam - 1):
        conteo_pasos = conteo_operaciones()
        pivoteo_simple(matriz, vector, i, conteo_pasos)
        eliminacion_adelante(matriz, vector, i, conteo_pasos, estab)  
        pasos.append(conteo_pasos)
    
    solucion = sustitucion_atras(matriz, vector)
    return solucion, pasos, estab  


def gaussiana_pivoteo_escalado(matriz, vector):
    tam = len(matriz)
    pasos = []
    estab = nuevo_estab(matriz)  
    for i in range(tam - 1):
        conteo_pasos = conteo_operaciones()
        pivoteo_escalado(matriz, vector, i, conteo_pasos)
        eliminacion_adelante(matriz, vector, i, conteo_pasos, estab)  
        pasos.append(conteo_pasos)
    solucion = sustitucion_atras(matriz, vector)
    return solucion, pasos, estab  

def mostrar_matriz(matriz, vector, solucion):
    for i in range(len(matriz)):
        print(matriz[i], " - ", vector[i])
    print("Solucion:", solucion)


if __name__ == "__main__":
    a12 = [
    [1.3407e-08, 2.86200125e-05, 7.71282706e-05, 5.20406822e-05, 2.69019703e-05, 8.97506196e-05, -3.52569526e-05, -7.95799865e-05, 9.2743729e-05, 4.75171707e-05, 5.87919642e-05, 4.70751006e-05],
    [1.19229739e+04, 9.43345765e+04, -2.79137721e+04, 5.34841249e+04, 8.34096835e+04, -3.61503637e+04, 5.06938864e+04, 1.56369357e+04, -4.55735222e+04, 4.11466774e+04, -9.95723312e+04, 4.52774903e+04],
    [2.70519337e-03, 7.56465355e-03, -8.31722416e-03, 1.84523013e-03, 6.59957738e-03, -5.2384333e-03, 2.90601783e-03, 2.15762119e-03, 5.81832697e-03, -5.05505158e-03, 9.63772913e-03, -5.65339628e-03],
    [4.7361833e+03, -2.2903298e+03, 8.38293495e+03, 3.15556386e+03, 1.86600979e+03, 1.65367916e+03, 6.23820612e+03, 6.43167599e+03, 1.07790609e+03, 8.22888029e+03, 3.1319774e+03, 1.91824343e+03],
    [4.11556548e-05, -4.86332608e-05, 3.54781266e-05, -1.40485529e-05, -8.04989572e-05, 4.87876377e-05, -4.93597957e-05, 1.81490131e-05, -7.36225567e-05, 1.04825395e-05, 3.96867268e-05, 5.83825652e-05],
    [3.69040121e+05, -9.66870732e+05, 8.61728264e+05, 7.74107904e+05, -2.51973737e+05, 5.11217156e+05, 5.52310313e+05, 9.46611327e+05, -8.65191957e+05, 4.15566294e+05, 3.63776332e+05, 3.25224762e+05],
    [3.5470172e-02, 3.2286982e-03, -1.4034672e-02, -4.859464e-04, -1.9366706e-02, 6.5085743e-03, -1.66351405e-02, 1.95791832e-02, -1.86199853e-02, -1.49865545e-02, 6.33436994e-02, 1.04578981e-02],
    [-8.29580538e+04, 1.47723211e+04, -6.62071918e+04, 7.77627003e+04, 5.9113749e+04, 6.71198873e+04, 4.73806845e+04, 2.46013295e+04, 5.42256665e+04, 6.80002405e+04, 1.46600694e+04, -7.04748433e+04],
    [4.78478957e-05, 4.74177728e-05, -5.00008216e-05, -8.09019942e-05, 9.96264129e-05, -6.54779356e-05, 5.58845205e-05, 5.68662072e-05, -6.98148836e-05, -4.75603449e-05, 1.91702541e-05, 5.2134748e-05],
    [1.70754409e+03, 1.75596842e+03, -3.3583456e+03, 6.02077474e+03, 4.08173052e+03, 2.52738854e+03, 5.79161749e+03, 8.87299068e+03, -7.69115047e+03, 1.71198725e+03, 6.70947562e+03, 5.50379648e+03],
    [6.62128249e-03, 4.72978435e-03, -4.21527069e-03, 7.27627231e-03, 8.24351754e-03, 6.16631194e-03, 9.74037062e-03, 4.78863744e-03, 6.71974041e-03, 6.16313996e-03, 3.96445541e-03, 3.46940098e-03],
    [-5.00713078e+04, 2.88624018e+04, 3.60557564e+04, 4.63192795e+04, 5.68987677e+04, 2.83052303e+04, 9.84274338e+04, -5.28888608e+04, 5.69419053e+04, 8.48620303e+04, -3.2286649e+04, 6.84397237e+04]
    ]

    b12 = [
    -0.00009885876325151139315,
    -1528.38292550107502,
    0.040823496875248026692,
    -2132.116814065697381,
    -0.00036837163769785421642,
    -780791.4415980108769,
    -0.04417817372835579269,
    99770.53658718820715,
    0.0003540165350861586367,
    1245.79867836156599,
    0.022618212160439973886,
    -12069.33152836593874
    ]

    solucion, conteo, estab = gaussiana_pivoteo_simple(a12, b12)
    mostrar_matriz(a12, b12, solucion)
    print("Conteo de operaciones:")
    for pasos in conteo:
        print(f"  {pasos}:")
    print("Estadsticas:")
    for clave, valor in estab.items():
        print(f"  {clave}: {valor}")