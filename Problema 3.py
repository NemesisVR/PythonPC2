numeros = []

while True:
    respuesta = input("¿Desea ingresar un número? (SI/NO): ").strip().upper()
    if respuesta == 'NO':
        break
    elif respuesta != 'SI':
        print("Respuesta no válida, por favor ingrese SI o NO.")
        continue
    numero = int(input("Ingrese el número: "))
    numeros.append(numero)

pares = len([num for num in numeros if num % 2 == 0])
impares = len(numeros) - pares

print(f"Números ingresados: {numeros}")
print(f"Cantidad de números pares: {pares}")
print(f"Cantidad de números impares: {impares}")
