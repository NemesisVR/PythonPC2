# Número de alumnos
n = int(input("Ingrese el número de alumnos: "))

# Lista de alumnos
alumnos = []

# Bucle de los datos de cada alumno
for _ in range(n):
    nombre = input("Ingrese el nombre del alumno: ")
    notas = [float(input(f"Ingrese la calificación {i+1} de {nombre}: ")) for i in range(3)]
    alumnos.append([nombre, notas])

# Listado de los alumnos
for alumno in alumnos:
    print(f"Alumno: {alumno[0]}, Notas: {alumno[1]}")
