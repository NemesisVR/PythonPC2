# Definir el rango
start = 1500
end = 2700

# Encontrar los números que cumplen con las condiciones
result = [number for number in range(start, end + 1) if number % 7 == 0 and number % 5 == 0]

# Imprimir los resultados
print(result)