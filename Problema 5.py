def contar_digitos(numero, digito):
    cantidad = 0
    while numero > 0:
        if numero % 10 == digito:
            cantidad += 1
        numero //= 10
    return cantidad

# Uso de la función
numero = 125500
digito = 5
resultado = contar_digitos(numero, digito)
print(f"Cantidad de veces {digito} en el número: {resultado}")


