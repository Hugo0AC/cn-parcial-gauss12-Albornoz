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