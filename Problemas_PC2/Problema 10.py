def convertir_fecha(fecha):
    meses = {
        "Enero": "01",
        "Febrero": "02",
        "Marzo": "03",
        "Abril": "04",
        "Mayo": "05",
        "Junio": "06",
        "Julio": "07",
        "Agosto": "08",
        "Septiembre": "09",
        "Octubre": "10",
        "Noviembre": "11",
        "Diciembre": "12"
    }
    
    # Separar la fecha en día, mes y año
    partes = fecha.split()
    dia = partes[1].strip(",")
    mes = meses.get(partes[0], partes[0])
    anio = partes[2]
    
    # Formatear la fecha en AAAA-MM-DD
    fecha_formateada = f"{anio}-{mes}-{dia:02}"
    return fecha_formateada

# Solicitar al usuario una fecha
fecha = input("Ingrese una fecha (en el formato mes/día/año o Mes día, año): ")

# Fecha en formato AAAA-MM-DD
fecha_formateada = convertir_fecha(fecha)

# Imprimir la fecha formateada
print("Fecha en formato AAAA-MM-DD:", fecha_formateada)
