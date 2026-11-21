# Conteo de operaciones por paso

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
