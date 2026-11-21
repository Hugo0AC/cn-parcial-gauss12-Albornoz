# Conteo de operaciones por paso

## Sin pivoteo

| Paso | Mult/Div | Sum/Res | Total flops | Comparaciones | Intercambios |
|---|---|---|---|---|---|
| 1 | 154 | 143 | 297 | 0 | 0 |
| 2 | 130 | 120 | 250 | 0 | 0 |
| 3 | 108 | 99 | 207 | 0 | 0 |
| 4 | 88 | 80 | 168 | 0 | 0 |
| 5 | 70 | 63 | 133 | 0 | 0 |
| 6 | 54 | 48 | 102 | 0 | 0 |
| 7 | 40 | 35 | 75 | 0 | 0 |
| 8 | 28 | 24 | 52 | 0 | 0 |
| 9 | 18 | 15 | 33 | 0 | 0 |
| 10 | 10 | 8 | 18 | 0 | 0 |
| 11 | 4 | 3 | 7 | 0 | 0 |
| **Total** | **704** | **638** | **1342** | **0** | **0** |

## Pivoteo escalado

| Paso | Mult/Div | Sum/Res | Total flops | Comparaciones | Intercambios |
|---|---|---|---|---|---|
| 1 | 154 | 143 | 297 | 11 | 2 |
| 2 | 130 | 120 | 250 | 10 | 0 |
| 3 | 108 | 99 | 207 | 9 | 2 |
| 4 | 88 | 80 | 168 | 8 | 2 |
| 5 | 70 | 63 | 133 | 7 | 2 |
| 6 | 54 | 48 | 102 | 6 | 2 |
| 7 | 40 | 35 | 75 | 5 | 2 |
| 8 | 28 | 24 | 52 | 4 | 2 |
| 9 | 18 | 15 | 33 | 3 | 0 |
| 10 | 10 | 8 | 18 | 2 | 0 |
| 11 | 4 | 3 | 7 | 1 | 0 |
| **Total** | **704** | **638** | **1342** | **66** | **14** |

## Convención de conteo

- 1 flop = 1 operación aritmética elemental (+, -, *, /).
- Se separan multiplicaciones/divisiones de sumas/restas.
- Cada multiplicador se calcula una sola vez por fila (1 división).
- Solo se cuenta la eliminación hacia adelante (incluye la actualización de b). La sustitución regresiva no se cuenta.
- Comparaciones e intercambios son sobrecosto del pivoteo y no son flops.
- Un intercambio de filas cuenta 2: una fila de A y un elemento de b.

## Pivoteo y mantisa

| Metodo | Multiplicador maximo | Factor de crecimiento | Error relativo final | Bits perdidos |
|---|---|---|---|---|
| Sin pivoteo | 2.753e+13 | 2.641e+03 | 6.773e-23 | 19.4 |
| Pivoteo escalado | 2.466e+09 | 1.783e+00 | 2.881e-25 | 11.5 |

Bits perdidos = log2(error relativo / u), con u = 1e-28 (28 digitos decimales). El error se mide contra una corrida de 60 digitos.

## Condicionamiento

- kappa infinito de A = 5.368e+13
- Cota kappa * u (double, u = 2^-53) = 5.959e-03
- Digitos recuperables segun la cota = 2.2
