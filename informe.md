# Informe eliminacion gaussiana

## Identificacion

- **Nombre:** Hugo Albornoz Contreras
- **Asignatura:** Computacion numerica
- **Fecha:** 21-11-2026
- **Enlace:** https://github.com/Hugo0AC/cn-parcial-gauss12-Albornoz

## Planteamiento

Se resuelve el sistema lineal denso **A x = b** con n = 12 incógnitas (A en `datos/matriz_a.csv`, b en `datos/vector_b.csv`).

**Escalas de fila.** El elemento más grande (en valor absoluto) de cada fila varía entre ≈ 1e-5 y ≈ 1e6:

| Filas | Elemento máximo de la fila |
|---|---|
| 1, 5, 9 | ≈ 1e-4 |
| 3, 7, 11 | ≈ 1e-2 |
| 4, 10 | ≈ 1e4 |
| 2, 8, 12 | ≈ 1e5 |
| 6 | ≈ 1e6 (966870.732, el máximo de A) |

Entre la fila más pequeña y la más grande hay una razón de ≈ 1e10.

**Qué lo hace costoso de resolver:**

1. **Pivote inicial diminuto.** a(1,1) = 1.3407e-8, mientras que su columna llega a 9.7e5. Sin pivoteo, el primer multiplicador llega a ≈ 2.75e13 y amplifica el error de redondeo.
2. **Mal escalamiento.** Las filas de magnitudes tan distintas hacen que el pivoteo simple (que solo compara la columna) elija mal. Por eso se prueba también el pivoteo escalado.
3. **Mal condicionamiento.** κ∞(A) ≈ 5.4e13, así que una perturbación pequeña en los datos se puede amplificar mucho en la solución.
4. **Matriz densa.** No hay ceros que aprovechar, y el costo de la eliminación no baja de ≈ 2n³/3 flops.

## Estrategias de eliminacion

Se usa eliminación gaussiana por columnas, en 11 pasos (k = 1..11). Se ejecuta con dos métodos: **sin pivoteo** y **con pivoteo parcial escalado**.

**Orden de los pasos.** En cada paso k:

1. (Solo en el pivoteo escalado) se elige como pivote la fila con mayor razón |a(i,k)| / (máximo de su fila) y se intercambia con la fila k.
2. Para cada fila i > k se calcula el multiplicador m(i,k) = a(i,k) / a(k,k).
3. Se resta m(i,k) veces la fila k a la fila i, desde la columna k en adelante, y se actualiza b.

Al terminar los 11 pasos, A queda triangular superior y la solución se obtiene por sustitución regresiva.

**Reutilización de multiplicadores.** Cada multiplicador se calcula **una sola vez** por fila (1 división) y se usa en toda la fila y en b. No se recalcula por columna, que es el caso penalizado (≈ 1750 flops).

**Por qué no excede el mínimo teórico.**

- El barrido del paso k parte de la columna k, sin tocar la parte ya anulada.
- No se calcula la inversa ni se hace más de una factorización.
- El pivoteo solo agrega comparaciones e intercambios, no flops.
- El total es 1342 flops. El mínimo teórico ≈ 2n³/3 = 1152, más la actualización de b. La diferencia viene de operar también la columna pivote (2 flops por cada una de las 66 filas, 132 en total). Sin ellos serían 1210.

## 5. Análisis de mantisa y pivoteo

| Método | Multiplicador máximo | Factor de crecimiento | Error relativo final | Bits perdidos |
|---|---:|---:|---:|---:|
| Sin pivoteo | 2.753e13 | 2.641e3 | 6.773e-23 | 19.4 |
| Pivoteo escalado | 2.466e9 | 1.783 | 2.881e-25 | 11.5 |

Bits perdidos = log₂(error relativo / u), con u = 1e-28 (28 dígitos decimales ≈ 93 bits de mantisa).

El pivote a(1,1) = 1.3407e-8 es inaceptable porque su columna llega a 9.7e5, lo que da multiplicadores de hasta 2.75e13 ≈ 2^44.6, de modo que el error de redondeo se amplifica y en una mantisa de 53 bits quedarían unos 8 bits fiables; el pivoteo escalado reduce el error unas 235 veces (8 bits menos perdidos).

## Resultados

Se reporta la solución refinada del pivoteo escalado. Los dígitos afirmados (28) son el tope de la precisión de trabajo y coinciden con la referencia de 60 dígitos. La tabla completa con ambos métodos está en `resultados/solucion.csv`.

| Incógnita | Valor reportado (refinado) | Dígitos afirmados | Valor sin refinar (pivoteo escalado) | Dígitos correctos |
|---|---|---:|---|---:|
| x1 | 0.7384915627000000000000000000 | 28 | 0.7384915627000000000000000627 | 25 |
| x2 | -1.205937416800000000000000000 | 28 | -1.205937416800000000000000820 | 25 |
| x3 | 0.004387195200000000000000000000 | 28 | 0.004387195199999999999999557068 | 7 |
| x4 | -0.09172645380000000000000000000 | 28 | -0.09172645379999999999999971413 | 8 |
| x5 | 2.846109372500000000000000000 | 28 | 2.846109372500000000000000422 | 25 |
| x6 | -0.006281540900000000000000000000 | 28 | -0.006281540900000000000000658174 | 22 |
| x7 | 1.473820591600000000000000000 | 28 | 1.473820591599999999999999436 | 10 |
| x8 | -0.03849271640000000000000000000 | 28 | -0.03849271640000000000000007110 | 24 |
| x9 | 0.9152648037000000000000000000 | 28 | 0.9152648037000000000000002108 | 24 |
| x10 | -2.607139485200000000000000000 | 28 | -2.607139485199999999999999556 | 10 |
| x11 | 0.05187362940000000000000000000 | 28 | 0.05187362940000000000000007938 | 24 |
| x12 | -1.084937162500000000000000000 | 28 | -1.084937162499999999999999583 | 10 |

