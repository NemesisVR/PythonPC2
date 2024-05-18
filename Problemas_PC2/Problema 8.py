def factorial(numero):
    if numero < 0:
        return None
    elif numero == 0:
        return 1
    else:
        resultado = 1
        for i in range(1, numero + 1):
            resultado *= i
        return resultado

# Uso de la función
numero = 3
resultado = factorial(numero)
print(f"El factorial de {numero} es {resultado}")
