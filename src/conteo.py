import math  
import numpy as np  

def conteo_operaciones():
    return {"MulDiv": 0, "SumRes": 0, "Comparacion": 0, "Intercambio": 0}

def guardar_conteo(corridas, nombre="resultados\\conteo_flops.md"):  
    with open(nombre, "w", encoding="utf-8") as archivo:
        archivo.write("# Conteo de operaciones por paso\n\n")
        for metodo, pasos in corridas: 
            total_md = 0
            total_sr = 0
            total_comp = 0
            total_inter = 0
            archivo.write(f"## {metodo}\n\n")  
            archivo.write("| Paso | Mult/Div | Sum/Res | Total flops | Comparaciones | Intercambios |\n")
            archivo.write("|---|---|---|---|---|---|\n")
            for k in range(len(pasos)):
                c = pasos[k]
                flops = c["MulDiv"] + c["SumRes"]
                archivo.write(f"| {k + 1} | {c['MulDiv']} | {c['SumRes']} | {flops} "
                              f"| {c['Comparacion']} | {c['Intercambio']} |\n")
                total_md += c["MulDiv"]
                total_sr += c["SumRes"]
                total_comp += c["Comparacion"]
                total_inter += c["Intercambio"]
            archivo.write(f"| **Total** | **{total_md}** | **{total_sr}** | **{total_md + total_sr}** "
                          f"| **{total_comp}** | **{total_inter}** |\n\n")

        archivo.write("## Convención de conteo\n\n")
        archivo.write("- 1 flop = 1 operación aritmética elemental (+, -, *, /).\n")
        archivo.write("- Se separan multiplicaciones/divisiones de sumas/restas.\n")
        archivo.write("- Cada multiplicador se calcula una sola vez por fila (1 división).\n")
        archivo.write("- Solo se cuenta la eliminación hacia adelante (incluye la actualización de b). "
                      "La sustitución regresiva no se cuenta.\n")
        archivo.write("- Comparaciones e intercambios son sobrecosto del pivoteo y no son flops.\n")
        archivo.write("- Un intercambio de filas cuenta 2: una fila de A y un elemento de b.\n")

def guardar_estabilidad(corridas, matriz, nombre = "resultados\\conteo_flops.md"):  
    A = np.array([[float(v) for v in fila] for fila in matriz])
    kappa = np.linalg.cond(A, np.inf)
    u = 1e-28  #unidad de redondeo de la corrida (28 digitos)
    with open(nombre, "a", encoding = "utf-8") as archivo:  
        archivo.write("\n## Pivoteo y mantisa\n\n")
        archivo.write("| Metodo | Multiplicador maximo | Factor de crecimiento | Error relativo final | Bits perdidos |\n")
        archivo.write("|---|---|---|---|---|\n")
        for metodo, estab, sol, referencia in corridas:
            crecimiento = estab["MaxElem"] / estab["MaxInicial"]
            num = max(abs(sol[i] - referencia[i]) for i in range(len(sol)))
            den = max(abs(v) for v in referencia)
            error = float(num / den)
            bits = math.log2(error / u) if error > 0 else 0
            archivo.write(f"| {metodo} | {float(estab['MultMax']):.3e} | {float(crecimiento):.3e} "
                          f"| {error:.3e} | {bits:.1f} |\n")
        archivo.write("\nBits perdidos = log2(error relativo / u), con u = 1e-28 (28 digitos decimales). "
                      "El error se mide contra una corrida de 60 digitos.\n")
        archivo.write("\n## Condicionamiento\n\n")
        archivo.write(f"- kappa infinito de A = {kappa:.3e}\n")
        archivo.write(f"- Cota kappa * u (double, u = 2^-53) = {kappa * 2.0 ** -53:.3e}\n")
        archivo.write(f"- Digitos recuperables segun la cota = {-math.log10(kappa * 2.0 ** -53):.1f}\n")